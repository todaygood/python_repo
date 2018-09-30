#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aliyunsdkcore import client
from aliyunsdkecs.request.v20140526 import DescribeInstanceMonitorDataRequest
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkvpc.request.v20160428 import DescribeEipAddressesRequest
from aliyunsdkvpc.request.v20160428 import DescribeEipMonitorDataRequest
# from aliyunsdkcore.profile import region_provider
# region_provider.modify_point('ecs', '<regionId>', 'ecs.<regionId>.aliyuncs.com')

from time import gmtime, strftime, time, strptime, mktime
import datetime
import ConfigParser
import json
import influxdb
import logging
import logger
import pytz


def utc_to_local(utc_ts, local_format='%Y-%m-%dT%H:%M:%SZ'):
	"""convert utc time to local time
	:param utc_ts: utc time, like: 2015-07-31T15:55:00Z
	:param local_format:  local time format
	:return: local time with local_format
	"""
	utc_format = "%Y-%m-%dT%H:%M:%SZ"
	utc_ts = strptime(utc_ts, utc_format)
	local_tz = pytz.timezone('Asia/Chongqing')
	time_str = strftime(utc_format, utc_ts)
	dt = datetime.datetime.strptime(time_str, utc_format)
	utc_dt = pytz.utc.localize(dt, is_dst=None)
	local_dt = utc_dt.astimezone(local_tz)
	return local_dt.strftime(local_format)


def local_to_utc(local_ts, utc_format='%Y-%m-%dT%H:%M:%SZ'):
	"""convert local time to utc time
	:param local_ts: local time, like: 2015-07-31T15:55:00Z
	:param utc_format:  utc time format
	:return: utc time with utc_format
	"""
	local_format = "%Y-%m-%dT%H:%M:%SZ"
	local_ts = strptime(local_ts, local_format)
	local_tz = pytz.timezone('Asia/Chongqing')
	time_str = strftime(local_format, local_ts)
	dt = datetime.datetime.strptime(time_str, local_format)
	local_dt = local_tz.localize(dt, is_dst=None)
	utc_dt = local_dt.astimezone(pytz.utc)
	return utc_dt.strftime(utc_format)


class InfluxDB:
	def __init__(self):
		self.user = 'aliuser'
		self.password = 'alipwd'
		self.host = '10.225.10.27'
		self.port = 8080
		self.dbname = 'aliserver'

	def __get_connect(self):
		self.client = influxdb.InfluxDBClient(self.host, self.port, self.user, self.password, self.dbname)
		return self.client

	def exec_query(self, sql):
		client = self.__get_connect()

		# sql = 'show databases'
		re_list = client.query(sql)
		log_monitor.debug(re_list)
		return re_list

	def exec_write_points(self, json_body):
		client = self.__get_connect()
		result = client.write_points(json_body)
		return result


def load_data(*params):
	data = params
	log_monitor.debug(data)
	log_monitor.debug(type(data))
	(ip, instance_id, IntranetBandwidth, IntranetTX, time_stamp, \
	BPSWrite, IOPSRead, IOPSWrite, IntranetRX, InternetTX, BPSRead, \
	InternetBandwidth, CPU, InternetRX) = data
	ip = ip[0]

	if IntranetBandwidth is None:
		IntranetBandwidth = 0
	if IntranetTX is None:
		IntranetTX = 0
	if IntranetRX is None:
		IntranetRX = 0
	if InternetBandwidth is None:
		InternetBandwidth = 0
	if InternetRX is None:
		InternetRX = 0
	if InternetTX is None:
		InternetTX = 0
	"""
	IntranetTX/IntranetRX: 特定时间内实例发送/接收的内网流量，单位：kbits，这里转化为发送或接收数据的带宽，单位为bits/s, 
	特定时间指DescribeInstanceMonitorDataRequest接口中的Period参数，默认为60s
	IntranetBandwidth：实例的内网带宽，单位时间内的网络流量，单位：kbits/s
	即：IntranetBandwidth = IntranetRX + IntranetTX
	"""
	json_body = [
		{
			"measurement": "ali_usage",
			"tags": {
				"ip": ip,
				"IntranetBandwidth": int(IntranetBandwidth) * 1000,
				"IntranetTX": (int(IntranetTX) * 1000)/60,
				"IntranetRX": (int(IntranetRX) * 1000)/60,
				"InternetTX": (int(InternetTX) * 1000)/60,
				"InternetRX": (int(InternetRX) * 1000)/60,
				"InternetBandwidth": int(InternetBandwidth) * 1000,
				"BPSWrite": BPSWrite,
				"BPSRead": BPSRead,
				"IOPSRead": IOPSRead,
				"IOPSWrite": IOPSWrite
			},
			"time": time_stamp,
			"fields": {
				"instance_id": instance_id,
				"CPU": CPU,
				"intranetbandwidth": int(IntranetBandwidth) * 1000,
				"intranettx": (int(IntranetTX) * 1000)/60,
				"intranetrx": (int(IntranetRX) * 1000)/60,
				"internettx": (int(InternetTX) * 1000)/60,
				"internetrx": (int(InternetRX) * 1000)/60,
				"internetbandwidth": int(InternetBandwidth) * 1000,
				"bpswrite": BPSWrite,
				"bpsread": BPSRead,
				"iopsread": IOPSRead,
				"iopswrite": IOPSWrite
			}
		}
	]
	log_monitor.debug(json_body)
	db = InfluxDB()

	log_monitor.info("Write points: {0}".format(json_body))
	result = db.exec_write_points(json_body)

	if result:
		message = " load succ!"
		log_monitor.info("res is " + str(result) + message)
		res = 0
		return (res, message, json_body)
	else:
		message = " load failed!"
		log_monitor.info("res is " + str(result) + message)
		res = 1
		return (res, message, json_body)


