import requests

url = 'https://xyz.com'

response = requests.get(url)

if response.status_code == 200:
    print("Site is valid")
else:
    print("site isn't valid")

#print("\nResponse Headers:")
#print(response.headers)

#print("\nResponse Text:")
#print(response.text)
