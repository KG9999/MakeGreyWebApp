from PIL import Image
import streamlit as st
with st.expander("Start Camera"):
    image_input=st.camera_input(label="Camera")


if image_input:
    my_image=Image.open(image_input)
    grey_img=my_image.convert("L")
    st.image(grey_img)