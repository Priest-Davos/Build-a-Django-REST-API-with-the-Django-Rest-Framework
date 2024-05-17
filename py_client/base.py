import requests

# endpoint='https://httpbin.org/anything'
base_url='http://127.0.0.1:8000/'#or 'localhost:8000'
endpoint=base_url+"/api/"


# response=requests.get(endpoint,params={"user":1}, json= {"query":"Helloo there"})
# print(response.json())

post_response=requests.post(endpoint, json={"title":"dead" })
print(post_response.json() )

