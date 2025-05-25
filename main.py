from helpers.vectorstore import get_vectorstore
from helpers.llm_chain import get_qa_chain
from helpers.parser_factory import parse_input
from helpers.ui import build_ui

# Initialize vectorstore and LLM chain
vectorstore = get_vectorstore()
qa_chain = get_qa_chain(vectorstore)

demo = build_ui(vectorstore, qa_chain)

demo.launch()