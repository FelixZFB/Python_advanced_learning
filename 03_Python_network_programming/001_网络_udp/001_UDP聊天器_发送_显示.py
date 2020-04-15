# -*- coding:utf-8 -*-

# UDP聊天器案例：
# 说明：
# 在一个电脑中编写1个程序，有2个功能
# 1.获取键盘数据，并将其发送给对方
# 2.接收数据并显示
# 并且可以选择以上的2个功能调用

import socket


def send_msg(udp_socket):
    '''发送消息'''
    dest_ip = input('请输入对方的IP:')
    dest_port = int(input('请输入对方的port:'))
    send_data = input('输入要发送的消息：')
    udp_socket.sendto(send_data.encode('utf-8'), (dest_ip, dest_port))


def recv_msg(udp_socket):
    '''接收显示消息'''
    recv_data = udp_socket.recvfrom(1024)
    print("来自%s:%s的消息" % (str(recv_data[1]), recv_data[0].decode('utf-8')))


def main():
    # 1. 创建udp套接字对象
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2. udp套接字对象绑定IP地址和端口(传入的是一个tuple类型)
    udp_socket.bind(('127.0.0.1', 7999))

    # 循环循环来处理请求
    while True:
        # 调用发送消息函数
        send_msg(udp_socket)

        # 调用接收接收显示消息函数
        recv_msg(udp_socket)


if __name__ == '__main__':
    main()

# 运行程序,自己和自己聊天：


# 请输入对方的IP:127.0.0.1
# 请输入对方的port:7999
# 输入要发送的消息：hahahahaha
# 来自('127.0.0.1', 7999):hahahahaha
# 请输入对方的IP:

# 因为只有一台电脑，相当于自己和自己聊天，
# 消息，必须先发送，然后接受显示出来
# 如果没有消息，程序就会阻塞，一直等待着
# 002案例进行功能升级

# 运行方式2：
# 打开网络调试助手，选择UDP，UDP没有区分服务器端和客户端
# 因为UDP服务器和客户端创建没有区别，方法都一样
# 运行结果查看：001_UDP聊天器_运行测试









