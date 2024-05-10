import requests as req

# response = req.get("http://127.0.0.1:5001/api/index/3")
# response = req.delete("http://127.0.0.1:5001/api/index/3")
response = req.post("http://127.0.0.1:5001/api/index/4", {"audi": "a3", "engine_capacity": "2"})
response = req.post("http://127.0.0.1:5001/api/index/5", {"audi": "a4", "engine_capacity": "5.2"})

print(response.json())
