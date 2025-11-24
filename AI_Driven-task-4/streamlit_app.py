# streamlit_app.py
import streamlit as st
from PyPDF2 import PdfReader
from utils.agent_client import call_agent_via_mcp

st.set_page_config(page_title="Study Notes Summarizer & Quiz Generator", layout="wide")
st.title("📚 Study Notes Summarizer & Quiz Generator")

# PDF Upload
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file is not None:
    # Extract text from PDF
    pdf_reader = PdfReader(uploaded_file)
    pdf_text = ""
    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            pdf_text += text + "\n"

    st.subheader("Extracted PDF Text")
    st.text_area("PDF Text", pdf_text, height=200)

    # Call MCP Agent on Button Click
    if st.button("Generate Summary & Quiz"):
        with st.spinner("Generating summary and quiz..."):
            instructions = "Summarize the PDF and generate a quiz"
            result = call_agent_via_mcp(pdf_text, instructions)

        st.subheader("Agent Result")
        st.json(result)
