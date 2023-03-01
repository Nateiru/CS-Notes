#!/usr/bin/env python

import requests
import json
import time
from rich.console import Console

url= ''

known = set()

while True:
  res = request.get(url).json()
  for danmuku in res['data']['room']:
    text = danmuku['text']
    user = danmuku['nickname']
    ts = danmuku['check_info']['ts']

    d = (text, user, ts)

    if d not in known:
      print(f'@{user}: {text}')
