#!/usr/bin/python -tt 

class SchoolMember:
	'''represents any school member '''
	def __init__(self,name,age):
		self.name = name
		self.age = age
		print "Initialized SchoolMember:%s"%(self.name)
	
	def tell(self):
		'''tell details '''
		print 'Name:%s Age:%s' % (self.name,self.age) 

class Teacher(SchoolMember):
	def __init__(self,name,age,salary):
		SchoolMember.__init__(self,name,age)
		self.salary = salary
		print "Initialized Teacher:%s" % (self.name )
	
	def tell(self):
		SchoolMember.tell(self)
		print "salary :%s"% (self.salary)
	
class Student(SchoolMember):
	def __init__(self,name,age,marks):
		SchoolMember.__init__(self,name,age)
		self.marks = marks
		print "Initialized Student:%s" % (self.name)
	
	def tell(self):
		SchoolMember.tell(self)
		print "marks :%s"% (self.marks)

t = Teacher('Mrs.Shrividya',40,30000)
s = Student('Swaroop',22,75)

print 

members = [t,s]

for member in members:
	member.tell()






