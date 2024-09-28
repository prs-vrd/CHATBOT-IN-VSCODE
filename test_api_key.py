import requests

API_KEY = "AIzaSyCqxTYDTxZ9Mgq64wSPQxMaQ9lz9ipqk-s"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}"

headers = {
    "Content-Type": "application/json"
}

# Update the payload according to the API's expected format
payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Explain how AI works"
                }
            ]
        }
    ]
}

response = requests.post(url, headers=headers, json=payload)

print("Status Code:", response.status_code)
print("Response:", response.json())
