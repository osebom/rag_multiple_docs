from dotenv import load_dotenv
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_google_genai import ChatGoogleGenerativeAI

import os
import streamlit as st

def main():
    load_dotenv()
    path="/Users/ojonyeagwu/Desktop/epl_data/data/premier-league-matches.csv" #path  to csv file of movies
    # Load the OpenAI API key from the environment variable
    if os.getenv("GOOGLE_GEMINI_KEY") is None or os.getenv("GOOGLE_GEMINI_KEY") == "":
        print("Please set the API_KEY for Gemini")
        exit(1)
    else:
        print("API_KEY is set")

    st.set_page_config(page_title="EPL Chat")
    st.header("English Premier League Chatbot")

    csv_file = path
    llm = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=os.environ["GOOGLE_GEMINI_KEY"])
    if csv_file is not None:

        agent = create_csv_agent(
            llm, csv_file, verbose=True)

        query = st.text_input("Ask your question:")

        if query is not None and query != "":
            with st.spinner(text="Loading..."):
                st.write(agent.run(query))


if __name__ == "__main__":
    main()