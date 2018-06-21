#!/usr/bin/env python 
from UserDict import UserDict


class Leaf:
    pass


class FileInfo(UserDict):
    "Store file Metadata"
    def __init__(self,filename=None):
        UserDict.__init__(self)
        self['name']=filename

f=FileInfo()

print(f.__doc__)



