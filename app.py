import streamlit as st
from PIL import Image
from ocr import ocr_image  

st.title("OCR and Keyword Search Application")


uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])


if uploaded_file:
    image = Image.open(uploaded_file)  
    st.image(image, caption="Uploaded Image.", use_column_width=True)  

    extracted_text = ocr_image(uploaded_file)  
    st.write("Extracted Text:")
    st.write(extracted_text)  

    
    search_keyword = st.text_input("Enter keyword to search:")
    
    
    if search_keyword:
        if search_keyword.lower() in extracted_text.lower():
            st.success(f"Keyword '{search_keyword}' found!")  
        else:
            st.error(f"Keyword '{search_keyword}' not found.")  
