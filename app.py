import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

st.title("📄 RAG Chatbot for Document Q&A")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
if uploaded_file:
    loader = PyPDFLoader(uploaded_file)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)

    retriever = vectorstore.as_retriever()
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    qa = RetrievalQA.from_chain_type(llm, retriever=retriever)

    query = st.text_input("Ask me anything about the document:")
    if query:
        st.write(qa.run(query))
