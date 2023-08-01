# import neccessary library
import streamlit as st
import numpy as np
from PIL import Image

c1, c2 = st.columns(2)

with c1:
    st.markdown("## Image")
    st.image("https://bit.ly/edus3ha")

with c2:
    st.markdown("## Video")
    st.video("https://bit.ly/canibs3")

st.markdown("## Audio")
st.audio("https://bit.ly/rainaws3")

st.title("Super Basic Photo Editor")


def display_figures(img1, img2):
    fig1_left, fig2_right = st.columns(2)
    with fig1_left:
        st.markdown("## Original Image")
        st.image(img1)
    with fig2_right:
        st.markdown("## Edited Image")
        st.image(img2)


image_file = st.sidebar.file_uploader(
    "Upload an image file", type=['jpg', 'png', 'tif'])

if image_file is not None:
    input_image = Image.open(image_file)

    effect = st.sidebar.selectbox("Select the type of image manipulation", [
                                  'Rotate Image', 'Flip Image', 'Resize'])

    if effect == 'Rotate Image':
        angle = st.sidebar.select_slider(
            "Select the angle of rotation", [0, 90, 180, 270, 360])
        output_image = input_image.rotate(angle)

    if effect == 'Flip Image':
        mirror_choice = st.sidebar.radio("Choose how to flip the image", [
                                         'Horizontally', 'Vertically'])
        if mirror_choice == 'Horizonatally':
            output_image = input_image.transpose(Image.FLIP_LEFT_RIGHT)
        else:
            output_image = input_image.transpose(Image.FLIP_TOP_BOTTOM)

    if effect == 'Resize':
        scale_factor = st.sidebar.slider(
            "Select the percentage size", 5, 10, 6)
        output_image = input_image.resize(
            (input_image.width // scale_factor, input_image.height // scale_factor))

    if st.button("Process image"):
        display_figures(input_image, output_image)
