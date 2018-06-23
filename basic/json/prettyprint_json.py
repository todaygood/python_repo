#!/usr/bin/env python 

import json,sys

def main():
    print("begin")
    if (len(sys.argv)) < 2:  
       print("Usage:%s json_file"% sys.argv[0])
       return -1
   
    with open(sys.argv[1],"r") as infile:
       print("pretty print the json file")
       js = json.load(infile) 
       outfile = open("./nodes2.json","w")
       json.dump(js,outfile,sort_keys=True,indent=4,separators=(',', ': '))
   
    infile.close()
    outfile.close()


if __name__ == "__main__":
    main()
