import cv2
import numpy as np
from PIL import Image
import streamlit as st
from streamlit.uploaded_file_manager import UploadedFile

img_width, img_height = 0, 0

st.title("Image Uploader")


def UploadImage():
    uploaded_file = st.file_uploader(
        "Choose a image file", type=[
            "jpg", "png", "jpeg"])
    if uploaded_file is not None:
        # Convert the file to an opencv image.
        file_bytes = np.asarray(
            bytearray(
                uploaded_file.read()),
            dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        # Now do something with the image! For example, let's display it:
        st.image(opencv_image, channels="BGR")
    return uploaded_file


Received_image = UploadImage()


def Width_height():
    image = Image.open(Received_image)
    img_width, img_height = image.width, image.height
    st.write(
        "The resolution of the Uploaded image is {} X {}".format(
            img_width,
            img_height))


if Received_image is None:
    st.text("Please Upload Your Image!")
else:
    if st.button("Click This"):
        Width_height()
