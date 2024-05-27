# Image2Code

Users can upload an image containing code via a Streamlit interface. Tesseract OCR extracts the text from the uploaded image. The extracted text is then sent to Google's Gemini LLM, which formats the code by adding appropriate indentation and removing line numbers displayed in the IDE. The final formatted code is displayed back to the user in a readable format using Markdown, allowing users to copy it with its formatting intact. This method ensures accurate text extraction and formatting, providing an efficient solution for converting image-based code into a usable format. For the OCR to effectively extract text, it is essential that the uploaded images are of high quality.

## Example

![Example Screenshot](https://github.com/Arjun-254/Image2Code/assets/102243820/6271b62c-acfe-4cd7-96d4-380174e3dbc2)

## Key Points

1. **Upload Image**: Use the Streamlit interface to upload an image containing code.
   
2. **Text Extraction**: Tesseract OCR will extract the text from the uploaded image.

3. **Code Formatting**: Google's Gemini LLM will format the extracted code by adding appropriate indentation and removing line numbers.

4. **Display Formatted Code**: The final formatted code will be displayed back to the user in Markdown format.

## Requirements

- Python 3.x
- Streamlit
- Tesseract OCR
- Opencv_python
- Google's Gemini API key



