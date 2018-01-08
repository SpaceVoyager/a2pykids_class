import requests
r = requests.post('http://0.0.0.0:5000', json={"name": "sean", "code_name": "humpy dumpy", "action":"add_or_update"})
print r.status_code
print r.json()
r = requests.post('http://0.0.0.0:5000', json={"name": "daniel", "action":"delete"})
print r.status_code
print r.json()