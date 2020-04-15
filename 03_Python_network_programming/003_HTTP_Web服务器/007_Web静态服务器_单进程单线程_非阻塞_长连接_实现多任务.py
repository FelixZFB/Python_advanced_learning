# -*- coding:utf-8 -*-

# 创建一个Web服务器，客户端请求后，返回显示所需要的页面，下面代码中已经加入了html文件夹的系统路径
# 打开一个网页后，自连接都可以打开了，程序会根据请求提取出名字，然后进入到html文件中查找匹配相关文件，然后再浏览器中显示出来

# tcp套接字的accept和recv方法默认是阻塞，我们此程序将其改为非阻塞
# 执行到accept和recv即使没有接受到消息，也继续向下执行
# 单进程单线程实现多个浏览器客户端的多任务

# 由于recv默认是阻塞的，如果某个用户超时或者一直不发来消息，程序就会再次卡住
# 下一个用户想进来就进不来，就实现不了多任务，设置为非阻塞后，就会消除这个问题


import socket
import re
import time


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
    # 上面提取出来的请求头的第一行是：GET /index.html HTTP/1.1
    # 从/之外的任何字符开始匹配，匹配多次，相当于从GET开始匹配，
    # 匹配到第一个/，后面匹配除了空格外的任何字符，相当于匹配到html结束，后面出现了空格
    # 并且从/之后的匹配视为一个分组，分组里面匹配结果就是/index.html
    # group(0)是取出匹配的整体结果：GET /index.html
    # group(1)就是第一个分组：/index.html
    get_file_name = re.match("[^/]+(/[^ ]*)", request_line).group(1)
    # 加入系统路径，网页都是放在html文件夹中
    get_file_name = "./html" + get_file_name  # ./html/index.html
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
        # 浏览器得到的数据长度达到返回的长度就会主动断开连接，避免一直连接占用资源
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

    # 3. 设置为监听套接字
    server_socket.listen(128)

    # 将服务器套接字设置为非阻塞
    server_socket.setblocking(False)

    # 4. 为这个客户端服务
    # 由于recv默认是阻塞的，如果某个用户超时或者一直不发来消息，程序就会再次卡住
    # 下一个用户想进来就进不来，就实现不了多任务，设置为非阻塞后，就会消除这个问题
    # 加入循环，服务器一直处于运行状态，可以不断接收新的客户端请求，
    # 创建一个用于存储新客户端的列表
    client_socket_list = list()

    while True:
        # 程序运行起来，没有客户端来一直会不断循环打印，便于观察加入等待
        time.sleep(3)
        try:
            # 5. 等待新客户端的连接，返回一个新的客户端专用套接字，accept()默认是阻塞的
            new_socket, client_addr = server_socket.accept()
        except Exception as ret:
            print('---没有客户端到来: %s---' % ret)
        else:
            print('---只要没有产生异常就意味着来了一个新的客户端---')
            # 设置套接字为非阻塞模式
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)

        # 循环为每个客户端服务
        for client_socket in client_socket_list:
            # 有些客户端可能没有发送数据过来，使用try语句判断
            try:
                # 1. 接收浏览器发送过来的请求，即HTTP请求
                # 注意，如果客户端调用close,request_data就为空，因此下面使用了if判断是否有数据
                request_data = client_socket.recv(1024).decode("utf-8")
            except Exception as ret:
                print('---这个客户端没有发送消息过来：%s---' % ret)
            else:
                # 如果对方发来了消息，进行下一步处理，
                if request_data:
                    # 对方发送过来了数据
                    print('---客户端发来了消息---')
                    service_client(request_data, client_socket)
                    # 每一次接收数据发送数据后就主动断开连接，短连接模式，每次接发送数据一次
                    # 下面2行代码注释掉就变成了长连接模式了，参考006案例代码底部运行方式4的说明
                    # client_socket.close()
                    # client_socket_list.remove(client_socket)
                else:
                    # 如果没有消息或者对方调用close关闭客户端，并从列表中移除
                    client_socket.close()
                    client_socket_list.remove(client_socket)
                    print('---客户端已经关闭---')
        print(client_socket_list)


if __name__ == "__main__":
    main()

# 上面代码已经变为了长连接，上面已经加入了body的长度，消除了浏览器一直等待数据的问题
# 此时打开浏览器运行，数据都可以正常请求显示出来

# 上面调用service_client(request_data, client_socket)后，
# 下面关闭代码已经注释掉了，客户端会一直保持和服务器的连接
# while再次循环时，该浏览器（固定IP和端口）再次请求一个新的网页，还是使用之前未关闭的客户端
# 如果while再次循环没有数据请求，则调用else关闭该客户端
# 长连接主要目的，减少连接次数，减少占用服务器的资源
# 客户请求频繁，将在TCP的建立和关闭操作上浪费时间和带宽


