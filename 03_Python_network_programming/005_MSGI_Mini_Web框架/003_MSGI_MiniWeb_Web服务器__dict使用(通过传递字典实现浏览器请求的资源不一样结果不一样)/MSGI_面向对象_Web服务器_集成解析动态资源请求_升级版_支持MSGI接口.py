# -*- coding:utf-8 -*-

# 创建一个Web服务器，客户端请求后，返回显示所需要的页面
# 下面代码中已经加入了html文件夹的系统路径,会进入到html文件中查找匹配相关文件
# 将代码封装到一个类中，面向对象
# 动态资源请求单独放置mini_frame中进行处理

import socket
import re
import time
import multiprocessing
import mini_frame


class WSGIServer():

    def __init__(self):
        # 1. 创建tcp套接字
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 设置当服务器先close，即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7788端口
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 2. 服务器绑定本地IP地址和端口
        self.server_socket.bind(("", 7788))

        # 3. 设置为监听套接字
        self.server_socket.listen(128)


    def service_client(self, new_socket):
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
        # 匹配结果：GET /index.html 我们提取出/及以后的内容
        get_file_name = re.match("[^/]+(/[^ ]*)", request_line).group(1)
        # 加入网页所在的系统路径，网页都是放在html文件夹中，此时html是放在上级目录，上上级使用../../html
        file_name = "../html" + get_file_name
        print("file name is ===>%s" % get_file_name)
        print('*' * 50)

        # 2. 返回http格式的数据给浏览器
        # 返回header（http协议内容）和body（浏览器要显示的内容）

        # 2.1 如果请求的资源不是以.py结尾，就认为是静态资源(比如html,css,js,png,jpg等)
        if not file_name.endswith('.py'):
            # 请求的网页也可能不存在，加入try语句
            try:
                f = open(file_name, 'rb')

            except:
                # 如果请求的页面不能打开，即不存在，返回以下信息
                response_header = "HTTP/1.1 404 not found\r\n"
                response_header += "\r\n"
                response_body = "====sorry ,file not found===="
                response = response_header + response_body
                new_socket.send(response.encode("utf-8"))

            else:
                # 页面存在，则返回相应的页面信息
                # 2.1.1 组织响应头信息(header)，浏览器中换行使用\r\n
                response_header = "HTTP/1.1 200 OK\r\n"  # 200表示找到这个资源
                response_header += "\r\n"  # 用一个空的行与body进行隔开，作为换行符
                # 组织内容(body)
                # 返回一个本地已经编辑好的前端html页面
                response_body = f.read()
                f.close()
                # 2.1.2 组织响应报文，发送数据,由于已经不是单纯的字符串，不能使用拼接
                # 头和体信息单独发送,或者编码后一起发送
                response = response_header.encode("utf-8") + response_body
                new_socket.send(response)

        else:
            # 2.2 如果是以.py结尾，那么就认为是动态资源请求
            # 调用mini_frame专门用于动态请求
            # 以下代码就实现了Web服务器支持MSGI协议
            # 代码执行流程：查看mini_frame.py中的说明
            env = dict()
            response_body = mini_frame.application(env, self.set_response_header)


            response_header = 'HTTP/1.1 %s\r\n' % self.status
            # 提取出self.headers里面的信息，添加到response_header中去
            for temp in self.headers:
                response_header += '%s:%s\r\n' %(temp[0], temp[1])
            response_header += "\r\n"
            # 浏览器默认解析使用的是gbk，gbk可以显示更多的汉字，此处直接使用utf-8会乱码
            # Content-Type里面指定charset编码是utf-8就可以完美显示中文了
            response = response_header + response_body

            new_socket.send(response.encode("utf-8"))

        # 3. 关闭客户端套接字
        new_socket.close()

    # 定义一个函数，专门用于返回动态请求的headers信息
    def set_response_header(self, status, headers):
        self.status = status
        # 手动加一个Web服务器的版本信息
        self.headers = [('Server', 'mini_web v8.0')]
        self.headers += headers


    def run_forever(self):
        # 加入循环，服务器一直处于运行状态，可以不断接收新的客户端请求，
        # 浏览器可以通过刷新不断请求该服务器
        while True:
            # 4. 等待新客户端的连接，返回一个新的客户端专用套接字，accept()默认是阻塞的
            # 有一个新的请求来了，就开始一个新的进程，不然一直处于阻塞，while循环就在该处等待
            new_socket, client_addr = self.server_socket.accept()

            # 5. 使用多进程为这个客户端服务，有新的请求，又重新创建一个子进程
            # 此时每来一个用户就单独创建一个子进程，每个子进程都是独立，即使某个用户出现了超时也不会影响其它用户
            # 多进程多线程多协程都可以实现多任务，单进程设置为非阻塞也可以实现多任务，参考006案例
            new_process = multiprocessing.Process(target=self.service_client, args=(new_socket, ))
            new_process.start()

            # 注意：父进程中的new_socket, client_addr = server_socket.accept()已经创建了一个new_socket客户端
            # 我们此处要将其关闭，不然子进程关闭了，父进程里面的并不会关闭，浏览器请求网页了就会一直处于刷新转圈状态
            # 没有关闭客户端与服务器连接，相当于没有挥手成功
            # 因为子进程已经复制了父进程的套接字等资源，所以父进程此处调用close不会将子进程对应的这个链接关闭的
            new_socket.close()

        # 关闭监听套接字，while未加入break语句，就一直处于监听状态，该语句没有机会执行可以注释掉
        # self.server_socket.close()

def main():
    """控制整体，创建一个web服务器对象，然后调用对象的run_forever方法"""
    wsgi_server = WSGIServer()
    wsgi_server.run_forever()


if __name__ == "__main__":
    main()


# 运行程序，打开浏览器，访问网址：http://127.0.0.1:7788/index.html
# 然后访问：http://127.0.0.1:7788/register.py
# 已经调用了mini_frame中的方法
# 上面已经加入的系统路径，网页中此时的子连接都可以打开了
# 会自动根据文件名调用html中的相匹配文件显示出来

