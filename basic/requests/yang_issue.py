#!/usr/bin/env python

import requests

r = requests.get("https://www.baidu.com", allow_redirects=True, verify=False)

print(r.content)


