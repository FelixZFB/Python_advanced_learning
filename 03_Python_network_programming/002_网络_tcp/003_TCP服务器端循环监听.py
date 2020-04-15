# -*- coding:utf-8 -*-

import socket


def main():

    # 1. 创建tcp套接字对象
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定ip地址和port端口，绑定本地
    addr = ('127.0.0.1', 8080)
    tcp_server_socket.bind(addr)

    # 3. 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的链接了
    # 该监听套接字启动后一直会处于监听状态
    tcp_server_socket.listen(128)
    print('监听中，等待客户端链接......')

    # 循环为多个客户端服务
    # 有了新的请求过来，就返回一个新的客户端，相当于从上面监听的结果中不断的取出新的客户端
    while True:
        data = input('输入任何内容开始为多个客户端服务(输入EXIT退出服务)：')
        if data != 'EXIT':
            print('等待一个新的客户端到来：')
            # 4. 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
            # new_client_socket用来专门为这个客户端服务，负责通信
            # tcp_server_socket就可以省下来专门等待其他新客户端的链接，负责监听
            # accept()接收客户端的请求，接收客户端的ip和port
            # accept()返回值就是一个客户端套接字和客户端地址
            # tcp_server_socket.accept()默认处于阻塞状态，只有新的请求来时，解除阻塞，返回new_client_socket, client_addr
            new_client_socket, client_addr = tcp_server_socket.accept()
            print('一个新的客户端已链接，客户端地址：%s' % str(client_addr))

            # 循环为某一个客户多次服务
            while True:
                # 5. 接收客户端发送过来的数据,返回数据，此时等待也会处于阻塞状态
                # 解阻塞有两种方式：客户端发来数据和对方客户端断开连接(客户端调用了close)，网络调试助手上面断开连接即可调用close
                recv_data = new_client_socket.recv(1024)
                print('客户端发过来的数据是：%s' % recv_data.decode('gbk'))

                # 如果上面的recv解阻塞,进行判断是否有数据
                if recv_data:
                    # 6. 发送数据,返回给客户端
                    new_client_socket.send('数据已收到'.encode('gbk'))
                else:
                    break

            # 7. 关闭accept返回的套接字,关闭新客户端套接字，结束对该客户的服务
            new_client_socket.close()
            print('已经服务完毕......')

        else:
            break

    # 8. 关闭服务器端套接字，即关闭监听套接字，结束监听
    tcp_server_socket.close()


if __name__ == '__main__':
    main()

# 分别同时打开两个网络调试助手，选择TCP client，主机地址改成上面代码中绑定的地址和端口
# 运行服务器程序，程序就开始监听，等待客户端链接,程序处于阻塞状态
# 网络调试助手1先连接，连接上服务器端，程序解除阻塞状态，服务器开始为1号客户端服务
# 发送消息给服务器端，接收服务器返回的消息，直到1号客户端断开链接
# 服务器继续监听，2号客户端链接，为2号服务，2号服务结束后
# 服务器可以继续监听，或者选择EXIT退出服务器端

# 服务器同时只为一个客户端服务，一个客户端服务结束后，才能进行下一个客户端服务

# 实际应用中，服务器端会一直运行，不会关闭,我上面while循环加入了关闭条件
# 如果服务器监听时候，服务器主动EXIT，就关闭服务器了

