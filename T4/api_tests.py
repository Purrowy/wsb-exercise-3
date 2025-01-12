import requests

url = "https://jsonplaceholder.typicode.com/posts"

print(f"Sending GET request to {url}")

response = requests.get(url)

print(f"Response status code: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    print(f"Contents: {data}")
else:
    print("Not valid response")