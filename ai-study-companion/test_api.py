import requests

url = "http://127.0.0.1:8001/summarize"
payload = {"text": "This is a local test request."}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
print("Status:", response.status_code)
print("Response:", response.json())



