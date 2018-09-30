# 本文档定义了清单页面默认展示及可选展示的内容，包括管理员、用户各自的界面

[DescribeInstances 结果示例](https://gitlab.genomics.cn/tianjing/cloud-management-platform/blob/master/Ali_describeInstance.md) 

示例中多项内容需分行显示


| 列名 | 管理员默认(Y/N) | 管理员可选(Y/N) | 用户默认(Y/N) | 用户可选(Y/N) | DescribeInstance var | 示例|
| ------ | ---------- | ---------- | -------- | --------- | ---- | --- | 
| Instance ID | Y | N | Y | N |  InstanceId | i-wz91j960yqqwv3b81zny | 
| Instance Name | Y | N | Y | N| InstanceName | 华大币项目 | 
| Operating System | Y | Y | Y | Y| OSName | CentOS  6.8 64位 | 
| Monitor | Y | Y | Y |Y | 无,暂时留空| 显示图标，连接为空 |
| Zone | Y | Y | Y |Y| ZoneId | cn-shenzhen-d | 
| Private IP | Y | N | Y | N| InnerIpAddress或PrimaryIpAddress，多个时显示在一列 | 192.168.44.34   10.224.4.1 |
| EIP | Y | Y | Y| Y| EipAddress 全部子项显示在一列 | 1.1.1.1   eip-wz98p7cfuiqisgw3umyge     PayByTraffic    Bandwidth:5Mbps |
| Public IP | Y | Y | Y |Y | PublicIpAddress.IpAddress | EIP 和 public IP 二选一 | 
| Status | Y | Y | Y | Y| Status | Runnging | 
| Network Type | N | Y |N |Y | InstanceNetworkType | vpc | 
| Configuration | Y | Y | Y | Y | Cpu,Memory（单位GB）,IoOptimized（如果为true显示，false不显示）, GPUSpec | CPU：4vcpu   Memory：8GB     IoOptimzed    GPUSpec:NVIDIA P100 |  | 
| Billing Method | Y | Y | Y | Y|InstanceChargeType，ExpiredTime(显示用户在OA上填的到期时间) | PrePaid     ExpiredTime：2019/12/31 00:00:00 | 
| SecurityGroup | N | Y | N | Y | SecurityGroupIds（显示id对应的名称，多个显示在一列） | 云管平台安全组      测试安全组 |
| StartTime | N | Y | N | Y | StartTime | 2018-06-25 14:34:20 |
| Description | N | Y | N | Y | Description | 云管平台测试机1 | 
| HostName | N | Y | N | Y | HostName| cmp-1 | 
| InstanceType | Y | Y | N | N | InstanceType | ecs.c5.xlarge | 
| CreationTime | N | Y | N |Y |CreationTime| 2018-06-24 10:20:14
| Manage | Y | N | Y |N | Start/Stop/Force Stop/Reboot/Force Reboot |  | 
