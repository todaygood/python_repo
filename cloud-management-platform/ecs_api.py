#!/usr/bin/python
# -*- coding: utf-8 -*-

from aliyunsdkcore import client
from aliyunsdkcore.profile import region_provider
from aliyunsdkecs.request.v20140526 import CreateInstanceRequest
from aliyunsdkecs.request.v20140526 import StartInstanceRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest
from aliyunsdkecs.request.v20140526 import RebootInstanceRequest
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest

import ConfigParser
import json
import getopt
import sys
import time

def usage():
	print("====================  " + sys.argv[0] + "  usage  ===================")
	print("   -h | --help: print usage")
	print("   -c | --create: create instance")
	print("   -s | --startup: startup instance")
	print("   -x | --stop: stop instance")
	print("   -d | --describe: describe instance")
	print("   -r | --reboot: reboot instance")
	print("   -i | --instance_id: set instance id")
	print("   -f | --forcestop: forcestop, true or false")
	sys.exit(1)

def create_instance(json_params):
	"""create one if instance in ALiCloud.

	:param json_params: params that using to create ecs instance, in json format

	ref: more documnets please see: https://help.aliyun.com/document_detail/25499.html?spm=a2c4g.11174283.6.846.4P8Jkp

	:returns
		A json object will be return. Including Status code and other AliCloud return Values.
		Status code：
			res：0	success
			res：1	failed
		For examle:
		{"res": 1, "message": "The specified ImageId does not exist.", "error_code": "InvalidImageId.NotFound",
		"http_status": 404, "request_id": "F131ED93-4D5C-43DE-BEB8-0FFBA57CBC24"}
		OR:
		{"InstanceId": "i-m5eik2gyllk5b1gvrgn9", "res": 0, "RequestId": "78CE4E5A-260D-4675-A814-AA0B0E2B13BA"}
	"""

	cf = ConfigParser.ConfigParser()
	cf.read("config.ini")
	access_key_id = cf.get("accesskey", "access_key_id")
	access_key_secret = cf.get("accesskey", "access_key_secret")
	region_id = cf.get("region", "region_id")
	clt = client.AcsClient(access_key_id, access_key_secret, region_id)

	# set params
	request = CreateInstanceRequest.CreateInstanceRequest()
	request.set_accept_format('json')

	params = json.loads(json_params)
	# print(type(params), params)
	request.add_query_param('RegionId', params['RegionId'])
	request.add_query_param('ImageId', params['ImageId'])
	request.add_query_param('InstanceType', params['InstanceType'])
	request.add_query_param('SecurityGroupId', params['SecurityGroupId'])
	request.add_query_param('InstanceName', params['InstanceName'])
	request.add_query_param('InternetChargeType', params['InternetChargeType'])
	request.add_query_param('AutoRenew', params['AutoRenew'])
	request.add_query_param('AutoRenewPeriod', params['AutoRenewPeriod'])
	request.add_query_param('InternetMaxBandwidthIn', params['InternetMaxBandwidthIn'])
	request.add_query_param('InternetMaxBandwidthOut', params['InternetMaxBandwidthOut'])
	request.add_query_param('HostName', params['HostName'])
	request.add_query_param('Password', params['Password'])
	request.add_query_param('SystemDisk.Size', params['SystemDisk.Size'])
	request.add_query_param('SystemDisk.Category', params['SystemDisk.Category'])
	request.add_query_param('Description', params['Description'])
	request.add_query_param('VSwitchId', params['VSwitchId'])
	request.add_query_param('IoOptimized', params['IoOptimized'])
	request.add_query_param('InstanceChargeType', params['InstanceChargeType'])
	request.add_query_param('Period', params['Period'])
	request.add_query_param('PeriodUnit', params['PeriodUnit'])

	# send request
	try:
		response = clt.do_action_with_exception(request)
		result = json.loads(response)
		result["res"] = 0
		return json.dumps(result)
	except Exception as err:
		# print(err)
		# print(type(err))
		# print(dir(err))
		result = {"res":1}
		result["error_code"] = err.__getattribute__("error_code")
		result["http_status"] = err.__getattribute__("http_status")
		result["message"] = err.__getattribute__("message")
		result["request_id"] = err.__getattribute__("request_id")
		# print(result)
		return json.dumps(result)

