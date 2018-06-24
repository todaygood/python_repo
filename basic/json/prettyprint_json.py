#!/usr/bin/env python 

import json,sys

def main():
   if (len(sys.argv)) < 2:
       print("Usage:%s json_file"% sys.argv[0])
       return -1
   
   with open(sys,argv[1],"r") as infile:
       json = json.loads(infile) 
       json.dumps(json,sort_keys=True,indent=4,s
   


if "__line__" == "__main__":
    main()
