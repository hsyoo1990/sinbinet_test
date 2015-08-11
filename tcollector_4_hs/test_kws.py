# -*- coding: utf-8 -*-
# test.py

import time
import requests
import json

url = "http://127.19.0.13:4242/api/put"

data = {
    "metric": "hs.test",
    "timestamp": time.time(),
    "value": 30,
    "tags": {
       "host": "mypc",
       "name": "Sinbinet"
    }
}

ret = requests.post(url, data=json.dumps(data))

print ret.text
