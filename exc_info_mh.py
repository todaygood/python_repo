#!/usr/bin/env python

import sys

try:
    x=1/0
except Exception:
    print(sys.exc_info())
    


