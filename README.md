# RAGIntellect

RAGIntellect is a Streamlit-based web application that leverages Retrieval-Augmented Generation (RAG) to interactively retrieve information and synthesize knowledge from uploaded documents. This application combines the power of Google's Gemini model and OpenAI's language models to provide contextual answers based on the content of the documents provided.

## Overview

The application allows users to:
- Upload documents in various formats including PDF, DOCX, TXT, PPT, HTML, CSV, and XLS.
- Ask questions via a chat interface and receive answers that are contextually relevant to the uploaded documents.
- Use a convenient sidebar for interactive file uploads and API key management.

## System Architecture

1. **app.py**: This file is used to create #csv agent# to communicate with the Premier League CSV file using the Gemini model from Google's Generative AI for chat responses. It also handles the UI components for user interactions such as asking questions and displaying answers. Its performance was very poor as it needed more context to be able to better answer questions about the Premier League's history. Below are some screenshots from its outputs:

<img width="468" alt="image" src="https://github.com/osebom/rag_multiple_docs/assets/40761922/aa393f30-39e6-4b9f-abd9-b784cabc28a0">
<img width="468" alt="image" src="https://github.com/osebom/rag_multiple_docs/assets/40761922/947cadaf-9f7d-4993-b104-1c1b59f4baa3">
<img width="468" alt="image" src="https://github.com/osebom/rag_multiple_docs/assets/40761922/9f25a53f-5dfc-4d51-865d-ea131d9f47df">


2. **utils.py**: Contains utility functions essential for document processing:
   - Document loading functions for different file formats.
   - Document splitting into manageable chunks for processing.
   - Vector store creation using OpenAI embeddings to facilitate efficient retrieval.
   - Creation of conversational chains that integrate retrieval with response generation.

3. **sidebar.py**: Manages the Streamlit sidebar for configuration. It handles:
   - File uploads and validation of file formats.
   - Input of API keys for Google and OpenAI services.
   - Starting the document processing chain once files and keys are provided.

4. **app2.py**: Orchestrates the initialization and main interactive logic of the application. It:
   - Initializes session state variables.
   - Loads the QA chain after validating API keys and processing uploaded documents.
   - Manages the chat interface, processing user prompts, and displaying conversation history.

## Installation

To set up and run RAGIntellect, follow these steps:

```bash
git clone <your-repository-url>
cd RAGIntellect
pip install -r requirements.txt

