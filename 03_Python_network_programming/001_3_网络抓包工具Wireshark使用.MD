## Wireshark网络抓包工具使用

参考为的博文：https://blog.csdn.net/u011318077/article/details/98469452

## 1 Wireshark干嘛用的？

- Wireshark可以从最底层从你选取的网卡
- 抓取从网络源头到目的地的所有数据（双方IP，端口，协议，数据等）
- 比如：从QQ给你的好友发送一条消息
- Wireshark可以抓取整个过程的数据

- Wireshark的作用
    - 网络编程中，你的代码有问题还是网络有问题
    - 可以通过Wireshark抓包进行判断

## 2 Wireshark的安装
- 直接网络搜索Wireshark，有英文版也有中文版
- 免费软件，直接下载安装即可

- 官网地址：https://www.wireshark.org/
- 官网下载地址：https://www.wireshark.org/#download


## 3 数据拦截
- 拦截本地回环数据
    本机访问本机的回环数据是不经过网卡的，
    比如我们在本机访问搭建在本机上的web服务，
    但我们经常有服务搭建在本机的操作也经常有拦截本地回环数据包加以分析的需求，
    所以我们环要拦载回环数据包。操作如下。
    
    首先，以管理员身份运行cmd（普通用户没有路由表操作权限，会提示“请求的操作需要提升”）
    然后，使用ipconfig查看本机ip和网关：
    ipconfig
    
    再然后，使用以下命令添加路由，指定回环数据也要先转发到网关（使用上一步获取本的本机ip和网关替换其中的<your_IP>和<gateway_IP>）：    
    route add <your_IP> mask 255.255.255.255 <gateway_IP> metric 1
    
    最后，查看路由表中路由是否已添加成功：
    route print
    
    回环数据经网关再回来会增加网卡的压力，可使用以下命令删除路由（使用前边获取本的本机ip替换其中的<your_IP>）：    
    route delete <your_IP>
    
    参考博文：https://www.cnblogs.com/lsdb/p/9254544.html

- 抓取网络数据
    网络数据抓取，启动软件，选取要抓取的网卡即可
    具体参考Wireshark的使用
    
## 4 Wireshark的使用

- 软件启动，选取要抓取的网卡，参考以下图片001
- 软件界面介绍 参考002图片，对比002_1_TCPIP协议(族).png

## 5 应用显示过滤器
- 显示过滤器表达式作用在在wireshark捕获数据包之后，从已捕获的所有数据包中显示出符合条件的数据包，隐藏不符合条件的数据包。

- 一条基本的表达式由过滤项、过滤关系、过滤值三项组成。
- 比如ip.addr == 192.168.1.1，
- 这条表达式中ip.addr是过滤项、==是过滤关系，192.168.1.1是过滤值
-（整条表达示的意思是找出所有ip协议中源或目标ip、等于、192.168.1.1的数据包）

- 常见用显示过滤需求及其对应表达式
    - 数据链路层：
    
    筛选mac地址为04:f9:38:ad:13:26的数据包----eth.src == 04:f9:38:ad:13:26
    
    筛选源mac地址为04:f9:38:ad:13:26的数据包----eth.src == 04:f9:38:ad:13:26
    
    - 网络层：
    
    筛选ip地址为192.168.1.1的数据包----ip.addr == 192.168.1.1
    
    筛选192.168.1.0网段的数据---- ip contains "192.168.1"
    
    筛选192.168.1.1和192.168.1.2之间的数据包----ip.addr == 192.168.1.1 && ip.addr == 192.168.1.2
    
    筛选从192.168.1.1到192.168.1.2的数据包----ip.src == 192.168.1.1 && ip.dst == 192.168.1.2
    
    - 传输层：
    
    筛选tcp协议的数据包----tcp
    
    筛选除tcp协议以外的数据包----!tcp
    
    筛选端口为80的数据包----tcp.port == 80
    
    筛选12345端口和80端口之间的数据包----tcp.port == 12345 && tcp.port == 80
    
    筛选从12345端口到80端口的数据包----tcp.srcport == 12345 && tcp.dstport == 80
    
    - 应用层：
    
    特别说明----http中http.request表示请求头中的第一行（如GET index.jsp HTTP/1.1），http.response表示响应头中的第一行（如HTTP/1.1 200 OK），其他头部都用http.header_name形式。
    
    筛选url中包含.php的http数据包----http.request.url contains ".php"
    
    筛选内容包含username的http数据包----http contains "username"
    
- 补充：

    过滤地址
    ip.addr==192.168.10.10  或  ip.addr eq 192.168.10.10  #过滤地址
    ip.src==192.168.10.10     #过滤源地址
    ip.dst==192.168.10.10     #过滤目的地址
     
    过滤协议，直接输入协议名
    icmp 
    http
     
    过滤协议和端口
    tcp.port==80
    tcp.srcport==80
    tcp.dstport==80
     
    过滤http协议的请求方式
    http.request.method=="GET"
    http.request.method=="POST"
    http.request.uri contains admin   #url中包含admin的
    http.request.code==404    #http请求状态码的
     
    连接符
    &&  
    ||
    and
    or
    
- 参考网址：https://www.cnblogs.com/lsdb/p/9254544.html


## 6 Wireshark展示TCP三次握手
- 参考网址：http://www.winwin7.com/JC/9065.html

## 7 Wireshark深入使用
- 数据流追踪 
- 专家信息说明
- 数据包的统计分析 
参考网址：https://blog.csdn.net/qq_36119192/article/details/84671638