def load_data_eip(*params):
	data = params
	log_monitor.debug(data)
	log_monitor.debug(type(data))
	"""
	param参数：
	instance_id, ip, eip_id, eip, time_stamp, eipflow, eiptx, eippackets, eiprx, eipbandwidth
	"""
	(instance_id, ip, eip_id, eip, time_stamp, eipflow, eiptx, eippackets, eiprx, eipbandwidth) = data
	# ip = ip[0]
	"""
	EipRX	Integer	指定时间内，EIP接收到的数据流量，单位为bytes, 此处转化为bytes/s
	EipTX	Integer	指定时间内，EIP发送的数据流量，单位为bytes, 此处转换为bytes/s
	EipFlow	Integer	指定时间内，EIP接收和发送的总流量，单位为bytes。
	EipBandwidth	Integer	EIP接收和发送流量的总速率，单位为bytes/s。
	EipPackets	Integer	指定时间内，EIP接受和发送的报文总数。
	TimeStamp String	监控数据的时间点，以ISO8601标准表示的UTC+8时间。
	指定时间默认为60s
	"""
	json_body = [
		{
			"measurement": "ali_usage",
			"tags": {
				"ip": ip,
				"eip": eip,
				"eipflow": eipflow,
				"eiptx": int(eiptx)/60,
				"eippackets": eippackets,
				"eiprx": int(eiprx)/60,
				"eipbandwidth": eipbandwidth,
			},
			"time": time_stamp,
			"fields": {
				"instance_id": instance_id,
				"eip_flow": eipflow,
				"eip_tx": int(eiptx) / 60,
				"eip_packets": eippackets,
				"eip_rx": int(eiprx) / 60,
				"eip_bandwidth": eipbandwidth,
			}
		}
	]
	log_monitor.debug(json_body)
	db = InfluxDB()

	log_monitor.info("Write points: {0}".format(json_body))
	result = db.exec_write_points(json_body)

	if result:
		message = " load succ!"
		log_monitor.info("res is " + str(result) + message)
		res = 0
		return (res, message, json_body)
	else:
		message = " load failed!"
		log_monitor.info("res is " + str(result) + message)
		res = 1
		return (res, message, json_body)


