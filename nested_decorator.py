#!/usr/bin/env python

user,passwd="alex","abc123"

def auth(auth_type):
    print("auth_type:%s in auth"%(auth_type))
    def out_wapper(func):
        print("in out_wapper",func)
        def wapper(*args,**kwargs):
            if auth_type=="local":
                username= input("User:").strip()
                password= input("Password:").strip()
                
                if user == username and passwd == password:
                    print("auth ok")
                    res= func(*args,**kwargs)
                    return res
                else:
                    exit("auth failed")
            elif auth_type == "ldap":
                print("Not Implemented")
                return -1

        return wapper
    return out_wapper



@auth(auth_type="local")
def bbs():
    print("in bbs")


@auth(auth_type="ldap")
def home():
    print("in home")


def index():
    print("in index")



bbs()

home()


