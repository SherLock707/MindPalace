# 🧠 MindPalace

**MindPalace** is a private, local-first AI assistant that lets you upload and chat with your documents. Inspired by Sherlock Holmes' mental filing system, it parses and stores knowledge from your files into an in-memory vector store, ready to be queried via natural language.

## 🚀 Features

- 🧾 **Upload PDFs, text files, images (OCR), or URLs**
- 🧠 **Ask questions using a local LLM** (via Ollama)
- 🗃️ **All processing happens locally** — no cloud, no leaks
- 🧩 **Modular parser architecture**
- 🎛️ **Simple Gradio UI**

## 🛠️ Stack

- **LangChain** – Orchestration & document processing
- **Ollama** – Run LLMs like LLaMA3, Mistral, or Gemma locally
- **FAISS** – In-memory vector store
- **Gradio** – Web UI
- **Tesseract OCR** – For image-to-text conversion

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/SherLock707/MindPalace.git
cd MindPalace

# Install dependencies
pip install -r requirements.txt

# Optional: Ensure Tesseract is installed
# Ubuntu: sudo apt install tesseract-ocr
# macOS: brew install tesseract
```

## 🧪 Run the App

Start your local LLM first:

```bash
ollama run llama3
```

Then start the MindPalace server:

```bash
python main.py
```

## 🧰 Folder Structure

```
MindPalace/
├── main.py
├── requirements.txt
├── README.md
├── helpers/
│   ├── parser_factory.py
│   ├── vectorstore.py
│   ├── llm_chain.py
│   ├── ui.py
│   └── parsers/
│       ├── pdf_parser.py
│       ├── txt_parser.py
│       ├── image_parser.py
│       └── url_parser.py
```

## 🔒 Privacy First

MindPalace runs entirely on your machine. No API calls, no telemetry, no vendor lock-in.

## 📌 Roadmap

- [ ] Add persistent vector DB option (Chroma, SQLite)
- [ ] Highlight citations in responses
- [ ] Export & reload sessions
- [ ] CLI interface for headless mode

## 🙏 Credits

- [LangChain](https://langchain.com/)
- [Ollama](https://ollama.com/)
- [FAISS](https://github.com/facebookresearch/faiss)

## 📄 License

MIT License. Yours to hack, extend, and evolve.

---

**🧑‍💻 Author**

Built by an engineer who believes your documents should stay yours. Let AI read your files without sending them anywhere else.