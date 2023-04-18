import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

uploaded_image = st.file_uploader("Upload Image")

with st.expander("start Camera"):
    # start the camera
    camera_image = st.camera_input("camera")

if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert to grayscale
    gray_img = img.convert("L")

    # Render on the web
    st.image(gray_img)

if uploaded_image:
    img = Image.open(uploaded_image)
    gray_img = img.convert("L")
    st.image(gray_img)