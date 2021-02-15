import requests

url = 'https://profanity-rzuu3ecqxa-ey.a.run.app/predict'

body = {
    "text": "Shit fuck"
}

response = requests.post(url, data=body)

print(response.json())