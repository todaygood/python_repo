#!/usr/bin/env python

import requests

baidu_url = "https://www.baidu.com"

response = requests.get(baidu_url)

print(response.content.decode())