def start_instance(instance_id):
	"""start instance by using instance id.

	:param instance_id: instance id which need to be startup

	:returns
		A json object will be return. Including Status code and other AliCloud return Values.
		Status code：
			res：0	success
			res：1	failed
		For examle:
		{"res": 0, "RequestId": "51620616-BCC3-403D-ADAD-82B1F679436D"}
		OR:
		{"res": 1, "message": "The specified InstanceId does not exist.",
		"error_code": "InvalidInstanceId.NotFound", "http_status": 404,
		"request_id": "88621913-6062-4ADA-AD98-DDDA11025502"}
	"""

	cf = ConfigParser.ConfigParser()
	cf.read("config.ini")
	access_key_id = cf.get("accesskey", "access_key_id")
	access_key_secret = cf.get("accesskey", "access_key_secret")
	region_id = cf.get("region", "region_id")
	clt = client.AcsClient(access_key_id, access_key_secret, region_id)

	# set params
	request = StartInstanceRequest.StartInstanceRequest()
	request.set_accept_format('json')

	request.add_query_param('InstanceId', instance_id)

	# send request
	try:
		response = clt.do_action_with_exception(request)
		result = json.loads(response)
		result["res"] = 0
		print(json.dumps(result))
		return json.dumps(result)
	except Exception as err:
		# print(err)
		# print(dir(err))
		result = {"res":1}
		result["error_code"] = err.__getattribute__("error_code")
		result["http_status"] = err.__getattribute__("http_status")
		result["message"] = err.__getattribute__("message")
		result["request_id"] = err.__getattribute__("request_id")
		return json.dumps(result)

def stop_instance(instance_id, forcestop):
	"""stop instance by using instance id.

	:param instance_id: instance id which need to be stopped
	:param forcestop: force stop instance or not(true or false), default: false

	:return
	A json object will be return. Including Status code and other AliCloud return Values.
		Status code：
			res：0	success
			res：1	failed
		For examle:
		{"res": 0, "RequestId": "5679BF07-8EA4-4B0E-93F2-46D31EBD5A76"}
		OR:
		{"res": 1, "message": "The current status of the resource does not support this operation.",
		"error_code": "IncorrectInstanceStatus", "http_status": 403,
		"request_id": "708E5940-BE18-4487-8310-D7D98E8E6EA6"}
	"""

	cf = ConfigParser.ConfigParser()
	cf.read("config.ini")
	access_key_id = cf.get("accesskey", "access_key_id")
	access_key_secret = cf.get("accesskey", "access_key_secret")
	region_id = cf.get("region", "region_id")
	clt = client.AcsClient(access_key_id, access_key_secret, region_id)

	# set params
	request = StopInstanceRequest.StopInstanceRequest()
	request.set_accept_format('json')

	request.add_query_param('InstanceId', instance_id)
	request.add_query_param('ForceStop', forcestop)

	# send request
	try:
		response = clt.do_action_with_exception(request)
		result = json.loads(response)
		result["res"] = 0
		return json.dumps(result)
	except Exception as err:
		# print(err)
		result = {"res":1}
		result["error_code"] = err.__getattribute__("error_code")
		result["http_status"] = err.__getattribute__("http_status")
		result["message"] = err.__getattribute__("message")
		result["request_id"] = err.__getattribute__("request_id")
		return json.dumps(result)


def reboot_instance(instance_id, forcestop):
	"""reboot instance by using instance id.

	:param instance_id: instance id which need to be reboot
	:param forcestop: force reboot instance or not(true or false), default: false

	:return
		A json object will be return. Including Status code and other AliCloud return Values.
		Status code：
			res：0	success
			res：1	failed
		For examle:
		{"res": 0, "RequestId": "1526C40A-3AE8-4854-B1C7-4249D3385C84"}
		OR:
		{"res": 1, "message": "The current status of the resource does not support this operation.",
		"error_code": "IncorrectInstanceStatus", "http_status": 403,
		"request_id": "726C5926-4F9D-456E-B8E9-36AAA75D50CF"}
	"""

	cf = ConfigParser.ConfigParser()
	cf.read("config.ini")
	access_key_id = cf.get("accesskey", "access_key_id")
	access_key_secret = cf.get("accesskey", "access_key_secret")
	region_id = cf.get("region", "region_id")
	clt = client.AcsClient(access_key_id, access_key_secret, region_id)

	# set params
	request = RebootInstanceRequest.RebootInstanceRequest()
	request.set_accept_format('json')

	request.add_query_param('InstanceId', instance_id)
	request.add_query_param('ForceStop', forcestop)

	# send request
	try:
		response = clt.do_action_with_exception(request)
		result = json.loads(response)
		result["res"] = 0
		return json.dumps(result)
	except Exception as err:
		# print(err)
		# print(type(err))
		# print(dir(err))
		result = {"res":1}
		result["error_code"] = err.__getattribute__("error_code")
		result["http_status"] = err.__getattribute__("http_status")
		result["message"] = err.__getattribute__("message")
		result["request_id"] = err.__getattribute__("request_id")
		return json.dumps(result)


