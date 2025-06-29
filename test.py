import requests

# Proxy URL
url = "https://aicraftingtableproxy.onrender.com/chat"

# Request body for OpenAI Chat API
data = {
    "model": "gpt-4o",
    "messages": [
        {"role": "user", "content": "Hello, AI Crafting Table Proxy!"}
    ]
}

# Send POST request
response = requests.post(url, json=data)

# Print the response
if response.ok:
    print("Response:")
    print(response.json())
else:
    print("Error:")
    print(response.status_code)
    print(response.text)
