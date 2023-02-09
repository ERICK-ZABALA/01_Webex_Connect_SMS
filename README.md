# Webex_Connect_SMS

## Introduction

In this lab we are going to send a simple mesagge via Python with Cisco Webex Connect. That is really simple and easy, I hope that enjoy :).

## Steps

# 1. Create an account Webex Connect.

    - You need to create an account using a corporative mail in order to use you Webex Connect by one year FREE!!!.

![image](https://user-images.githubusercontent.com/38144008/217719017-2a2378dc-2d73-41cb-9db6-d5bb9e509673.png)
 
![image](https://user-images.githubusercontent.com/38144008/217719131-d4024ccf-7fee-4d7d-924a-eca4224b7e08.png)
     
# 2. Copy your Service Key , that is really important when you want to send your sms via Python.

![image](https://user-images.githubusercontent.com/38144008/217719804-6774a52e-439e-4075-bd8d-c8acf492d4f2.png)

# 3. That is my code in Python as example in order to test in your account.

Code: 

import requests

headers = {
    'Authorization': 'e4axxxxx-a2a6-xxxd-9fxx-xxxx',
    # Already added when you pass json= but not when you pass data=
    # 'Content-Type': 'application/json',
}

json_data = {
    'from': '+143729xxxxx',
    'to': '+15144xxxx',
    'content': 'Cisco Live!!!',
    'contentType': 'TEXT',
}

response = requests.post('https://api-sandbox.imiconnect.io/v1/sms/messages', headers=headers, json=json_data)

print(response)

![image](https://user-images.githubusercontent.com/38144008/217720492-fa88752a-33c1-44ba-ae69-d8e5f0fb9307.png)

