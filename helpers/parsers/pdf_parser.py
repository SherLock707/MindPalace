from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def parse_pdf(file):
    loader = PyPDFLoader(file.name)
    docs = loader.load()
    return RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50).split_documents(docs)
