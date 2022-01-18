import requests
import os


image_data = open("NewPicture.jpg", "rb").read()

response = requests.post(
    "http://localhost:80/v1/vision/custom/dark",
    files={
        "image": image_data}).json()
os.remove("NewPicture.jpg")
for object in response["predictions"]:
    print(object["label"])

print(response)
