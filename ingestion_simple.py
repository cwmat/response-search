from dotenv import load_dotenv
from langchain_community.document_loaders import Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
import os

load_dotenv()

INDEX_NAME = "response-search-index"
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")


def ingest_docs():
    directory = "data"
    documents = []

    for filename in os.listdir(directory):
        if filename.endswith(".docx"):
            filepath = os.path.join(directory, filename)
            loader = Docx2txtLoader(filepath)
            raw_documents = loader.load()
            documents.extend(raw_documents)  # Collect all documents into one list

    print(f"Loaded {len(documents)} documents")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
    split_documents = text_splitter.split_documents(documents)

    print(f"Going to add {len(split_documents)} documents to Pinecone")
    PineconeVectorStore.from_documents(
        split_documents, embeddings, index_name=INDEX_NAME
    )
    print("****Loading to vectorstore done ***")


if __name__ == "__main__":
    ingest_docs()
