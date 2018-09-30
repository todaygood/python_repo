此接口用于查询vSwitch信息，展示时可以只显示abailable状态的vSwitch，并且，不显示批量计算相关的vSwitch（VSwitchName为cls开头）

```
{
    "PageNumber": 1, 
    "VSwitches": {
        "VSwitch": [
            {
                "CreationTime": "2018-05-07T06:35:24Z", 
                "RouteTable": {
                    "RouteTableId": "vtb-m5e75gekhvd8e47h4p54w", 
                    "RouteTableType": "System"
                }, 
                "CidrBlock": "10.0.0.0/24", 
                "Status": "Available", 
                "Description": "华大云管平台测试交换机", 
                "IsDefault": false, 
                "AvailableIpAddressCount": 252, 
                "VSwitchName": "bgi_cmp_sw_test", 
                "ZoneId": "cn-qingdao-b", 
                "VSwitchId": "vsw-m5etq9yuy5k9n9j0kgsjm", 
                "VpcId": "vpc-m5e9zj6o5f91d9ge74dvi"
            }
        ]
    }, 
    "TotalCount": 1, 
    "PageSize": 10, 
    "RequestId": "8878CD10-A02A-4881-B658-0FCBD7764F0B"
}

```