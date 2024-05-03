# RAGIntellect

RAGIntellect is a Streamlit-based web application that leverages Retrieval-Augmented Generation (RAG) to interactively retrieve information and synthesize knowledge from uploaded documents. This application combines the power of Google's Gemini model and OpenAI's language models to provide contextual answers based on the content of the documents provided.

## Overview

The application allows users to:
- Upload documents in various formats including PDF, DOCX, TXT, PPT, HTML, CSV, and XLS.
- Ask questions via a chat interface and receive answers that are contextually relevant to the uploaded documents.
- Use a convenient sidebar for interactive file uploads and API key management.

## System Architecture

1. **app.py**: This is the main entry point for the Streamlit application. It initializes the application, loads environment variables, and uses the Gemini model from Google's Generative AI for chat responses. It also handles the UI components for user interactions such as asking questions and displaying answers.

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

