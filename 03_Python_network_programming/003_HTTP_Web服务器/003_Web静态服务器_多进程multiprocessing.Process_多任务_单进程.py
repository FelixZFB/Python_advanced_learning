# -*- coding:utf-8 -*-

# 创建一个Web服务器，客户端请求后，返回显示所需要的页面
# 下面代码中已经加入了html文件夹的系统路径
# 打开一个网页后，自连接都可以打开了
# 程序会根据请求提取出名字，然后进入到html文件中查找匹配相关文件
# 然后再浏览器中显示出来

# 003升级为多进程，快速点击不同的连接，明显发现004打开网页速度会更快

import socket
import re
import multiprocessing


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

    # 上面提取出来的请求头的第一行是：GET /index.html HTTP/1.1
    # 从/之外的任何字符开始匹配，匹配多次，相当于从GET开始匹配，
    # 匹配到第一个/，后面匹配除了空格外的任何字符，相当于匹配到html结束，后面出现了空格
    # 并且从/之后的匹配视为一个分组，分组里面匹配结果就是/index.html
    # group(0)是取出匹配的整体结果：GET /index.html
    # group(1)就是第一个分组：/index.html

    get_file_name = re.match("[^/]+(/[^ ]*)", request_line).group(1)
    # 加入网页所在的系统路径，网页都是放在html文件夹中
    get_file_name = "./html" + get_file_name # ./html/index.html
    print("file name is ===>%s" % get_file_name)
    print('*' * 50)

    # 2. 返回http格式的数据给浏览器
    # 请求的网页也可能不存在，加入try语句
    try:
        f = open(get_file_name, 'rb')

    except:
        # 如果请求的页面不能打开，即不存在，返回以下信息
        response_header = "HTTP/1.1 404 not found\r\n"
        response_header += "\r\n"
        response_body = "====sorry ,file not found===="
        response = response_header + response_body
        new_socket.send(response.encode("utf-8"))

    else:
        # 页面存在，则返回相应的页面信息
        # 2.1 组织响应头信息(header)，浏览器中换行使用\r\n
        response_header = "HTTP/1.1 200 OK\r\n"  # 200表示找到这个资源
        response_header += "\r\n"  # 用一个空的行与body进行隔开，作为换行符
        # 组织内容(body)
        # 返回一个本地已经编辑好的前端html页面
        response_body = f.read()
        f.close()
        # 2.2 组织响应报文，发送数据,由于已经不是单纯的字符串，不能使用拼接
        # 头和体信息单独发送,或者编码后一起发送
        response = response_header.encode("utf-8") + response_body
        new_socket.send(response)

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
        # 4. 等待新客户端的连接，返回一个新的客户端专用套接字，accept()默认是阻塞的
        new_socket, client_addr = server_socket.accept()

        # 5. 使用多进程为这个客户端服务，有新的请求，又重新创建一个子进程
        # 此时每来一个用户就单独创建一个子进程，每个子进程都是独立，即使某个用户出现了超时也不会影响其它用户
        # 多进程多线程多协程都可以实现多任务，单进程设置为非阻塞也可以实现多任务，参考006案例
        new_process = multiprocessing.Process(target=service_client, args=(new_socket, ))
        new_process.start()

        # 注意：父进程中的new_socket, client_addr = server_socket.accept()已经创建了一个new_socket客户端
        # 我们此处要将其关闭，不然子进程关闭了，父进程里面的并不会关闭，浏览器请求网页了就会一直处于刷新转圈状态
        # 没有关闭客户端与服务器连接，相当于没有挥手成功
        # 因为子进程已经复制了父进程的套接字等资源，所以父进程此处调用close不会将子进程对应的这个链接关闭的
        new_socket.close()

        # service_client(new_socket)


if __name__ == "__main__":
    main()


# 运行程序，打开浏览器，访问网址：http://127.0.0.1:7788/index.html
# 上面已经加入的系统路径，网页中此时的子连接都可以打开了
# 会自动根据文件名调用html中的相匹配文件显示出来


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