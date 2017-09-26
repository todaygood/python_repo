#!/usr/bin/env python 

import logging 

logging.info("This is a info Message")
logging.critical("This is a critical Message")
logging.error("This is a error Message")

logging.root.setLevel(level=logging.INFO)
logging.info("This is a info Message")

logging.basicConfig(format='%(asctime)s:

