#!/usr/bin/pytohn
# -*- coding: utf-8 -*-
#
# Author: tianjing <tianjing@genomics.cn>
#
# Description: transit base ehr information from EHR MSSQL database to CNGB MySQL database
#
# DataBase schema：
# ————————————————————————————————————————————————————————————————————————————————————-----------------------------------------
# | code | name_zh | name | email | o2code | o2description | o3code | o3description | o4code | 04description | phone | status |
# ————————————————————————————————————————————————————————————————————————————————————-----------------------------------------

import pymssql
import MySQLdb
import ConfigParser
import sys
import getopt
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


def usage():
	print("========= " + sys.argv[0] + " usage =========")
	print("     -h | --help:  print usage")
	print("     -t | --transit： transit ehr data")
	print("     -s (user1, user2...)| --search(user1,user2...): search user information")
	sys.exit(0)


class MSSQL:
	"""

	"""
	def __init__(self, host, user, pwd, db, charset):
		self.host = host
		self.user = user
		self.pwd = pwd
		self.db = db
		self.charset = charset

	def __get_connect(self):
		"""

		:return:
		"""
		if not self.db:
			raise (NameError, " Do not set db information...")
		self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset=self.charset)
		cursor = self.conn.cursor()
		if not cursor:
			raise (NameError, "fail to connect database")
		else:
			return cursor

	def exec_query(self, sql):
		"""

		:param sql:
		:return:
		"""
		cursor = self.__get_connect()
		cursor.execute(sql)
		reList = cursor.fetchall()
		self.conn.close()
		return reList

	def exec_no_query(self,sql):
		"""

		:param sql:
		:return:
		"""
		cursor = self.__get_connect()
		cursor.execute(sql)
		self.conn.commit()
		self.conn.close()


class MYSQL:
	"""

	"""
	def __init__(self, host, user, pwd, db, charset):
		self.host = host
		self.user = user
		self.pwd = pwd
		self.db = db
		self.charset = charset

	def __get_connect(self):
		if not self.db:
			raise (NameError, "Do not set db information")
		self.conn = MySQLdb.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset=self.charset)
		cursor = self.conn.cursor()
		if not cursor:
			raise (NameError, "fail to connect db")
		else:
			return cursor

	def exec_query(self, sql):
		cursor = self.__get_connect()
		cursor.execute(sql)
		reList = cursor.fetchall()
		self.conn.close()
		return reList

	def exec_no_query(self, sql, *params):
		cursor = self.__get_connect()
		cursor.execute(sql, params)
		self.conn.commit()
		self.conn.close()

def transit_ehr_data():
	"""
	将192.168.225.198的数据库中同步EHR的人员信息到本地
	:return:
	"""
	cf = ConfigParser.ConfigParser()
	cf.read("config_db.ini")

	MSHOST = cf.get("MSSQL", "host")
	MSUSER = cf.get("MSSQL", "user")
	MSPWD = cf.get("MSSQL", "pwd")
	MSDB = cf.get("MSSQL", "db")
	MSCHARSET = cf.get("MSSQL", "charset")

	MYHOST = cf.get("MYSQL", "host")
	MYUSER = cf.get("MYSQL", "user")
	MYPWD = cf.get("MYSQL", "pwd")
	MYDB = cf.get("MYSQL", "db")
	MYCHARSET = cf.get("MYSQL", "charset")

	ms = MSSQL(host=MSHOST, user=MSUSER, pwd=MSPWD, db=MSDB, charset=MSCHARSET)
	my = MYSQL(host=MYHOST, user=MYUSER, pwd=MYPWD, db=MYDB, charset=MYCHARSET)

	# delete old data from base_user_info table
	mysql_sql_del = 'TRUNCATE TABLE ehr_base_user_info.base_user_info'
	try:
		my.exec_no_query(mysql_sql_del)
		log_transit.info("old base_ehr_info has been delete")
	except Exception as err:
		log_transit.error(err)

	# sql that insert new data to base_user_info table
	mysql_sql_insert = 'insert into ehr_base_user_info.base_user_info ' \
					   'values(%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s)'

	# select all user information from ehr database
	try:
		reList = ms.exec_query("SELECT code, name, email, phone, o2code,o2description,"
							   "o3code,o3description, o4code,o4description, employeeClass_zh_CN "
							   "FROM [EhrTransitData].[dbo].[EHR_BaseUserInfo]")
		log_transit.info("collect ehr data from 192.168.225.198")
	except Exception as err:
		print(err)
		log_transit.error(err)

	# insert in to mysql database
	try:
		for (code, name_zh, email, phone, o2code, o2description, o3code, o3description, o4code, o4description, status) in reList:
			if email.find('@') != -1:
				(name, domain) = (email.split('@'))
				# print(name)
			else:
				name = email
				# print(name)

			email = name + "@genomics.cn"
			print(name_zh, name, email, o2code, o2description, o3code, o3description, o4code, o4description)

			my.exec_no_query(mysql_sql_insert, code, name_zh, name, email, o2code, o2description, o3code, o3description, o4code, o4description, status, phone)
		log_transit.info("my ehr data has been update")
	except Exception as err:
		log_transit.error(err)


def search_user(*userList):
	"""

	:param userList:
	:return:
	"""
	cf = ConfigParser.ConfigParser()
	cf.read("config_db.ini")

	MYHOST = cf.get("MYSQL", "host")
	MYUSER = cf.get("MYSQL", "user")
	MYPWD = cf.get("MYSQL", "pwd")
	MYDB = cf.get("MYSQL", "db")
	MYCHARSET = cf.get("MYSQL", "charset")

	my = MYSQL(host=MYHOST, user=MYUSER, pwd=MYPWD, db=MYDB, charset=MYCHARSET)

	# print(type(userList))

	# tuple to str
	userList = ''.join(userList)

	# split string
	userList = userList.split(",")

	# string to list
	userList = list(userList)
	# print(userList)
	for user in userList:
		# print(user)
		user = user + "@genomics.cn"
		sql = "select * from ehr_base_user_info.base_user_info where email=" + "\"" + user + "\""

		result = my.exec_query(sql)
		for username, o2, o2d, o3, o3d, o4, o4d in result:
			res = (username, o2d, o3d, o4d)
			res = str(res).replace('u\'', '\'')
			print res.decode("unicode-escape")


if __name__ == '__main__':
	# transit_ehr_data()
	# search_user("tianjing", "lulh", "caozhengyi")
	log_transit = Logger("ehr_transit_log", logging.DEBUG, logging.INFO)
	# log_transit.debug("this is a debug message")
	# log_transit.info("this is a info message")
	# log_transit.war("this is a warnning message")
	# log_transit.error("this is a error message")
	# log_transit.cri("this is a cri message")
	# exit(1)

	opts, args = getopt.getopt(sys.argv[1:], "hts:", ["help", "transit",
															"search="])
	for op, value in opts:
		if op in ("-h", "--help"):
			usage()
		if op in ("-t", "--transit"):
			transit_ehr_data()
			exit(0)
		if op in ("-s", "--search"):
			userList = value
			search_user(userList)
			exit(0)

