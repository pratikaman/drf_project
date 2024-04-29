# HTTP request -> HTML
# REST API HTTP request -> JSON

import requests

# endpoint = 'https://httpbin.org/status/200'
# endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/api/'


# response = requests.get(endpoint, json={"q": "hello django"}, params={"abc":12321})
response = requests.post(endpoint, json={'title': 'WD 4TB Gaming Drive Works with Playstation 4 Portable External Hard Drive', 'price': '685', 'sale_price': '91.2', 'my_discount': '22.8'}, params={"abc":12321})

# print(response)
print(response.json())
