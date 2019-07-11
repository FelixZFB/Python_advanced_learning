# -*- coding:utf-8 -*-

import socket

def main():
    # 1. 创建tcp的套接字对象
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 链接服务器端
    server_ip = input('请输入要链接的服务器的IP:')
    server_port = int(input('请输入要链接的服务器的port:'))
    server_addr = (server_ip, server_port)
    tcp_socket.connect(server_addr)

    # 3. 发送/接收数据
    # 加入while循环，输入退出命令时候，才关闭客户端
    while True:
        send_data = input('请输入要发送的数据(输入EXIT退出)：')
        if send_data != 'EXIT':
            tcp_socket.send(send_data.encode('gbk')) # 此处使用gbk编码，使用utf-8网络调试助手解码后乱码
        else:
            break

    # 4. 关闭tcp套接字对象
    tcp_socket.close()


if __name__ == '__main__':
    main()

# 打开H:\ProgramDevelop\netassist下的网络调试助手
# 协议类型选择TCP Server
# 运行代码，输入网络调试助手中的IP和端口号，然后发送消息
# 网络调试助手中IP和端口可以修改，修改为私网IP，端口非著名端口即可

# 运行如下：
# 请输入要链接的服务器的IP:192.168.56.1
# 请输入要链接的服务器的port:8080
# 请输入要发送的数据(输入EXIT退出)：护发黄飞鸿
# 请输入要发送的数据(输入EXIT退出)：哈哈哈
# 请输入要发送的数据(输入EXIT退出)：EXIT
#
# Process finished with exit code 0

# 调试助手窗口就会接收到消息
# [2019-07-11 21:59:45.162]# Client 192.168.56.1:13474 gets online.
#
# [2019-07-11 21:59:48.369]# RECV ASCII FROM 192.168.56.1 :13474>
# 护发黄飞鸿
#
# [2019-07-11 21:59:51.275]# RECV ASCII FROM 192.168.56.1 :13474>
# 哈哈哈
#
# [2019-07-11 22:00:40.179]# Client 192.168.56.1:13474 gets offline.

# 上面发现客户端地址其实也是本电脑，IP地址一样，但是端口不同，相当于就是不同的进程