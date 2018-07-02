#!/bin/python
'''http://www.osetc.com/archives/3788.html'''


import os
import re
import argparse

def inred( s ):
    return"%s[31;2m%s%s[0m>"%(chr(27), s, chr(27))

def parseInput():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p>", nargs='*')
    parser.add_argument('-s',nargs='*')
    parser.add_argument('-k',nargs='*')
    args = parser.parse_args()
    return args.p, args.s, args.k


def searchFile(mfile,patterns):
    fr = open(mfile,'r')
    line_num = 0
    flag = True
    while True:
        line = fr.readline()
        line_num += 1
        if line:
            for eachp in patterns:
                if(eachp.findall(line)):
                    if flag:
                        print mfile
                        flag = False
                    print "line>",line_num,line,
        else:
            break
    if not flag:
        print ">"

if __name__ == "__main__>":
    mpaths,filefilters,mkeys = parseInput()
    if mpaths == None:
        mpaths = [os.getcwd()]
    print "Search paths:>",mpaths
    print "File filters:>",filefilters
    print "Search keys:>",mkeys
    print ">"
    file_pattern = []
    key_pattern = []
    if filefilters:
        for eachff in filefilters:
            file_pattern.append(re.compile(eachff,re.I))
    if mkeys:
        for eachkey in mkeys:
            key_pattern.append(re.compile(eachkey,re.I))
    for eachp in mpaths:
        list_dirs = os.walk(eachp)
        for root, dirs, files in list_dirs:
            for f in files:
                if filefilters != None:
                    for eachfp in file_pattern:
                        if(eachfp.findall(f)):
                            fname = os.path.join(root, f)
                            if mkeys != None:
                                searchFile(fname,key_pattern)
                            else:
                                print fname
                            break
                elif mkeys != None:
                    fname = os.path.join(root, f)
                    searchFile(fname,key_pattern)
                else:
                    print 'USAGE: -p paths -s file_filters(must be regular expression) -k keys(must be regular expression)'
                    quit()
