#!/bin/python

import libvirt

conn = libvirt.open("")

f = open("test.xml")

xml = f.read()

dom_ref=conn_handler.defineXML(xml)

conn_handler.listDefinedDomains()


dom_ref.undefine()

conn_handler.listDefinedDomains()


