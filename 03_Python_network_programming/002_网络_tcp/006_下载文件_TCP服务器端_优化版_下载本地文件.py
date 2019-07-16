# -*- coding:utf-8 -*-

import socket

def send_file_to_client(new_client_socket, client_addr):

    # 1. 接收客户端发送过来要下载的文件名,此时等待也会处于阻塞状态
    file_name = new_client_socket.recv(1024).decode('utf-8')
    print('客户端(%s)需要下载的文件是:%s' % (str(client_addr), file_name))

    file_content = None
    # 2. 打开要下载的文件，读取数据,此处直接使用open，如果没有文件就是上面的None
    try:
        f = open(file_name, 'rb')
        file_content = f.read()
        f.close()
    except Exception as ret:
        print('服务器没有要下载的文件:%s' % file_name)

    # 3. 发送文件的数据给客户端
    if file_content:
        new_client_socket.send(file_content)


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
    new_client_socket, client_addr = tcp_server_socket.accept()

    # 5. 发送数据给客户端
    send_file_to_client(new_client_socket, client_addr)

    # 6. 关闭套接字,关闭客户端套接字和监听套接字
    new_client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()

# 用客户端下载testfile.py文件
# 下载后重命名为004_new_testfile.py
# 先运行006服务器然后运行004客户端
# 输入要下的文件名称：testfile.py
# 然后下载完成