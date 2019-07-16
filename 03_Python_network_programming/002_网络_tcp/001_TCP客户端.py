# -*- coding:utf-8 -*-

import socket

def main():
    # 1. 创建tcp的套接字对象
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 链接服务器端
    server_ip = input('请输入要链接的服务器的IP:')
    server_port = int(input('请输入要链接的服务器的port:'))
    server_addr = (server_ip, server_port)
    tcp_client_socket.connect(server_addr)

    # 3. 发送数据
    # 加入while循环，输入退出命令时候，才关闭客户端
    while True:
        send_data = input('请输入要发送的数据(输入EXIT退出)：')
        if send_data != 'EXIT':
            tcp_client_socket.send(send_data.encode('gbk')) # 此处使用gbk编码，使用utf-8网络调试助手解码后乱码
        else:
            break

    # 4. 接收对方发送过来的数据，最大接收1024个字节
    recvData = tcp_client_socket.recv(1024)
    print('接收到的数据为:', recvData.decode('gbk'))

    # 5. 关闭tcp套接字对象
    tcp_client_socket.close()


if __name__ == '__main__':
    main()

# 打开H:\ProgramDevelop\netassist下的网络调试助手（作为服务器端）
# 协议类型选择TCP Server
# 运行代码，输入网络调试助手中的IP和端口号，然后发送消息
# 网络调试助手中IP和端口可以修改，修改为私网IP，端口非著名端口即可

# 运行如下：
# 请输入要链接的服务器的IP:192.168.56.1
# 请输入要链接的服务器的port:8080
# 请输入要发送的数据(输入EXIT退出)：哈哈哈
# 请输入要发送的数据(输入EXIT退出)：你好吗！
# 请输入要发送的数据(输入EXIT退出)：EXIT
# 接收到的数据为: 我很好啊
#
# Process finished with exit code 0

# [2019-07-12 16:05:41.240]# Client 192.168.56.1:4089 gets online.
#
# [2019-07-12 16:05:48.417]# RECV ASCII FROM 192.168.56.1 :4089>
# 哈哈哈
#
# [2019-07-12 16:05:59.239]# RECV ASCII FROM 192.168.56.1 :4089>
# 你好吗！
#
# [2019-07-12 16:06:10.202]# SEND ASCII TO ALL>
# 我很好啊
#
# [2019-07-12 16:06:16.208]# Client 192.168.56.1:4089 gets offline.

# 上面发现客户端地址其实也是本电脑，IP地址一样，但是端口不同，相当于就是不同的进程