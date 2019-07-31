# -*- coding:utf-8 -*-

# 创建一个Web服务器，客户端请求后，返回显示所需要的页面
# 下面代码中已经加入了html文件夹的系统路径
# 打开一个网页后，自连接都可以打开了
# 程序会根据请求提取出名字，然后进入到html文件中查找匹配相关文件
# 然后再浏览器中显示出来

import socket
import re
import threading


def service_client(new_socket):
    "为一个客户端进行服务,为这个客户端返回数据"

    # 1. 接收浏览器发送过来的请求，即HTTP请求
    request_data = new_socket.recv(1024).decode("utf-8")
    # 将请求报文以行分隔为列表
    request_header_lines = request_data.splitlines()
    # 格式化打印出请求报文信息，换行打出
    for line in request_header_lines:
        print(line)

    # 提取出请求网页的名称，即/后面的内容
    # 先取出请求头的第一行
    request_line = request_header_lines[0]
    # 匹配出/之外的任何字符，就是从GET开始匹配，然后从后面的/之后视为一个分组
    # 匹配出出空格外的任何内容，即从第一个/开始匹配到空格结束
    # 请求头的第一行request_line：GET /index.html HTTP/1.1
    # 匹配结果：GET /index.html 我们提取出/以后的内容
    get_file_name = re.match("[^/]+(/[^ ]*)", request_line).group(1)
    # 加入系统路径，网页都是放在html文件夹中
    get_file_name = "./html" + get_file_name
    print("file name is ===>%s" % get_file_name)
    print('*' * 50)

    # 2. 返回http格式的数据给浏览器
    # 请求的网页也可能不存在，加入try语句
    try:
        f = open(get_file_name, 'rb')
    except:
        response_header = "HTTP/1.1 404 not found\r\n"
        response_header += "\r\n"
        response_body = "====sorry ,file not found===="
    else:
        # 2.1 组织相应头信息(header)，浏览器中换行使用\r\n
        response_header = "HTTP/1.1 200 OK\r\n"  # 200表示找到这个资源
        response_header += "\r\n"  # 用一个空的行与body进行隔开，作为换行符
        # 组织内容(body)
        # 返回一个本地已经编辑好的前端html页面
        response_body = f.read()
        f.close()
    finally:
        # 2.2 组织响应报文，发送数据,由于已经不是单纯的字符串，不能使用拼接
        # 头和体信息单独发送
        # response = response_header + response_body
        # 先发送头header信息
        new_socket.send(response_header.encode("utf-8"))
        # 再发送body信息
        new_socket.send(response_body)

        # 3. 关闭客户端套接字
        new_socket.close()


def main():
    "作为程序的主控制入口，完成整体控制"

    # 1. 创建tcp套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置当服务器先close，即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7788端口
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 服务器绑定本地IP地址和端口
    server_socket.bind(("", 7788))

    # 3. 设置为监听套接字
    server_socket.listen(128)

    # 加入循环，服务器一直处于运行状态，可以不断接收新的客户端请求，
    # 浏览器可以通过刷新不断请求该服务器
    while True:
        # 4. 等待新客户端的连接，返回一个新的客户端专用套接字
        new_socket, client_addr = server_socket.accept()

        # 5. 使用多进程为这个客户端服务，有新的请求，又重新创建一个子进程
        new_process = threading.Thread(target=service_client, args=(new_socket, ))
        new_process.start()


        # 注意：多线程不会复制new_socket，共享这个全局变量，此处不能close


if __name__ == "__main__":
    main()


# 运行程序，打开浏览器，访问网址：http://127.0.0.1:7788/index.html
# 浏览器运行结果：
# 显示了一个html页面
# 如果随便访问一个网址：http://127.0.0.1:7788/index555.html，
# QQ浏览器则会无法显示此网页 错误代码 HTTP ERROR 404
# 火狐浏览器没有内容显示


# 打印出的请求头信息
# GET /index.html HTTP/1.1
# Host: 127.0.0.1:7788
# Connection: keep-alive
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
# Accept-Encoding: gzip, deflate, br
# Accept-Language: zh-CN,zh;q=0.9
#
# file name is ===>./html/index.html
# **************************************************