def get_instance_list(region_id):
	cf = ConfigParser.ConfigParser()
	cf.read("config.ini")
	access_key_id = cf.get("accesskey", "access_key_id")
	access_key_secret = cf.get("accesskey", "access_key_secret")
	region_id = region_id

	clt = client.AcsClient(access_key_id, access_key_secret, region_id)

	request = DescribeInstancesRequest.DescribeInstancesRequest()
	request.set_accept_format('json')

	request.add_query_param('RegionId', region_id)
	request.add_query_param('PageSize', 100)

	try:
		response = clt.do_action_with_exception(request)
		result = json.loads(response)
		total_count = result["TotalCount"]
		page_num = (total_count / 100) + 1
		log_monitor.debug("Total Instance is, " + str(total_count))
		instance_list_all = {}
		for page in (1, page_num):
			request.add_query_param('PageNumber', page)
			response = clt.do_action_with_exception(request)
			instance_list = json.loads(response)["Instances"]["Instance"]
			log_monitor.debug(type(instance_list))

			a = 1
			for instance in instance_list:
				log_monitor.debug(a)
				instance_id = instance["InstanceId"]
				InstanceNetworkType = instance["InstanceNetworkType"]
				if InstanceNetworkType in "classic":
					ip = instance["InnerIpAddress"].get("IpAddress")
				else:
					vpc_ip = instance["VpcAttributes"]["PrivateIpAddress"]["IpAddress"]
					primary_ip = instance["NetworkInterfaces"]["NetworkInterface"][0].get("PrimaryIpAddress")
					if vpc_ip:
						ip = vpc_ip
					elif primary_ip:
						ip = primary_ip
				instance_list_all[instance_id] = ip
				a = a+1
		return instance_list_all

	except Exception as err:
		log_monitor.error(err)
		result_ip = {"res": 1}
		result_ip["ip"] = "no_ip"
		result_ip["msg"] = err
		return result_ip


def get_instance_monitor_data(instance_id, ip, start_time_utc, end_time_utc):
	cf = ConfigParser.ConfigParser()
	cf.read("config.ini")
	access_key_id = cf.get("accesskey", "access_key_id")
	access_key_secret = cf.get("accesskey", "access_key_secret")
	region_id = cf.get("region", "region_id")

	clt = client.AcsClient(access_key_id, access_key_secret, region_id)
	instance_id = instance_id
	ip = ip

	# 设置参数
	request = DescribeInstanceMonitorDataRequest.DescribeInstanceMonitorDataRequest()
	request.set_accept_format('json')

	request.add_query_param('InstanceId', instance_id)
	request.add_query_param('EndTime', end_time_utc)
	request.add_query_param('StartTime', start_time_utc)


	# 发起请求
	list_data = []
	try:
		response = clt.do_action_with_exception(request)
		result = json.loads(response)["MonitorData"]["InstanceMonitorData"]

		for x in result:
			IntranetBandwidth = x.get("IntranetBandwidth")
			IntranetTX = x.get("IntranetTX")
			TimeStamp = x.get("TimeStamp")
			time_stamp_local = utc_to_local(TimeStamp)
			log_monitor.debug("utc time is " + str(TimeStamp))
			log_monitor.debug("local time is " + str(time_stamp_local))
			time_stamp = int(round(mktime(strptime(time_stamp_local, "%Y-%m-%dT%H:%M:%SZ")))) * 1000 * 1000 * 1000
			BPSWrite = x.get("BPSWrite")
			IOPSWrite = x.get("IOPSWrite")
			IOPSRead = x.get("IOPSRead")
			IntranetRX = x.get("IntranetRX")
			InternetTX = x.get("InternetTX")
			BPSRead = x.get("BPSRead")
			InternetBandwidth = x.get("InternetBandwidth")
			CPU = x.get("CPU")
			InternetRX = x.get("InternetRX")
			list_tmp = (ip, instance_id, IntranetBandwidth, IntranetTX, time_stamp,\
			   BPSWrite, IOPSRead, IOPSWrite, IntranetRX, InternetTX, BPSRead,\
			   InternetBandwidth, CPU, InternetRX)

			list_data.append(list_tmp)
		return list_data
	except Exception as err:
		log_monitor.error(err)
		list_data = {"res": 1}
		list_data["msg"] = err
		return list_data


