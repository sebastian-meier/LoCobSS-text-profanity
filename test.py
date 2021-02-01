import requests

url = 'http://localhost:1080/predict'

body = {
    "text": "Arschpimmel"
}

response = requests.post(url, data=body)

print(response.json())