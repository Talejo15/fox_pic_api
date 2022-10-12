import requests

response = requests.get("https://randomfox.ca/floof")
response_json = response.json()
image_response = requests.get(response_json['image'])

fox_pic = open("fox_image.jpg", 'wb')
fox_pic.write(image_response.content)
fox_pic.close()