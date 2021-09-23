import requests

image_data = open("Image.jpg", "rb").read()

response = requests.post(
    "http://localhost:81/v1/vision/custom/dark",
    files={
        "image": image_data}).json()

for object in response["predictions"]:
    print(object["label"])

print(response)
