import requests
import json

address = "erd10tjn6q88yrfshh4qfkwhdlpgfz8cejmtc7lughmujgeftvqlkt7s06zmlc"
response = requests.get(f"https://gateway.elrond.com/address/{address}/keys").json()

print()
print(json.dumps(response, indent=4))
print()


