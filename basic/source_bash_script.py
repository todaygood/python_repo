#!/usr/bin/env python
'''
Purpose: source a file like bash  in python

https://stackoverflow.com/questions/3503719/emulating-bash-source-in-python

'''


import os,sys
import pprint
import subprocess

def main():
    if len(sys.argv) < 2 :
        print("Usage: ",sys.argv[0],"bash file within envionment")
        return

    cmd='source %s && env'%sys.argv[1]
    #print(cmd)

    command = ['bash', '-c', cmd]
    proc = subprocess.Popen(command, stdout = subprocess.PIPE)

    for line in proc.stdout:
        line = line.rstrip('\n')
        (key, _, value) = line.partition("=")
        os.environ[key] = value

    proc.communicate()

    pprint.pprint(dict(os.environ))



if __name__ == "__main__"  :
    main()



