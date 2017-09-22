#!/usr/bin/python

import argparse
import socket




parser = argparse.ArgumentParser(description='tcp connect target.')

parser.add_argument('ipaddr',help='server ip addr',default="192.168.5.51")
parser.add_argument('port',help='server\'s port',default=5678,type=int)


args=parser.parse_args()
print args.ipaddr,args.port


address=(args.ipaddr,args.port)
sk = socket.socket()
sk.connect(address)


sk.send("hello,world")

data = sk.recv(512)
print "received is:",data


sk.close()



