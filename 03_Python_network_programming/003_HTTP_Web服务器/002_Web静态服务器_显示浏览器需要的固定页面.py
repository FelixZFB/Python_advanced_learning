# -*- coding:utf-8 -*-

# 创建一个Web服务器，客户端请求后，返回显示一个固定的页面

import socket
import re

def service_client(new_socket):
    "为一个客户端进行服务,为这个客户端返回数据"

    # 1. 接收浏览器发送过来的请求，即HTTP请求
    request_data = new_socket.recv(1024).decode("utf-8")
    # 将请求报文以行分隔为列表
    request_header_lines = request_data.splitlines()
    # 格式化打印出请求报文信息，换行打出
    for line in request_header_lines:
        print(line)

    # 浏览器访问网址：http://127.0.0.1:7788/index.html
    # 提取出请求网页的名称，即/后面的内容
    # 先取出请求头的第一行：GET /index.html HTTP/1.1
    request_line = request_header_lines[0]

    # 上面提取出来的请求头的第一行是：GET /index.html HTTP/1.1
    # 从/之外的任何字符开始匹配，匹配多次，相当于从GET开始匹配，
    # 匹配到第一个/，后面匹配除了空格外的任何字符，相当于匹配到html结束，后面出现了空格
    # 并且从/之后的匹配视为一个分组，分组里面匹配结果就是/index.html
    # group(0)是取出匹配的整体结果：GET /index.html
    # group(1)就是第一个分组：/index.html

    get_file_name = re.match("[^/]+(/[^ ]*)", request_line).group(1)
    print("请求的file name is ===>%s" % get_file_name)
    print('*' * 50)

    # 2. 返回http格式的数据给浏览器
    f = open('.\html\index.html', 'rb')
    html_content = f.read()
    f.close()

    # 2.1 组织相应头信息(header)，浏览器中换行使用\r\n
    response_headers = "HTTP/1.1 200 OK\r\n"  # 200表示找到这个资源
    response_headers += "\r\n"  # 用一个空的行与body进行隔开，作为换行符
    # 组织内容(body)
    # 返回一个本地已经编辑好的前端html页面

    # 2.2 组织响应报文，发送数据,由于已经不是单纯的字符串，不能使用拼接
    # 头和体信息单独发送
    # response = response_headers + response_body
    # 先发送头header信息
    new_socket.send(response_headers.encode("gbk"))
    # 再发送body信息
    new_socket.send(html_content)


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

        # 5. 为这个客户端服务
        service_client(new_socket)


if __name__ == "__main__":
    main()


# 运行程序，打开浏览器，访问网址：http://127.0.0.1:7788/index.html
# 浏览器运行结果：
# 显示了一个html页面


# 按行打印出请求头信息，输出结果：
# GET /index.html HTTP/1.1
# Host: 127.0.0.1:7788
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
# Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
# Accept-Encoding: gzip, deflate
# Connection: keep-alive
# Upgrade-Insecure-Requests: 1
# Cache-Control: max-age=0
#
# file name is ===>GET /index.html
# **************************************************
