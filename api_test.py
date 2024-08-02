import requests

# post request test
url_post = "https://bjfinservtask-1-r1815985.deta.app/bfhl"
payload = {
    "data": ["A", "C", "z"]
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url_post, json=payload, headers=headers)

print(response.text)
