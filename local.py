import requests as req

response = req.get("127.0.0.1:5000")
print(response.json())