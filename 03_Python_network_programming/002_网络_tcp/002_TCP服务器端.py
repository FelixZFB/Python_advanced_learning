# -*- coding:utf-8 -*-

import socket


def main():

    # 1. 创建tcp套接字对象
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定ip地址和port端口，绑定本地
    addr = ('127.0.0.1', 8080)
    tcp_server_socket.bind(addr)

    # 3. 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的链接了
    tcp_server_socket.listen(128)
    print('监听中，等待客户端链接......')

    # 4. 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
    # new_client_socket用来专门为这个客户端服务，负责通信
    # tcp_server_socket就可以省下来专门等待其他新客户端的链接，负责监听
    # accept()接收客户端的请求，接收客户端的ip和port
    # accept()返回值就是一个客户端套接字和客户端地址
    # tcp_server_socket.accept()默认处于阻塞状态，只有新的请求来时，解除阻塞，返回new_client_socket, client_addr
    new_client_socket, client_addr = tcp_server_socket.accept()
    print('客户端已链接，客户端地址：')
    print(client_addr)

    # 5. 接收客户端发送过来的数据,返回数据，此时等待也会处于阻塞状态
    recv_data = new_client_socket.recv(1024)
    print(recv_data.decode('gbk'))

    # 6. 发送数据
    new_client_socket.send('数据已收到'.encode('gbk'))


    # 7. 关闭套接字,关闭客户端套接字和监听套接字
    new_client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()

# 打开网络调试助手，选择TCP client，主机地址改成上面代码中绑定的地址和端口
# 运行程序，程序就开始监听，等待客户端链接,程序处于阻塞状态
# 网络调试助手作为客户端，点击连接，连接上服务器端，程序解除阻塞状态
# 发送消息给服务器端，接收服务器返回的消息


# 运行结果如下
# 可以发现，new_client_socket的
# client_addr的ip地址就是服务器端的IP地址，因为现在都是在同一个电脑
# port是6639，相当于给网络调试助手作为客户端分配了一个专门的接口


# 监听中，等待客户端链接......
# 客户端已链接，客户端地址：
# ('127.0.0.1', 6639)
# 你好，服务器
# Process finished with exit code 0

# [2019-07-13 11:21:44.870]# SEND ASCII>
# 你好，服务器
#
# [2019-07-13 11:21:44.873]# RECV ASCII>
# 数据已收到