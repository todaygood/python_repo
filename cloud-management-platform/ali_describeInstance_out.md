## 需要特殊处理的例子：


* 判段实例状态

[实例状态表](https://help.aliyun.com/document_detail/25687.html?spm=a2c4g.11186623.2.1.bBlUxz)：

| instance status | 说明 |
| ---- | ---- | 
| Pending |  在控制台或者使用接口 RunInstances 创建实例后，实例的默认状态|
| Starting |在控制台或者使用接口 StartInstance 开启实例后，实例的瞬时状态 |
| Running |实例的稳定运行状态。这是实例的正常状态，实例拥有者此时可以运行、管理、或者调整实例上运行的业务或者应用| 
| Stopping |在控制台或者使用接口 StopInstance 停止关机实例后，实例的瞬时状态 |
| Stopped |ECS 实例完全停止关机的状态 | 

> 1. 用过describeinstance接口的Instances.instance.status 判断实例状态，如果是Stopped状态，则
> 1. 通过describeinstance接口的Instances.instance.ExpiredTime 判断实例是否已到期，以及
> 2. 通过describeinstance接口的Instances.instance.[OperationLocks.LockReason](https://help.aliyun.com/document_detail/25632.html?spm=a2c4g.11186623.2.7.iE8QyO)查询实例被锁定的原因
>  * financial  因欠费被锁定
>  * security 因安全原因被锁定


* 实例内网IP地址
    * VPC类型：通过vpcAttributes获取，不要通过NetworkInterfaces.PrimaryIpAddress获取，有些instance没有PrimaryIpAddress。
NetworkInterfaces显示的是弹性网卡的信息，NetworkInterfaces.PrimaryIpAddress是[弹性网卡主私有IP地址](https://help.aliyun.com/document_detail/58510.html?spm=a2c4g.11186623.2.8.y2aM2S)
    *  经典网络类型：通过InnerIpAddress.IpAddress 获取

```
if InstanceNetworkType in "classic":
	ip = instance["InnerIpAddress"].get("IpAddress")
else:
	vpc_ip = instance["VpcAttributes"]["PrivateIpAddress"]["IpAddress"]
	primary_ip = instance["NetworkInterfaces"]["NetworkInterface"][0].get("PrimaryIpAddress")
	if vpc_ip:
		ip = vpc_ip
	elif primary_ip:
		ip = primary_ip

"InnerIpAddress":{
		"IpAddress":[  //经典网络的内网IP

		]
	},

"NetworkInterfaces":{
		"NetworkInterface":[
			{
				"MacAddress":"00:16:3e:08:52:0c",
				"PrimaryIpAddress":"192.168.29.227", //IP地址，多个显示在同一列，只显示ip，有些实例不显示IP地址
				"NetworkInterfaceId":"eni-wz9fjsv2rrwe1rpsta0b"
			}
		]
	},

"VpcAttributes":{
		"NatIpAddress":"",
		"PrivateIpAddress":{
			"IpAddress":[
				"192.168.29.227"  //内网IP显示这个
			]
		},
		"VSwitchId":"vsw-wz982f1w68a6agljyi12h",
		"VpcId":"vpc-94g45i4gf"
	},

```




## Describeinstance接口输出结果示例

### 公有云输出结果示例：
```
{
	"InnerIpAddress":{
		"IpAddress":[  //经典网络的内网IP，跟NetworkInterface只会存在一个

		]
	},
	"ImageId":"centos_6_08_64_20G_alibase_20170824.vhd",  //不显示
	"InstanceTypeFamily":"ecs.c5",   //不显示
	"VlanId":"",//不显示
	"NetworkInterfaces":{
		"NetworkInterface":[
			{
				"MacAddress":"00:16:3e:08:52:0c",
				"PrimaryIpAddress":"192.168.29.227", //IP地址，多个显示在同一列，只显示ip，有些实例不显示IP地址，所以，内网IP用VpcAttributes.PrivateIpAddress.ipaddress 代替
				"NetworkInterfaceId":"eni-wz9fjsv2rrwe1rpsta0b"
			}
		]
	},
	"InstanceId":"i-wz91j960yqqwv3b81zny", // 显示
	"EipAddress":{//弹性ip，显示到一列中
		"IpAddress":"120.79.77.92",   
		"AllocationId":"eip-wz98p7cfuiqisgw3umyge",
		"InternetChargeType":"PayByTraffic",
		"IsSupportUnassociate":"True",
		"Bandwidth":5
	},
	"InternetMaxBandwidthIn":-1,//不显示
	"ZoneId":"cn-shenzhen-d",//显示
	"InternetChargeType":"",//不显示
	"SpotStrategy":"NoSpot",//不显示
	"StoppedMode":"Not-applicable",//不显示
	"SerialNumber":"d2b4ffc4-d511-4762-b79f-5220b4b0d522",//不显示
	"IoOptimized":"True",//显示
	"Memory":8192,//显示
	"Cpu":4,//显示
	"VpcAttributes":{//不显示
		"NatIpAddress":"",
		"PrivateIpAddress":{
			"IpAddress":[
				"192.168.29.227"  //内网IP地址显示这个值
			]
		},
		"VSwitchId":"vsw-wz982f1w68a6agljyi12h",
		"VpcId":"vpc-94g45i4gf"
	},
	"InternetMaxBandwidthOut":0,//不显示
	"DeviceAvailable":"True",DeviceAvailable
	"SecurityGroupIds":{//显示名称，多个显示在同一列
		"SecurityGroupId":[
			"sg-wz9aseg189xckyalq3lg"
		]
	},
	"SaleCycle":"",//不显示
	"SpotPriceLimit":0,//不显示
	"AutoReleaseTime":"",//不显示
	"StartTime":"2018-06-25T01:42Z",//显示
	"InstanceName":"华大币项目",//显示
	"Description":"",//显示
	"ResourceGroupId":"",//不显示
	"OSType":"linux",//不显示
	"OSName":"CentOS  6.8 64位",//显示
	"InstanceNetworkType":"vpc",//显示
	"PublicIpAddress":{//显示
		"IpAddress":[

		]
	},
	"HostName":"iZwz91j960yqqwv3b81znyZ",//显示
	"InstanceType":"ecs.c5.xlarge",//显示
	"CreationTime":"2018-06-25T01:42Z",//显示
	"Status":"Running",//显示
	"ClusterId":"",//不显示
	"Recyclable":"False",//不显示
	"RegionId":"cn-shenzhen",//不显示
	"GPUSpec":"NVIDIA P100"
	"DedicatedHostAttribute":{//显示
		"DedicatedHostId":"",
		"DedicatedHostName":""
	},
	"OperationLocks":{//不显示
		"LockReason":[

		]
	},
	"InstanceChargeType":"PrePaid",//显示
	"GPUAmount":1,//不显示
	"ExpiredTime":"2018-07-25T16:00Z"//不显示
}

```



### 专有云输出结果示例

```
{
    "Instances": {
        "Instance": [
            {
                "RegionId": "cn-sz-gjjy-d01", 
                "SerialNumber": "d9a0cc82-8545-446e-b30b-ed699d5d12a9", 
                "CreationTime": "2017-07-25T02:37Z", 
                "ExpiredTime": "1970-01-01T00:00Z", 
                "IoOptimized": false, 
                "PublicIpAddress": {
                    "IpAddress": [ ]
                }, 
                "InternetChargeType": "PayByTraffic", 
                "VpcAttributes": {
                    "VpcId": "", 
                    "VSwitchId": "", 
                    "PrivateIpAddress": {
                        "IpAddress": [ ]
                    }, 
                    "NatIpAddress": ""
                }, 
                "Status": "Running", 
                "Description": "Vs Phere Client", 
                "InstanceId": "i-88fr1k0la", 
                "HostName": "iZ88fr1k0laZ", 
                "ClusterId": "", 
                "ImageId": "win2012_64_std_r2_zh-cn_100G_bgi_20170719.vhd", 
                "InstanceTypeFamily": "ecs.s3", 
                "InstanceNetworkType": "classic", 
                "InstanceType": "ecs.s3.large", 
                "EipAddress": {
                    "InternetChargeType": "", 
                    "IpAddress": "", 
                    "AllocationId": ""
                }, 
                "InnerIpAddress": {
                    "IpAddress": [
                        "10.50.10.49"
                    ]
                }, 
                "OperationLocks": {
                    "LockReason": [ ]
                }, 
                "InstanceChargeType": "PostPaid", 
                "SecurityGroupIds": {
                    "SecurityGroupId": [
                        "sg-88fzwafme"
                    ]
                }, 
                "InternetMaxBandwidthOut": 0, 
                "ZoneId": "cn-sz-gjjy-am55001-a", 
                "InstanceName": "CNGB00019", 
                "Cpu": 4, 
                "InternetMaxBandwidthIn": 200, 
                "VlanId": "", 
                "Memory": 8192, 
                "DeviceAvailable": true
            }
        ]
    }, 
    "res": 0, 
    "TotalCount": 1, 
    "PageNumber": 1, 
    "RequestId": "7CB74631-53A3-416F-9B0E-49AAC6C5E5EF"
}
```