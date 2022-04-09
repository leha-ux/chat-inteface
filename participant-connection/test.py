import requests
import json


url = "http://localhost:8082/reset"
data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
headers = {'Content-type': 'application/json', 'Accept': '*'}

try: 
    while True: 
        message = input("Gebe Message ein:")
        r = requests.post(url, data=json.dumps(message), headers=headers)
        print(r.content)
except KeyboardInterrupt:
    pass