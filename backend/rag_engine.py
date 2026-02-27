from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os


def build_retriever():

    documents = []

    for file in os.listdir("documents"):
        with open(f"documents/{file}", "r", encoding="utf-8") as f:
            documents.append(f.read())

    splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    docs = splitter.create_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    vectorstore = FAISS.from_documents(docs, embeddings)

    return vectorstore.as_retriever()