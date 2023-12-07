# thesisGen
This app can read multiple PDF files to create a thesis out of it.

Python code to create a thesis by uploading relevant PDF files. 

<img width="777" alt="image" src="https://github.com/kamranferoz/thesisGen/assets/34434270/f42aaeb2-979e-4804-8e02-57ed185ee123">



thesisWithInput.py will let user give inputs for the thesis in terms of "Tital", "Author Name", and "Citation details"


A sample thesis created by this app!

<img width="509" alt="image" src="https://github.com/kamranferoz/thesisGen/assets/34434270/5a2ec1dd-4e72-41cb-a60d-d6bcc68d6161">

This program is a Thesis Generator application. It allows users to upload multiple PDF files, extract the text from these files, and generate a thesis on a given topic with citations. The program uses the Streamlit library for the user interface, PyMuPDF to extract text from PDF files, and OpenAI's GPT-3 model to generate the thesis.

The application offers several features:

User Inputs: Users can input their name and the title of the thesis.

PDF Upload: Users can upload multiple PDF files which will be used to generate the thesis.

Citations Input: Users can input citations, one per line, which will be included in the generated thesis.

Thesis Generation: When the user clicks the "Generate Thesis" button, the program generates a thesis on the given topic using OpenAI's GPT-3 model. The generated thesis includes the citations provided by the user.

Thesis Display: The generated thesis with citations is displayed to the user.

The application also includes a footer with the name of the user. If no PDF files are uploaded, the program displays a warning message.

https://genthesis.streamlit.app/
