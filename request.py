# request.py
import json
import requests

# x ist reponse
x = requests.get('http://127.0.0.1:5000/courses')

# parse x:
# x.json ist liste
y = x.json() 

# print(x.text)
print("Raw response text:", x.text)
print("Parsed JSON content:", json.dumps(y, indent=2))
