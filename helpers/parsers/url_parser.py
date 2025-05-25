from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def parse_url(url):
    loader = WebBaseLoader(url)
    docs = loader.load()
    return RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50).split_documents(docs)
