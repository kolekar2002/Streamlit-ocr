import streamlit as st
import numpy as np
import pytesseract #pythn wrapper for the OCR software
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'

st.title('OPTICAL CHARACTER RECOGNITION')
st.text('upload the image')
Uploaded_file = st.sidebar.file_uploader('choose an image:', type = ["jpg","png","jpeg"])#create a file uploader in the sidebar
if Uploaded_file is not None: 
  img = Image.open(Uploaded_file)# read the uploaded image , open it 
  st.image(img , caption = 'Uploade Image', use_column_width =True ) #display the image on the webapp screen ,use_column_width = true means keep orginal image size
  st.write(" ") #print the blank space

  if st.button('PREDICT'):
    st.write("extract text :")
    output = pytesseract.image_to_string(img) #pytesseract converts image to text and then prints the output
    st.write(output)
