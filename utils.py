import streamlit as st
from langchain.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
    UnstructuredPowerPointLoader,
    UnstructuredHTMLLoader,
    UnstructuredExcelLoader,
)
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI

def load_document(file_path, file_ext):
    if file_ext == '.pdf':
        return PyPDFLoader(file_path=file_path).load()
    elif file_ext == '.txt':
        return TextLoader(file_path=file_path).load()
    elif file_ext in ['.doc', '.docx']:
        return Docx2txtLoader(file_path=file_path).load()
    elif file_ext == '.ppt':
        return UnstructuredPowerPointLoader(file_path=file_path).load()
    elif file_ext == '.html':
        return UnstructuredHTMLLoader(file_path=file_path).load()
    elif file_ext == '.xls':
        return UnstructuredExcelLoader(file_path=file_path).load()
    elif file_ext == '.csv':
        return CSVLoader(file_path=file_path).load()

def load_multiple_documents(file_infos):
    documents_to_text = []
    for file_path, file_ext in file_infos:
        documents_to_text.extend(load_document(file_path, file_ext))
    return documents_to_text

def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(documents)
    return text_chunks

def get_vectorstore(text_chunks, openai_keys):
    embeddings = OpenAIEmbeddings(openai_api_key=openai_keys, model='text-embedding-ada-002')
    vector_store = FAISS.from_documents(documents=text_chunks, embedding=embeddings)
    return vector_store

def create_conservational_chain(vector_store, openai_keys):
    template = """
    As a highly competent AI assistant, your role is analyze the documents provided by the user, Your responses should be grounded in the context contained within these documents.
      For each user query provided in the form of chat, apply the following guidelines:
    - If the answer is within the document's context, provide a detailed and precise response.
    - If the answer is not available based on the given context, clearly state that you don't have the information to answer.
    - If the query falls outside the scope of the context, politely clarify that your expertise is limited to answering questions directly related to the provided documents.

    With the dataset, in FTR column, H means that the team in the Home column won the match and that means that team recevied 
    3 points from that match, while the team in the Away column lost the match and received 0 points. If the value in FTR is A, the team in the Away column
    won the match and received 3 points while the team in the Home column lost the match and received 0 points. If the FTR column contains a value of D, it
    means that the match ended in a draw and the teams in the Home and Away columns both received 1 point. Using this, it is possible to 
    calculate the number of points accumulated by each team during a season and the team with the most points win the league that season.

    When responding, prioritize accuracy and relevance:
    Context:
    {context}

    Question:
    {question}
    """
    system_message_prompt = SystemMessagePromptTemplate.from_template(template=template)
    human_template = "{question}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    qa_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3, openai_api_key=openai_keys)
    memory = ConversationBufferMemory(memory_key='chat_history',return_messages=True)
    qa_chain = ConversationalRetrievalChain.from_llm(llm=model, retriever=vector_store.as_retriever(), memory=memory, combine_docs_chain_kwargs={'prompt': qa_prompt})
    return qa_chain


def initialize_state():
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "How can I help?"}]
    if "qa_chain" not in st.session_state:
        st.session_state.qa_chain = None

def load_qa_chain(saved_files_info, openai_keys):
    loaded_docs = load_multiple_documents(saved_files_info)
    docs_splits = split_documents(loaded_docs)
    vectordb = get_vectorstore(docs_splits, openai_keys)
    return create_conservational_chain(vectordb, openai_keys)
