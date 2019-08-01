# -*- coding:utf-8 -*-


import socket
import re
import time
import select


def service_client(request_data, client_socket):
    "为一个客户端进行服务,为这个客户端返回数据"
    # 1. 处理接收到的请求数据
    if not request_data:
        return

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
        # 先发送头header信息
        client_socket.send(response_header.encode("utf-8"))
        # 再发送body信息
        client_socket.send(response_body.encode("utf-8"))

    else:
        # 2.1 组织相应头信息(header)，浏览器中换行使用\r\n
        response_body = f.read()
        f.close()

        response_header = "HTTP/1.1 200 OK\r\n"  # 200表示找到这个资源
        # 告诉客户端body数据的长度，可以消除长连接一直等待数据问题
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"  # 用一个空的行与body进行隔开，作为换行符

        # 2.2 组织响应报文，发送数据
        # 合并header信息（先编码为二进制）和body信息
        response = response_header.encode("utf-8") + response_body
        client_socket.send(response)


def main():
    "作为程序的主控制入口，完成整体控制"

    # 1. 创建tcp套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置当服务器先close，即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7788端口
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 服务器绑定本地IP地址和端口
    server_socket.bind(("", 7788))

    # 3. 设置为监听套接字和epoll对象并注册
    server_socket.listen(128)

    # 将服务器套接字设置为非阻塞
    # server_socket.setblocking(False)

    # 创建epoll对象
    epl = select.epoll()

    # fd是对象在内存空间中的一个标记，相当于一个id
    # 将tcp服务器套接字对应的标记fd（server_socket.fileno()）注册到epoll中进行监听
    # fileno()是文件描述符,select.EPOLLIN是数据事件
    epl.register(server_socket.fileno(), select.EPOLLIN)

    # 创建上面添加的fd对应的套接字的字典
    fd_event_dict = dict()

    while True:

        # 5. 使用epoll进行监听，事件通知，处理事件
        # 默认会阻塞,直到os监测到数据到来，通过事件通知方式告诉程序，此时解阻塞
        fd_event_list = epl.poll()

        # 上面的返回值是元组列表，(fd, envent)
        # 循环取出的fd也就是文件描述符xxx_socket.fileno()
        # (套接字对应的文件描述符，这个文件描述符究竟是什么事件 比如可以调用recv接收等)
        for fd, event in fd_event_list:
            # 如果监听到的的fd是服务器套接字，则可以接收数据，即可以accept
            if fd == server_socket.fileno():
                # 等待新客户端的连接，返回一个新的客户端专用套接字，accept()默认是阻塞的
                new_socket, client_addr = server_socket.accept()
                # 向epoll中注册连接到socket的可读事件，即将新客户端也注册到监听列表中
                epl.register(new_socket.fileno(), select.EPOLLIN)
                # 将这个客户端添加到字典中进行记录
                fd_event_dict[new_socket.fileno()] = new_socket
            # 如果是接收到数据的事件
            elif event == select.EPOLLIN:
                # 1. 接收浏览器发送过来的请求，即HTTP请求
                # 注意，如果客户端调用close,request_data就为空，因此下面使用了if判断是否有数据
                # 根据上面循环取出的fd取出字典里面对应的套接字
                request_data = fd_event_dict[fd].recv(1024).decode("utf-8")

                # 如果对方发来了消息，进行下一步处理，
                if request_data:
                    # 对方发送过来了数据
                    service_client(request_data, fd_event_dict[fd])
                else:
                    # 如果没有消息或者对方调用close关闭客户端，并从字典中移除
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]


if __name__ == "__main__":
    main()


# 代码需要在Linux下运行
# epoll使用的是Linux内核



