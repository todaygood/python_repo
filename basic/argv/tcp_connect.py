#!/usr/bin/python

import argparse

parser=argparse.ArgumentParser("tcp connect target:")

parser.add_argument("server_ip");

parser.add_argument('-o','--output')

parser.add_argument('-v',dest='verbose',action='store_true')

args = parser.parse_args()


print args.server_ip

