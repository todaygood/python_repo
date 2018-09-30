#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import logging.handlers


class Logger:
	"""
	封装logger类
	"""
	def __init__(self, path, clevel = logging.INFO, flevel = logging.DEBUG):
		self.logger = logging.getLogger(path)
		self.logger.setLevel(logging.DEBUG)
		# 设置日志格式
		fmt = logging.Formatter('%(asctime)s - %(filename)s:%(lineno)d - %(name)s - %(message)s')

		# 设置 CMD 日志
		sh = logging.StreamHandler()
		sh.setFormatter(fmt)
		sh.setLevel(clevel)

		# 设置文件日志
		fh = logging.FileHandler(path)
		fh.setFormatter(fmt)
		fh.setLevel(flevel)

		self.logger.addHandler(sh)
		self.logger.addHandler(fh)

	def debug(self, message):
		self.logger.debug(message)

	def info(self, message):
		self.logger.info(message)

	def war(self, message):
		self.logger.warning(message)

	def error(self, message):
		self.logger.warning(message)

	def cri(self, message):
		self.logger.critical(message)
