import cv2
import streamlit as st

st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)
# print(camera)

while run:
    _,frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')

# import cv2

# videoCaptureObject = cv2.VideoCapture(0)
# result = True
# while(result):
#     ret,frame = videoCaptureObject.read()
#     cv2.imwrite("NewPicture.jpg",frame)
#     result = False
# videoCaptureObject.release()
# cv2.destroyAllWindows()