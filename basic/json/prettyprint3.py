#!/usr/bin/env python 

import json,sys
import pprint

def main():
    if (len(sys.argv)) < 2:  
       print("Usage:%s json_file"% sys.argv[0])
       return -1
   
    with open(sys.argv[1],"r") as infile:
       print("pretty print the json file")
       js = json.load(infile) 
       outfile = open("./nodes3.json","w")
       pprint.pprint(js,outfile)
   
    infile.close()
    outfile.close()


if __name__ == "__main__":
    main()
