# import requests
import json
from requests import get, post, put

# res = get("https://api.github.com/search/users?q=harish223")

# print(res.status_code)
# print(res.text)

# /* updating title of product with id 1 */
# fetch('https://dummyjson.com/products/1', {
#   method: 'PUT', /* or PATCH */
#   headers: { 'Content-Type': 'application/json' },
#   body: JSON.stringify({
#     title: 'iPhone Galaxy +1'
#   })
# })
# .then(res => res.json())
# .then(console.log);

data = json.dumps({
    "title": 'iPhone Galaxy +1'
})
print(type(data))
res = put("https://dummyjson.com/products/1", data=data)

data1 = res.json()
print(type(data1))