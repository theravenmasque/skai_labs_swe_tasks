import requests

response = requests.get("https://65ca20363b05d29307dfbfef.mockapi.io/api/v1/sellers")

sellerId= response.json()[0]["sellerId"]

print(sellerId)