import requests
import json

# Proxy URL
url = "https://aicraftingtableproxy.onrender.com/chat"

# Request body
data = {
    "model": "gpt-4o",
    "messages": [
        {"role": "user", "content": "Hello from Python program!"}
    ]
}

# Print the request for debugging
print("Sending request to:", url)
print("Request body:")
print(json.dumps(data, indent=2))

try:
    response = requests.post(url, json=data, timeout=100)
    print("Status code:", response.status_code)
    print("Response text:", response.text)

    response.raise_for_status()
    result = response.json()

    # Extract the assistant's message
    message = result['choices'][0]['message']['content']
    print("Assistant:", message)

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
    print("Full response:")
    print(response.text if 'response' in locals() else 'No response received')
except (KeyError, IndexError, json.JSONDecodeError) as e:
    print("Unexpected response format or JSON decode error:", e)
