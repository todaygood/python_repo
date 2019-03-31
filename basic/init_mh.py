#!/usr/bin/python -tt 

class Person:
	def __init__(self,name):
		self.name = name

	def say(self):
		print "how are you? My name is",self.name


p = Person("hujun")

print p.name

p.say()


