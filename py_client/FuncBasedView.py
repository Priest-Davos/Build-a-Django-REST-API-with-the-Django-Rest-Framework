import requests

base_url='http://127.0.0.1:8000/'#or 'localhost:8000'

endpoint = f"{base_url}api/products/funcBased/"

# create a product
payload={'title': 'test79', 'content': 'test content', 'price': '1000',  'discount_percentage': 10,}
get_post_response=requests.post(endpoint,json=payload)
print(get_post_response.json())


#list all products
get_response=requests.get(endpoint)
print(get_response.json())


# fetch a  unique propduct using id 
endpoint = f"{base_url}api/products/funcBased/1"
get_response=requests.get(endpoint)
print(get_response.json())

