from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def get_vectorstore():
    embeddings = HuggingFaceEmbeddings()
    return FAISS(embedding_function=embeddings.embed_query)

def add_documents(vectorstore, documents):
    vectorstore.add_documents(documents)
