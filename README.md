🔹 2. Voice-Enabled Chatbot

Description (for GitHub/README & CV):
Developed an AI Voice Assistant that takes speech input, processes it with Whisper (speech-to-text), generates responses with LLMs, and replies via text-to-speech. Mimics an AI personal assistant workflow.

Tech Stack:

Whisper (OpenAI) for STT

OpenAI GPT (or HuggingFace LLM) for responses

gTTS / pyttsx3 for TTS

Gradio / Streamlit UI

Folder Structure:
voice-chatbot/
│── app.py                  # Streamlit/Gradio frontend
│── requirements.txt
│── utils/
│    ├── stt.py             # speech-to-text
│    ├── llm.py             # chatbot logic
│    └── tts.py             # text-to-speech
│── README.md


# 📄 RAG Chatbot for Document Q&A
Upload any PDF and ask questions — chatbot retrieves context using FAISS/Chroma and generates answers with an LLM.

## Tech Stack
- LangChain
- FAISS
- OpenAI GPT / HuggingFace LLMs
- Streamlit
