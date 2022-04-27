#!/usr/bin/env python3
import json
import requests

AUTH_USERNAME = "christian"
AUTH_TOKEN = "d776f629f04cf5b777c418fe972af3150f779e6fd92cc7a7dfbd4f7f12aa538e"

username = 'christian'

req = requests.get(
    f"http://192.168.10.80/api/v1/ssh_keys/authorized_keys/{username}",
    headers={"Auth-Username": AUTH_USERNAME, "Auth-Token": AUTH_TOKEN}
)
data = json.loads(req.content)
if req.status_code == 200:
    if 'keys' in data:
        print('\n'.join(data['keys']))
        exit(0)
