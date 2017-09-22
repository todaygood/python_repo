#!/usr/bin/python -tt 


while True:
	try:
		x=int(raw_input("please enter a number: "))
		break
	except ValueError:
		print "Oops!That was no valid number. Try again..."

