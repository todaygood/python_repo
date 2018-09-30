class Foo:
	def bar(self):
		from ctypes import string_at
		string_at(0xDEADBEEF) # this code will cause Python to segfault

f = Foo()
f.someattr = 42
f.someotherattr = {'one':1, 'two':2L, 'three':[(), (None,), (None, None)]}
f.bar()




