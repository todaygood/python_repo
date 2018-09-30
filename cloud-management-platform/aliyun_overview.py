#!/usr/bin/python
# -*- coding:utf-8 -*-


import ConfigParser
import json
import oss2
from aliyunsdkcore import client
from aliyunsdkslb.request.v20140515 import DescribeLoadBalancersRequest
from aliyunsdknas.request.v20170626 import DescribeFileSystemsRequest
from aliyunsdkvpc.request.v20160428 import DescribeEipAddressesRequest

def get_oss_bucket_info(region_id):
	cf = ConfigParser.ConfigParser()
	cf.read("config.ini")
	access_key_id = cf.get("accesskey", "access_key_id")
	access_key_secret = cf.get("accesskey", "access_key_secret")
	# region_id = cf.get("region", "region_id")

	auth = oss2.Auth(access_key_id, access_key_secret)
	endpoint = "http://oss-" + region_id + ".aliyuncs.com"
	service = oss2.Service(auth, endpoint)
	result = {}
	try:
		result1 = oss2.BucketIterator(service)

		num = 0
		result_list = []
		for x in result1:
			# print(x.name)
			result_list.append(x.name)
			num = num + 1

		result["res"] = 0
		# print(result)
		result["count"] =  num
		# print(result)
		result["object"] = result_list
		return result
	except Exception as err:
		result["res"] = 1
		result["msg"] = str(err)
		return result


def get_eip_info():
	clt = client.AcsClient('<accessKeyId>', '<accessSecret>', 'cn-hangzhou')

	# 设置参数
	request = DescribeEipAddressesRequest.DescribeEipAddressesRequest()
	request.set_accept_format('json')

	request.add_query_param('RegionId', 'cn-shenzhen')

	# 发起请求
	response = clt.do_action(request)

	print response


def get_rds_info():
	pass


def get_slb_info(region_id):
	cf = ConfigParser.ConfigParser()
	cf.read("config.ini")
	access_key_id = cf.get("accesskey", "access_key_id")
	access_key_secret = cf.get("accesskey", "access_key_secret")
	clt = client.AcsClient(access_key_id, access_key_secret, region_id)

	# 设置参数
	request = DescribeLoadBalancersRequest.DescribeLoadBalancersRequest()
	request.set_accept_format('json')

	request.add_query_param('RegionId', region_id)

	# 发起请求
	try:
		response = clt.do_action_with_exception(request)
		result = json.loads(response)
		# print(type(result))
		# print(result["TotalCount"])
		slb_total_count = result["TotalCount"]
		result = {"res": 0}
		result["total_count"] = slb_total_count
		return result
	except Exception as err:
		result = {"res": 1}
		result["msg"] = str(err)
		return result


def get_nas_info():
	cf = ConfigParser.ConfigParser()
	cf.read("config.ini")
	access_key_id = cf.get("accesskey", "access_key_id")
	access_key_secret = cf.get("accesskey", "access_key_secret")
	clt = client.AcsClient(access_key_id, access_key_secret, 'cn-shenzhen')

	# 设置参数
	request = DescribeFileSystemsRequest.DescribeFileSystemsRequest()
	request.set_accept_format('json')

	# 发起请求
	try:
		response = clt.do_action_with_exception(request)
		# print(response)
		result = json.loads(response)
		nas_total_count = result["TotalCount"]
		filesystems = result["FileSystems"]["FileSystem"]
		# print(filesystems)
		rest = {"res" : 0}

		rest["total_count"] = nas_total_count
		total_size = 0
		for x in filesystems:
			total_size = total_size + int(x["MeteredSize"])

		total_size = str(total_size / (1024 * 1024 * 1024 * 1024)) + "TB"
		rest["total_size"] = total_size
		return rest
	except Exception as err:
		print(err)
		rest = {"res" : 1}
		rest["msg"] = str(err)
		return rest


if __name__ == "__main__":
	# print(get_oss_bucket_info("cn-shenzhen"))
	# print(get_slb_info("cn-shenzhen"))
	print(get_nas_info())