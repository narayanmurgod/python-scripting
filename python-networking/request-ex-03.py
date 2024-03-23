import requests 

r=requests.get('https://api.github.com/events')
print(r) #<Response [200]>
r1 = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(r1) #<Response [200]>

r2 = requests.get('https://api.github.com/events', stream=True)
print(r2.raw) #<urllib3.response.HTTPResponse object at 0x7ef8b8ec1c40>
print(r2.json()) #[{'id': '36823297250', 'type': 'IssueCommentEvent', 'actor..........