def describe_instances(region_id, instance_id_list):
	"""get information of instance by using instance id.

	:param region_id： region id which the instance location
	:param instance_id_list: list that which you need to describe, max 100 Ids. for example:
		[“i-xxxxxxxxx”, ”i-yyyyyyyyy”, … “i-zzzzzzzzz”]

	:return
		A json object will be return. Including Status code and other AliCloud return Values.
		Status code：
			res：0	success
			res：1	failed
		ps: this func always return {res:0}, if TotalCount = 0 means no hit.

		For examle:
		{"PageSize": 10, "Instances": {"Instance": [{"AutoReleaseTime": "", "RegionId": "cn-qingdao",
		"InstanceTypeFamily": "ecs.xn4", "InternetChargeType": "PayByTraffic",
		"SerialNumber": "900bdeb7-ea06-4e96-bcb6-248b0793e92f",
		"CreationTime": "2018-05-09T06:20Z", "SpotPriceLimit": 0.0,
		"ExpiredTime": "2099-12-31T15:59Z", "IoOptimized": true,
		"Memory": 1024, "OSType": "linux", "StoppedMode": "Not-applicable",
		"VpcAttributes": {"VpcId": "vpc-m5e9zj6o5f91d9ge74dvi", "VSwitchId": "vsw-m5etq9yuy5k9n9j0kgsjm",
		"PrivateIpAddress": {"IpAddress": ["10.0.0.199"]}, "NatIpAddress": ""}, "Status": "Running",
		"Description": "cmp instance description", "InstanceId": "i-m5eik2gyllk5b1gvrgn9",
		"HostName": "cmp-test", "ClusterId": "", "ImageId": "centos_6_09_64_20G_alibase_20170825.vhd",
		"ResourceGroupId": "", "SpotStrategy": "NoSpot", "InstanceNetworkType": "vpc",
		"InstanceType": "ecs.xn4.small",
		"NetworkInterfaces": {"NetworkInterface": [{"MacAddress": "00:16:3e:05:d5:71", "NetworkInterfaceId": "eni-m5e5jnl5beqrtda71zoy", "PrimaryIpAddress": "10.0.0.199"}]},
		"EipAddress": {"InternetChargeType": "", "IpAddress": "", "AllocationId": ""},
		"InnerIpAddress": {"IpAddress": []},
		"GPUAmount": 0, "OperationLocks": {"LockReason": []}, "InstanceChargeType":
		"PostPaid", "SecurityGroupIds": {"SecurityGroupId": ["sg-m5eeaa5819tki221db0o"]},
		"InternetMaxBandwidthOut": 1, "SaleCycle": "", "ZoneId": "cn-qingdao-b",
		"InstanceName": "cmp_test_instance", "Cpu": 1, "PublicIpAddress": {"IpAddress": []},
		"InternetMaxBandwidthIn": 1, "OSName": "CentOS  6.9 64\u4f4d", "VlanId": "",
		"Recyclable": false, "StartTime": "2018-05-09T07:08Z", "GPUSpec": "", "DeviceAvailable": true,
		"DedicatedHostAttribute": {"DedicatedHostName": "", "DedicatedHostId": ""}}]},
		"res": 0, "TotalCount": 1, "PageNumber": 1, "RequestId": "9231A10E-EEB0-41F9-B213-63A018251CA5"}
		OR:
		{"res": 1, "message": "Fail to describe instance info."
	"""
	region_provider.modify_point('Ecs', 'cn-sz-gjjy-d01', 'ecs.sz.cngb.org')
	cf = ConfigParser.ConfigParser()
	cf.read("config.ini")
	access_key_id = cf.get("accesskey", "access_key_id")
	access_key_secret = cf.get("accesskey", "access_key_secret")
	region_id = cf.get("region", "region_id")
	clt = client.AcsClient(access_key_id, access_key_secret, region_id)
	print("region_id is ", region_id)
	# set params
	request = DescribeInstancesRequest.DescribeInstancesRequest()
	request.set_accept_format('json')

	# str2json = {}
	# str2json["instance_id"] = instance_id
	# instance_id_json = json.dumps(str2json)
	print("instance list is ", instance_id_list)
	#sys.exit(1)

	request.add_query_param('RegionId', region_id)
	request.add_query_param('InstanceIds', instance_id_list)

	# send request
	try:
		response = clt.do_action_with_exception(request)
		result = json.loads(response)
		result["res"] = 0
		return json.dumps(result)
	except Exception as err:
		print(err)
		result = {"res":1}
		result["message"] = "Fail to describe instance info."
		return json.dumps(result)


