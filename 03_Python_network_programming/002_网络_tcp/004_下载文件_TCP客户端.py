# -*- coding:utf-8 -*-

import socket

def main():

    # 1. 创建套接字对象
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 获取服务器的IP和端口
    dest_ip = input('请输入服务器的IP：')
    dest_port = int(input('请输入服务器的port：'))

    # 3. 链接服务器
    tcp_socket.connect((dest_ip, dest_port))

    # 4. 获取下载的文件名字
    download_file_name = input('请输入要下载的文件名称：')

    # 5. 将文件名字发送到服务器
    tcp_socket.send(download_file_name.encode('utf-8'))

    # 6. 接收文件中的数据
    recv_data = tcp_socket.recv(1024) # 1024--->1K  1024*1024--->1K*1024=1M

    # 7. 保存接收的数据到一个文件中
    if recv_data:
        with open('004_new_' + download_file_name, 'wb') as f:
            f.write(recv_data)

    # 8. 关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()

# 运行方式1：网络调试助手作为服务器端
# 打开网络调试助手作为服务器端，然后打开运行
# 运行代码，输入网络调试助手的IP和port
# 发送要下载的文件名称，随便写一个作为测试
# 服务器端发送数据给客户端(当做要下载文件的数据)
# 客户端接收数据，然后打开一个文件，将数据保存进去
# 下载的文件：004_new_test_file

# 运行方式2:005作为服务器端
# 先运行005，在运行004
# 下载的文件：004_new_test_file_1
