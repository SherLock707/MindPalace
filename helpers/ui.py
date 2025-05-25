import gradio as gr
from helpers.parser_factory import parse_input
from helpers.vectorstore import add_documents

def build_ui(vectorstore, qa_chain):
    with gr.Blocks() as demo:
        gr.Markdown(\"\"\"# 🧠 MindPalace\nYour private mind for querying documents.\"\"\")
        
        with gr.Row():
            file_input = gr.File(label=\"Upload File\")
            url_input = gr.Textbox(label=\"or Enter URL\")
            upload_btn = gr.Button(\"Ingest\")

        chatbot = gr.Chatbot()
        query_input = gr.Textbox(label=\"Ask something...\")
        send_btn = gr.Button(\"Send\")

        def ingest(file, url):
            docs = parse_input(file=file, url=url)
            add_documents(vectorstore, docs)
            return f\"Added {len(docs)} document chunks.\"

        def ask(query, history):
            answer = qa_chain.run(query)
            history.append((query, answer))
            return history, history

        upload_btn.click(ingest, inputs=[file_input, url_input], outputs=None)
        send_btn.click(ask, inputs=[query_input, chatbot], outputs=[chatbot, chatbot])

    return demo
