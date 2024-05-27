import cv2
from PIL import Image
import pytesseract
import streamlit as st
import google.generativeai as genai

genai.configure(api_key="GEMINI-API-KEY") #Replace with your Gemini API Key
gemini_model = genai.GenerativeModel('gemini-pro')
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'  #Replace with your tesseract OCR path

#OCR function
def extract_and_format_code(img_path):
    with st.spinner('Extracting Code using OCR'):
        img = Image.open(img_path)
        text = pytesseract.image_to_string(img, lang='eng')
        formatted_code = gemini(text)
        return formatted_code

#format the code using an LLM
def gemini(text):
    with st.spinner('Format Code using an LLM(Gemini)'):
        response = gemini_model.generate_content(
            f'''You're tasked with Formatting code that i have extracted from an image.
                Preserve the indentation of the code strictly and remove the line numbering if any exists.
                Return only the formatted code in the form of a markdown only.
                The extracted code is : {text}'''
        )
        formatted_text = (response.text)
        return formatted_text

def main():
    st.title('Image to Code')
    st.write("Upload an image containing code to extract the formatted code from it")

    uploaded_file = st.file_uploader("Upload an image",type = ['png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)

        if st.button('Extract and Format Code'):
            formatted_code = extract_and_format_code(uploaded_file)
            st.markdown(f'```{formatted_code}```')

#Run using - streamlit run Image2Code.py
if __name__ == '__main__': 
    main()
