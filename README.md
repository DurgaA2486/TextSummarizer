## TextSummarizer
This text summarizer is built using Streamlit to create a user-friendly web-based interface that interacts with the Bard API. It allows users to summarize text by either uploading a PDF or entering text manually. The app extracts and processes the content, providing a concise summary based on the input provided.

## How It Works:
1. Open the code in vscode.
2. Install the neccessary dependencies mentioned below and run the code.
3.  **Choose Input Method:**
   - The user can choose one of two input methods given below:
     - **Upload a PDF**: Users can upload a PDF file, and the text will be extracted using the `pypdf` library.
     - **Enter Text Manually**: Users can type or paste the text directly into the text input box.
4. **Text Extraction (PDF Upload):**
   - If the user uploads a PDF file, the text is extracted from all the pages using `PdfReader` from the `pypdf` library. The extracted text is displayed in a read-only text area for the user's reference.
5. **Generate Summary:**
   - After providing the input text (either manually or from the PDF), the app sends the text to the **Bard API** for summarization.
   - The user can set a **word limit** for the summary, which controls the length of the generated summary.

6. **Display Summary:**
   - Once the "Summarize" button is clicked, the app processes the text and displays the summarized content based on the word limit specified.
     
## Dependencies:
**Streamlit:** Used for building the web interface.  
**Bard API Client:**  For interacting with Google's Bard API to generate summaries.  
**pypdf:**  For extracting text from PDF files.  
**os:**  For setting the environment variable for the Bard API key.  

## Screenshot of the interface after running the code
![Screenshot 2025-02-18 092737](https://github.com/user-attachments/assets/c0a23287-c4be-4c54-b9f0-3dedcff82199)
