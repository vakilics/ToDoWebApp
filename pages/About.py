import streamlit as st

st.write("Welcome to my simple web app!")
st.write("Contact me:")
st.write("hamidgml@gmail.com")
from PIL import Image
image = Image.open('pages/AVA.png')
st.image(image, caption='Greetings! ')
