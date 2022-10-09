import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint, json={"name": "gopal"})  # HTTP request

# print(get_response.text)  # print raw text response
print(get_response.json()['message'])
