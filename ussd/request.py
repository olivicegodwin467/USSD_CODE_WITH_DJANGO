import requests

url = "http://127.0.0.1:8000/api/ussd/"
data = {
    "text": "",
    "session_id": "enter session Id",
    "phone_number": "phone number"
}

response = requests.post(url, json=data)
print(response.json())  # Print the server response
