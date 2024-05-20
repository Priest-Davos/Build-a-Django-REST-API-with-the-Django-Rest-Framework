import requests

base_url='http://127.0.0.1:8000/'#or 'localhost:8000'
id=13
endpoint = f"{base_url}api/products/{id}/"

get_response=requests.get(endpoint)
print(get_response.json())

