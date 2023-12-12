import requests

response = requests.post(
    "http://127.0.0.1:5000/users/",
    json={"name": "user_1", "password": "dfobgops5b5o4iubub"},
)

print(response.status_code)
print(response.text)


response = requests.patch(
    "http://127.0.0.1:5000/users/1",
    json={"name": "new_name", "password": "dfobgops5b5o4iubub"},
    headers={"Content-Type": "application/json"},
)

print(response.status_code)
print(response.text)

response = requests.get("http://127.0.0.1:5000/users/1")

print(response.status_code)
print(response.text)


response = requests.delete("http://127.0.0.1:5000/users/1")

print(response.status_code)
print(response.text)
