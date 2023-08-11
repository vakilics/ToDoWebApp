import streamlit as st
#pip install pillow to work on image!
from PIL import  Image

st.header("Weclome to Vakili image converter!")
st.subheader("Convert Color to Grayscale!")

#Create a file uploader component
upload_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    #Provode Camera_image to convert_image to the grayscale version
    img = Image.open(camera_image)
    gray_camera_img = img.convert('L')
    st.image(gray_camera_img)

# Check if the image exists / user uploaded alrady
if upload_image:
    #Open
    img = Image.open(upload_image)
    gray_upload_img = img.convert('L')
    #Display
    st.image(gray_upload_img)
