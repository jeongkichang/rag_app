import boto3
from langchain_community.embeddings import BedrockEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.chat_models import BedrockChat
import os
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize Boto3 session
session = boto3.Session()

def get_llm():
    model_kwargs = {
        "max_tokens": 1024,
        "temperature": 0
    }

    llm = BedrockChat(
        model_id="anthropic.claude-3-sonnet-20240229-v1:0",
        model_kwargs=model_kwargs
    )

    return llm

def get_index():
    embeddings = BedrockEmbeddings()

    pdf_paths = [
        "230101_230306.pdf",
        "230307_230614.pdf",
        "230605_230922.pdf",
        "230923_231231.pdf"
    ]  # PDF 파일 경로 리스트
    loaders = []

    for path in pdf_paths:
        if os.path.exists(path):
            try:
                loaders.append(PyPDFLoader(file_path=path))
            except Exception as e:
                logging.error(f"Error loading {path}: {e}")
        else:
            logging.warning(f"File {path} does not exist.")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )

    index_creator = VectorstoreIndexCreator(
        vectorstore_cls=FAISS,
        embedding=embeddings,
        text_splitter=text_splitter
    )

    index_from_loader = index_creator.from_loaders(loaders)

    return index_from_loader

def get_rag_response(index, question):
    llm = get_llm()

    response_text = index.query(question=question, llm=llm)

    return response_text

def generate_response(index, question):
    # Generate text response based on the question
    response_text = get_rag_response(index, question)

    return response_text
