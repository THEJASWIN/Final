import cv2
import requests
import numpy as np
from PIL import Image
import streamlit as st
from streamlit.uploaded_file_manager import UploadedFile

img_width, img_height = 0, 0

st.title("Image Uploader")

def uploadImage():
    uploaded_file = st.file_uploader(
        "Choose a image  file", type=[
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
    # temp = uploaded_file.name
    print(uploaded_file)

    # image_data = open(temp, "rb").read()

    # response = requests.post(
    # "http://localhost:80/v1/vision/custom/dark",
    # files={
    #     "image": image_data}).json()

    # for object in response["predictions"]:
    #     print(object["label"])
    #     print(response)
    return uploaded_file


Received_image = uploadImage()

# def deepStack():
#     image_data = open(uploaded_file, "rb").read()

#     response = requests.post(
#     "http://localhost:80/v1/vision/custom/dark",
#     files={
#         "image": image_data}).json()

#     for object in response["predictions"]:
#         print(object["label"])

def Width_height():
    image = Image.open(Received_image)
    print(image)
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