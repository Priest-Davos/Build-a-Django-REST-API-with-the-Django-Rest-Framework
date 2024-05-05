import requests

# endpoint='https://httpbin.org/anything'
base_url='http://127.0.0.1:8000/'#or 'localhost:8000'
endpoint=base_url+"/api/"


response=requests.get(endpoint,params={"user":1}, json= {"query":"Helloo there"})
# print(response)# output= <Response [200]>
# print(response.headers)# {'Date': 'Fri, 03 May 2024 22:36:02 GMT', 'Content-Type': 'application/json', 'Content-Length': '394', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
# print(response.encoding)# utf-8

# print (response.text) 
# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.31.0",
#     "X-Amzn-Trace-Id": "Root=1-66356751-7ac14030318f852e43df6889"
#   },
#   "json": null,
#   "method": "GET",
#   "origin": "42.108.27.76",
#   "url": "https://httpbin.org/anything"
# }
print(response.json())