def get_eip_monitor_data(instance_id, ip, eip_id, eip, start_time_utc, end_time_utc):
	cf = ConfigParser.ConfigParser()
	cf.read("config.ini")
	access_key_id = cf.get("accesskey", "access_key_id")
	access_key_secret = cf.get("accesskey", "access_key_secret")
	region_id = cf.get("region", "region_id")

	clt = client.AcsClient(access_key_id, access_key_secret, region_id)

	# 设置参数
	request = DescribeEipMonitorDataRequest.DescribeEipMonitorDataRequest()
	request.set_accept_format('json')
	request.add_query_param('StartTime', start_time_utc)
	request.add_query_param('EndTime', end_time_utc)
	request.add_query_param('AllocationId', eip_id)

	# 发起请求
	try:
		response = clt.do_action_with_exception(request)
		result = json.loads(response)["EipMonitorDatas"]["EipMonitorData"]
		ip = ip[0]
		eip_data = []
		for x in result:
			utc_time = x.get("TimeStamp")
			local_time = utc_to_local(utc_time)
			time_stamp = int(round(mktime(strptime(local_time, "%Y-%m-%dT%H:%M:%SZ")))) * 1000 * 1000 * 1000
			eipflow = x.get("EipFlow")
			eiptx = x.get("EipTX")
			eippackets = x.get("EipPackets")
			eiprx = x.get("EipRX")
			eipbandwidth = x.get("EipBandwidth")
			eip_data_tmp = (instance_id, ip, eip_id, eip, time_stamp, eipflow, eiptx, eippackets, eiprx, eipbandwidth)
			eip_data.append(eip_data_tmp)
		return eip_data
	except Exception as err:
		log_monitor.error(err)
		result_err = {"res": 1}
		result_err["msg"] = err
		return result_err


def get_eip_info(instance_list):
	if instance_list.has_key("res"):
		log_monitor.error("get eip info failed...")
		exit(1)

	cf = ConfigParser.ConfigParser()
	cf.read("config.ini")
	access_key_id = cf.get("accesskey", "access_key_id")
	access_key_secret = cf.get("accesskey", "access_key_secret")
	region_id = cf.get("region", "region_id")

	clt = client.AcsClient(access_key_id, access_key_secret, region_id)

	# 设置参数
	request = DescribeEipAddressesRequest.DescribeEipAddressesRequest()
	request.set_accept_format('json')

	request.add_query_param('RegionId', 'cn-shenzhen')
	request.add_query_param('AssociatedInstanceType', 'EcsInstance')

	instance_list_with_eip=[]
	try:
		for (k, v) in instance_list.items():
			request.add_query_param('AssociatedInstanceId', k)

			# 发起请求
			response = clt.do_action_with_exception(request)
			result = json.loads(response)["EipAddresses"].get("EipAddress")
			# print(result)
			# print(type(result))
			if result:
				result = result[0]
				eip_id = result.get("AllocationId")
				eip = result.get("IpAddress")
				bandwidth = result.get("Bandwidth")
				ins_tmp = (k, v, eip_id, eip, bandwidth)
				# log_monitor.info(ins_tmp)
				instance_list_with_eip.append(ins_tmp)
			else:
				ins_tmp = (k, v)
				instance_list_with_eip.append(ins_tmp)
		return instance_list_with_eip
	except Exception as err:
		log_monitor.error(err)
		result_err = {"res": 1}
		result_err["msg"] = err
		return result_err


def main():
	start_time_utc = strftime("%Y-%m-%dT%H:%M:%SZ", gmtime(time() - 300))
	end_time_utc = strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())
	log_monitor.info(start_time_utc + " and " + end_time_utc)
	re_list = get_eip_info(get_instance_list("cn-shenzhen"))
	if isinstance(re_list, dict):
		log_monitor.error("get instance with eip failed...")
		exit(1)
	log_monitor.info("Total Instances is, " + str(len(re_list)))

	"""
	re_list 是一个列表，列表元素是元组，如下所示：
	(u'i-944q67sly', [u'192.168.31.44'], u'eip-94arq499t', u'112.74.189.247', u'1')或
	(u'i-wz9cjazswriglffngt8s', [u'192.168.29.237'])
	"""
	count = 1
	for x in re_list:
		# print(count)
		instance_id = x[0]
		ip = x[1]
		res_list = get_instance_monitor_data(x[0], x[1], start_time_utc, end_time_utc)
		log_monitor.debug(type(res_list))
		if isinstance(res_list, dict):
			log_monitor.error("get monitor data failed...")
			exit(1)
		for res in res_list:
			load_data(*res)
			log_monitor.info("instance data, " + str(res))
		if len(x) > 2:
			eip_id = x[2]
			eip = x[3]
			res_list_eip = get_eip_monitor_data(instance_id, ip, eip_id, eip, start_time_utc, end_time_utc)
			if isinstance(res_list_eip, dict):
				log_monitor.error("get eip monitor data failed...")
				exit(1)
			for x in res_list_eip:
				load_data_eip(*x)
				log_monitor.info("eip data is, " + str(x))
		count = count + 1


if __name__ == "__main__":
	log_monitor = logger.Logger("ali_monitor.log", logging.INFO, logging.ERROR)
	main()
