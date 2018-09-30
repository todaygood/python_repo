# 本文档定义了Overview仪表盘页面显示的内容

Overview页面展示的资源池包括：阿里公有云、阿里专有云、腾讯云、VMware和Openstack。暂时只有阿里公有云可用，其他框灰掉，灰掉的框内容可以和阿里公有云相同。

1. 搜索： Overview页面最上方需要一个搜索框，用于全站搜索

2. 消息中心：搜索框下方需要消息中心，包括待办事项和平台告警：
    * 待办事项展示oa传过来的任务信息
        * 显示内容示例：xxx提交的oa申请（申请单号为：oa-xxx-2918-xxx）需要处理
        * 点击消息，跳转到示例创建页面
    * 平台告警展示系统自动发现的Instance 信息，需要管理员确认
        * 显示内容示例1：[warning] 阿里云有2台ECS在云管平台中没有记录，请确认
        * 显示内容示例2：[warning] 阿里云有5台ECS记录信息和云管平台不一致，请确认
        * 点击消息，跳转到具体消息页面，消息页面展示没有记录或者不一致的ECS条目，并有2个选项：确认更新 or 放弃更新并忽略消息
    * 如消息中心为空，可以隐藏不显示

## 阿里公有云

| 产品名称 | 显示内容 |
| -------- | -------- |
| Elastic Compute Servive | Total：`158`；   Running： `156`；  Expiring：`30` | 
| ApsaraDB for RDS  | Total：`4` |
| Server Load Balancer | Total: `20` |
| Object Storage Service | Total Bucket: `5`; Total Size: `200T` |
| NAS | Total FileSystem: `6`; Total Size: `500T` |
| Elastic IP Address | Total: `98` |
| BatchCompute | Total: `2` | 