if __name__ == "__main__":
	json_params = '{"RegionId":"cn-qingdao", "ImageId":"centos_6_09_64_20G_libase_20170825.vhd", ' \
				'"InstanceType":"ecs.xn4.small", "SecurityGroupId":"sg-m5eeaa5819tki221db0o", ' \
				'"InstanceName":"cmp_test_instance", "InternetChargeType":"PayByTraffic", ' \
				'"AutoRenew":"True", "AutoRenewPeriod":1,"InternetMaxBandwidthIn":1, ' \
				'"InternetMaxBandwidthOut":1, "HostName":"cmp-test", ' \
				'"Password":"123wqe.bgi.org123$", "SystemDisk.Size":40, ' \
				'"SystemDisk.Category":"cloud_efficiency", "Description":"cmp instance description", ' \
				'"VSwitchId":"vsw-m5etq9yuy5k9n9j0kgsjm", "IoOptimized":"optimized", ' \
				'"InstanceChargeType":"PostPaid", "Period":1, "PeriodUnit":"week"}'

	# set defalut value
	action = ""
	instance_id = ""
	forcestop = "false"

	opts, args = getopt.getopt(sys.argv[1:], "hcsxrdi:f:", ["help", "create",
															  "startup", "stop", "reboot", "describe",
															  "instance_id=", "forcestop="])
	for op, value in opts:
		if op in ("-h", "--help"):
			usage()
		if op in ("-i", "--instance_id"):
			instance_id = value
		if op in ("-f", "--forcestop"):
			forcestop = value
		if op in ("-c", "--create"):
			action = "create_instance"
		if op in ("-s", "--startup"):
			action = "startup_instance"
		if op in ("-x", "--stop"):
			action = "stop_instance"
		if op in ("-r", "--reboot"):
			action = "reboot_instance"
		if op in ("-d", "--describe"):
			action = "describe_instance"

	if action == "create_instance":
		response = create_instance(json_params)
		# successful response
		# response = {"InstanceId":"i-m5eiztnsn7rv676n87w2","RequestId":"4F73820A-1850-41B1-AE91-93A0333488B8"}
		print(response)
		print(type(response))
		# print(type(response))
		# sys.exit(1)
		#response_dict = eval(response)
		#instance_id = response_dict["InstanceId"]
		#print(instance_id)
		# sys.exit(1)
		#time.sleep(30)
		#result = json.loads(describe_instances("cn-qingdao", instance_id))
		#print(result["Instances"]["Instance"][0]["Status"])
		#sys.exit(1)
	if action == "startup_instance" and instance_id:
		print(instance_id, " is now starting...")
		print(start_instance(instance_id))
		# sys.exit(1)
	if action == "startup_instance" and not instance_id:
		print("please set instance id which need to be startup...")
		usage()
	if action == "stop_instance" and instance_id:
		print(instance_id, " is now shutting down...", forcestop)
		print(stop_instance(instance_id, forcestop))
	if action == "stop_instance" and not instance_id:
		print("please set instance id which need to be stoped...")
		sys.exit(1)
	if action == "reboot_instance" and instance_id:
		print(instance_id, "is now rebooting...", forcestop)
		print(reboot_instance(instance_id, forcestop))
	if action == "reboot_instance" and not instance_id:
		print("please set instance id which need to be reboot...")
	if action == "describe_instance" and instance_id:
		print("start getting info of instance: ", instance_id)
		instance_id_list = [instance_id]
		print(describe_instances("cn-qingdao", instance_id_list))
	if action == "":
		print("no actoin, exit...")
		usage()