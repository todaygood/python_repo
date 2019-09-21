#!/usr/bin/env python
import logging 


logging.basicConfig(level=logging.WARNING,
                    filename='./log.txt',
                    filemode='w',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

logging.info("This is a info Message")
logging.critical("This is a critical Message")
logging.error("This is a error Message")

logging.root.setLevel(level=logging.INFO)
logging.info("This is a info Message")

