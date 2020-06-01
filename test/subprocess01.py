import subprocess

# s = subprocess.getoutput('ipconfig')
# print(s)
# print(len(s))

ip = '192.168.56.1'

import requests,json
requests.post('http://127.0.0.1:8000/asset/',data=json.dumps(ip))