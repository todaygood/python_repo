#!/usr/bin/python3

import subprocess 

result = subprocess.run(['ls','-al'],stdout=subprocess.PIPE)

print(result.stdout)


