import requests
response = requests.get("https://abx.com")
#print(response.status_code)
if response:
    print("Success!")
else:
    raise Exception(f"Non-success status code: {response.status_code}")  #Exception: Non-success status code: 403