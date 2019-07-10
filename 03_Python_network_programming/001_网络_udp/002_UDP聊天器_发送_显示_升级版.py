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
    print("来自%s的消息:%s" % (str(recv_data[1]), recv_data[0].decode('utf-8')))


def main():
    # 1. 创建udp套接字对象
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2. 绑定IP地址和端口(传入的是一个tuple类型)
    udp_socket.bind(('127.0.0.1', 7999))

    # 循环循环来处理请求
    while True:
        print("---本地我与我的聊天器---")
        print("功能选择，请输入以下数字:")
        print("1:发送消息")
        print("2:接收消息")
        print("0:退出聊天系统")
        op = input('请输入功能：')

        if op == '1':
            # 调用发送消息函数
            send_msg(udp_socket)

        elif op == '2':
            # 调用接收接收显示消息函数
            recv_msg(udp_socket)

        elif op == '0':
            break

        else:
            print("输入有误，请重新选择功能输入")

if __name__ == '__main__':
    main()

# 先选择功能1发送消息，我们可以多次选择1，发送多次，消息存储在内存之中
# 然后再选择2接收显示消息，每次只会取出一条，取出之前都存储在内存中

'''
---本地我与我的聊天器---
功能选择，请输入以下数字:
1:发送消息
2:接收消息
0:退出聊天系统
请输入功能：1
请输入对方的IP:127.0.0.1
请输入对方的port:7999
输入要发送的消息：消息1
---本地我与我的聊天器---
功能选择，请输入以下数字:
1:发送消息
2:接收消息
0:退出聊天系统
请输入功能：1
请输入对方的IP:127.0.0.1
请输入对方的port:7999
输入要发送的消息：消息2
---本地我与我的聊天器---
功能选择，请输入以下数字:
1:发送消息
2:接收消息
0:退出聊天系统
请输入功能：2
来自('127.0.0.1', 7999)的消息:消息1
---本地我与我的聊天器---
功能选择，请输入以下数字:
1:发送消息
2:接收消息
0:退出聊天系统
请输入功能：2
来自('127.0.0.1', 7999)的消息:消息2
---本地我与我的聊天器---
功能选择，请输入以下数字:
1:发送消息
2:接收消息
0:退出聊天系统
请输入功能：
'''






