# -*- coding:utf-8 -*-

# 创建一个Web服务器，客户端请求后，返回显示一个固定的页面

import socket


def service_client(new_socket):
    "为一个客户端进行服务,为这个客户端返回数据"

    # 1. 接收浏览器发送过来的请求，即HTTP请求
    request_data = new_socket.recv(1024).decode("utf-8")
    request_header_lines = request_data.splitlines()
    # 格式化打印出请求报文信息，换行打出
    for line in request_header_lines:
        print(line)

    # 2. 返回http格式的数据给浏览器
    # 2.1 组织相应头信息(header)，浏览器中换行使用\r\n
    response_headers = "HTTP/1.1 200 OK\r\n"  # 200表示找到这个资源
    response_headers += "\r\n"  # 用一个空的行与body进行隔开，作为换行符
    # 组织内容(body)
    response_body = "hello world \r\nWeb静态服务器显示一个固定页面\r\n打猪猪"

    # 2.2 组织响应报文，发送数据
    response = response_headers + response_body
    new_socket.send(response.encode("gbk"))

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


# 运行程序，打开浏览器，访问网址：127.0.0.1:7788
# 浏览器运行结果：
# hello world
# Web静态服务器显示一个固定页面
# 打猪猪


# 打印出的请求头信息
# GET / HTTP/1.1
# Host: 127.0.0.1:7788
# User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
# Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
# Accept-Encoding: gzip, deflate
# Connection: keep-alive
# Upgrade-Insecure-Requests: 1
# Cache-Control: max-age=0