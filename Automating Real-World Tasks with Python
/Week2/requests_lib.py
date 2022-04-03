import requests

response = requests.get('https://www.google.com')

print("Was successful request:", response.ok)
print("Status code of response:", response.status_code)

response.raise_for_status()

p = {"search": "grey kitten", "max_results": 15}
response = requests.get("https://example.com/path/to/api", params=p)
response.request.url  # 'https://example.com/path/to/api?search=grey+kitten&max_results=15'

p = {"description": "white kitten", "name": "Snowball", "age_months": 6}
response = requests.post("https://example.com/path/to/api", data=p)

response = requests.post("https://example.com/path/to/api", json=p)
response.request.url
# 'https://example.com/path/to/api'
response.request.body
# b'{"description": "white kitten", "name": "Snowball", "age_months": 6}'
