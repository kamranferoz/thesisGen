import streamlit as st
import fitz  # PyMuPDF
import re

# Streamlit UI components
st.title("Thesis Generator App")
st.write("Upload multiple PDF files and generate a thesis with citations.")

# Upload multiple PDF files
pdf_files = st.file_uploader("Upload PDF Files", type=["pdf"], accept_multiple_files=True)

# Function to add citations to text
def add_citations_to_text(text):
    # Replace [1], [2], ... with actual citations
    citation_pattern = re.compile(r'\[(\d+)\]')
    
    def replace_citations(match):
        reference_number = match.group(1)
        # Replace with your actual citation format
        return f"[{reference_number}] Author, Year"

    processed_text = citation_pattern.sub(replace_citations, text)
    return processed_text

# Generate thesis button
if st.button("Generate Thesis"):
    if pdf_files:
        # Extract text from uploaded PDFs
        text = ""
        for pdf_file in pdf_files:
            pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
            for page_num in range(pdf_document.page_count):
                text += pdf_document.get_page_text(page_num)

        # Process text and add citations
        processed_text = add_citations_to_text(text)

        # Display the generated thesis with citations
        st.write("Generated Thesis with Citations:")
        st.write(processed_text)
    else:
        st.warning("Please upload at least one PDF file.")

# Streamlit app footer
st.write("Created by Kamran Feroz")
