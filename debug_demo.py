#!/usr/bin/python 

 
_debug = True 


def debug_demo(val): 	
	if _debug:  
		import pdb  
		pdb.set_trace()
	if val < 10: 
		print "less than 10"  
	elif val<20: 
		print "less than 20, but big than 10"  
	else:  
		print "other condition" 

if __name__ == "__main__": 
	debug_demo(4500)