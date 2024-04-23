import json

with open("tes.json") as file_json:
    data = json.loads(file_json.read())
    
print(json.dumps(data, indent=1, sort_keys=False))
