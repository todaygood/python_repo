#!/usr/bin/env python

import urllib2
import json


def curl_keystone():
    url = 'http://10.54.13.246:35357/v2.0/tokens'
    values = {"auth":{"passwordCredentials":{"username":"admin","password":"nt3ns1vuK5OT4ybnZtZlXGXsZECCqYWAgKTvAKF3"},"tenantName":"admin"}}
    params = json.dumps(values)
    print("dump :",params)
    headers = {"Content-type":"application/json","Accept": "application/json"}
    req = urllib2.Request(url, params, headers)
    response = urllib2.urlopen(req)
    data = response.read()
    print("data :",data)

    ddata=json.loads(data)

    print("ddata :",ddata)
    token = ddata['access']['token']['id']
    return token

curl_keystone()
