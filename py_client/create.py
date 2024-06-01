import requests

base_url='http://127.0.0.1:8000/'#or 'localhost:8000'

endpoint = f"{base_url}api/products/create-products"

payload={'title': 'test77', 'content': 'test content', 'price': '1000',  'discount_percentage': 10,}
get_response=requests.post(endpoint,json=payload)
print(get_response.json())

