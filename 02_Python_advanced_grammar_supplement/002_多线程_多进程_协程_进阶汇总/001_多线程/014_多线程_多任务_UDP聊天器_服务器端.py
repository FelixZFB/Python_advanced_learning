# -*- coding:utf-8 -*-

import threading
import socket

def send_msg(udp_socket):
    """获取键盘数据，并将其发送给对方"""
    while True:
        # 1. 从键盘输入数据
        msg = input("\n请输入要发送的数据:")
        # 2. 输入对方的ip地址
        dest_ip = input("\n请输入对方的ip地址:")
        # 3. 输入对方的port
        dest_port = int(input("\n请输入对方的port:"))
        # 4. 发送数据
        udp_socket.sendto(msg.encode("utf-8"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    """接收数据并显示"""
    while True:
        # 1. 接收数据
        recv_msg = udp_socket.recvfrom(1024)
        # 2. 解码
        recv_ip = recv_msg[1]
        recv_msg = recv_msg[0].decode("utf-8")
        # 3. 显示接收到的数据
        print(">>>%s:%s" % (str(recv_ip), recv_msg))


def main():
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2. 绑定本地信息
    udp_socket.bind(("127.0.0.1", 7890))
    # 3. 创建一个子线程用来接收数据，参数后面需要写一个逗号，代表元组
    t = threading.Thread(target=recv_msg, args=(udp_socket,))
    t.start()
    # 4. 让主线程用来检测键盘数据并且发送
    send_msg(udp_socket)


if __name__ == "__main__":
    main()


# 运行，启动一个网络调试助手，作为客户端，打开链接
# 然后发送数据，填写调试助手的IP和端口
# 进行聊天