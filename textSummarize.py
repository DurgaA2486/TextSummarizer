import streamlit as st
from bardapi import Bard
import os
from pypdf import PdfReader

# Set up your Bard API key
os.environ['_BARD_API_KEY']="Your_API_Key"

# Function to summarize text using Bard API
def get_summary(text, word_limit):
    prompt = f"""
    Your task is to summarize the input text in approximately {word_limit} words.
    The input text is: {text}
    """
    try:
        # Sending the prompt to Bard API
        response = Bard().get_answer(prompt)["content"]
        return response  # Extracting the content from the Bard response
    except Exception as e:
        return f"Error occurred: {str(e)}"

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    extracted_text = ""
    for page in pdf_reader.pages:
        extracted_text += page.extract_text()
    return extracted_text

# Streamlit Interface for the chatbot
def main():
    st.title("Bard API Text Summarizer with PDF Upload")
    st.write("Provide text or upload a PDF file to summarize, and specify the number of words for the summary.")

    # Create a toggle for input method: PDF upload or manual text input
    input_method = st.radio(
        "Choose your input method:",
        ("Upload PDF", "Enter Text Manually")
    )

    user_input = ""

    if input_method == "Upload PDF":
        # Option to upload a PDF file
        uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
        if uploaded_file is not None:
            # Extract text from the uploaded PDF
            user_input = extract_text_from_pdf(uploaded_file)
            st.write("Extracted Text from PDF:")
            st.text_area("PDF Text (Read-Only):", user_input, height=200, disabled=True)  # Display PDF text as read-only

    elif input_method == "Enter Text Manually":
        # Manual text input
        user_input = st.text_area(
            "Enter the text you want to summarize:", 
            placeholder="Type or paste text here..."
        )

    # Word limit input
    word_limit = st.number_input(
        "Enter the number of words for the summary (min: 10):",
        min_value=10,
        step=5,
        value=100,
    )

    # Generate Summary button
    if st.button("Summarize"):
        if user_input.strip():  # Check if the input text is not empty
            summary = get_summary(user_input, word_limit)
            st.subheader("Generated Summary:")
            st.write(summary)
        else:
            st.warning("Please enter some text or upload a PDF file to summarize.")

if __name__ == "__main__":
    main()
