import requests

headers = {
    'Authorization': 'e4xxxdb-xxxx-11ed-9f86-xxxxd6fdfb3',
    # Already added when you pass json= but not when you pass data=
    # 'Content-Type': 'application/json',
}

json_data = {
    'from': '+1437291xxx6',
    'to': '+1514xxxxxxxx',
    'content': 'Cisco Live!!!',
    'contentType': 'TEXT',
}

response = requests.post('https://api-sandbox.imiconnect.io/v1/sms/messages', headers=headers, json=json_data)

print(response)
