import time
import requests

url = "https://jsonplaceholder.typicode.com/posts"

def send_request():
    """
    sends a single request to API
    and returns status code
    """

    response = requests.get(url)
    return response.status_code

n = 10
print(f"Sending {n} requests to {url}")

start_time = time.time() # creates timestamp

for i in range(n):
    status = send_request()
    print(f"Req no {i + 1} - status: {status}")

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Time: {elapsed_time} secs")