# 📄 RAG Chatbot for Document Q&A

Upload any PDF and ask questions — the chatbot retrieves relevant context using **FAISS/Chroma** and generates answers with an **LLM (OpenAI/HuggingFace)**.  
Built with **LangChain** and deployed via **Streamlit** for an interactive web app.

---

## ✨ Features
- 📑 Upload **PDF documents** (e.g., medical, legal, reports).
- 🔍 Text is split and embedded into a **vector store (FAISS/Chroma)**.
- 🤖 **LLM (GPT / HuggingFace)** retrieves context and generates accurate answers.
- 🖥️ **Streamlit interface** for easy interaction.

---

## 🛠️ Tech Stack
- **Python**
- **LangChain** – pipeline orchestration
- **FAISS / ChromaDB** – vector database
- **OpenAI GPT / HuggingFace LLMs**
- **Streamlit** – frontend
- **PyPDF** – document parsing

---

## 📂 Project Structure
rag-chatbot/
│── app.py # Streamlit app
│── requirements.txt
│── utils/
│ ├── loader.py # PDF loader & splitter
│ ├── embeddings.py # Vector store setup
│ └── qa_chain.py # QA pipeline
│── data/
│ └── sample.pdf
│── assets/
│ ├── streamlit_ui.png
│ └── pipeline_diagram.png
│── README.md


---

## 🚀 Setup

```bash
# Clone the repo
git clone https://github.com/<your-username>/rag-chatbot.git
cd rag-chatbot

# Create virtual environment
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt


▶️ Run
streamlit run app.py
