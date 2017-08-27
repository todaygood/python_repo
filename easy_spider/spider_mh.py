#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import requests

from lxml import etree

class Tieba_Spider(object):
	
	def __init__(self):
		'''
		初始化构造方法
		'''
		self.tieba_name=raw_input('input url:')
		self.start_page=raw_input('input start page:')
		self.end_page=raw_input('input end page:')

	
tieba_spider=Tieba_Spider()



	
