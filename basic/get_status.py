import libvirt

conn = libvirt.open('xen:///')

for id in conn.listDomainsID():

	dom = conn.lookupByID(id)

	print "Dom %s  State %s" % ( dom.name(), dom.info()[0] )

	dom.suspend()
	print "Dom %s  State %s (after suspend)" % ( dom.name(), dom.info()[0] )

	dom.resume()
	print "Dom %s  State %s (after resume)" % ( dom.name(), dom.info()[0] )

	dom.destroy()
	
	
	
	
	