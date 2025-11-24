from PyPDF2 import PdfReader

def extract_text_from_pdf(uploaded_file):
    """
    Extract text from a PDF file uploaded via Streamlit.
    """
    reader = PdfReader(uploaded_file)
    all_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            all_text += text + "\n\n"

    return all_text
