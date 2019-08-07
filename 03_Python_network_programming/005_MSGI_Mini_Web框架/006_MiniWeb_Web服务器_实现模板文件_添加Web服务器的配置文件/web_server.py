import socket
import re
import multiprocessing
import time
import sys
import dynamic.mini_frame


class WSGIServer(object):
    def __init__(self, port, app, static_path):
        # 1. 创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 2. 绑定,使用外部参数port
        self.tcp_server_socket.bind(("", port))

        # 3. 变为监听套接字
        self.tcp_server_socket.listen(128)

        # 使用外部参数app
        self.application = app

        # 静态请求文件夹加入类属性，用于之后静态请求的调用
        self.static_path = static_path

    def service_client(self, new_socket):
        """为这个客户端返回数据"""

        # 1. 接收浏览器发送过来的请求 ，即http请求  
        # GET / HTTP/1.1
        # .....
        request = new_socket.recv(1024).decode("utf-8")
        # print(">>>"*50)
        # print(request)

        request_lines = request.splitlines()
        print("")
        print(">"*20)
        print(request_lines)

        # GET /index.html HTTP/1.1
        # get post put del
        file_name = ""
        ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
        if ret:
            file_name = ret.group(1)
            # print("*"*50, file_name)
            if file_name == "/":
                file_name = "/index.html"

        # 2. 返回http格式的数据，给浏览器
        # 2.1 如果请求的资源不是以.py结尾，那么就认为是静态资源（html/css/js/png，jpg等）
        if not file_name.endswith(".py"):
            try:
                f = open(self.static_path + file_name, "rb")
            except:
                response = "HTTP/1.1 404 NOT FOUND\r\n"
                response += "\r\n"
                response += "------file not found-----"
                new_socket.send(response.encode("utf-8"))
            else:
                html_content = f.read()
                f.close()
                # 2.1 准备发送给浏览器的数据---header
                response = "HTTP/1.1 200 OK\r\n"
                response += "\r\n"
                # 2.2 准备发送给浏览器的数据---boy
                # response += "hahahhah"

                # 将response header发送给浏览器
                new_socket.send(response.encode("utf-8"))
                # 将response ic.mini_frame.applicationbody发送给浏览器
                new_socket.send(html_content)
        else:
            # 2.2 如果是以.py结尾，那么就认为是动态资源的请求

            env = dict()  # 这个字典中存放的是web服务器要传递给 web框架的数据信息
            env['PATH_INFO'] = file_name
            # {"PATH_INFO": "/index.py"}
            # 直接使用外面传入的模块参数self.application = app
            body = self.application(env, self.set_response_header)

            header = "HTTP/1.1 %s\r\n" % self.status

            for temp in self.headers:
                header += "%s:%s\r\n" % (temp[0], temp[1])

            header += "\r\n"

            response = header+body
            # 发送response给浏览器
            new_socket.send(response.encode("utf-8"))


        # 关闭套接
        new_socket.close()

    def set_response_header(self, status, headers):
        self.status = status
        self.headers = [("server", "mini_web v8.8")]
        self.headers += headers
        

    def run_forever(self):
        """用来完成整体的控制"""

        while True:
            # 4. 等待新客户端的链接
            new_socket, client_addr = self.tcp_server_socket.accept()

            # 5. 为这个客户端服务
            p = multiprocessing.Process(target=self.service_client, args=(new_socket,))
            p.start()

            new_socket.close()


        # 关闭监听套接字
        self.tcp_server_socket.close()


def main():
    """控制整体，创建一个web 服务器对象，然后调用这个对象的run_forever方法运行"""
    # sys.argv获取命令行启动时传入的参数
    # 先判断python之后传入的参数是不是三个，然后取出第2个参数即为port接口，第三个参数即框架
    if len(sys.argv) == 3:
        try:
            port = int(sys.argv[1]) # 7890
            frame_app_name = sys.argv[2] # mini_frame:application
        except Exception as ret:
            print('端口输入错误......%s' % ret)
            return

    else:
        print('请按照以下格式运行代码')
        print('python xxx.py 7788 mini_frame:application')
        return # return没有返回值，执行到此结束函数

    # mini_frame:application
    ret = re.match(r"([^:]+):(.*)", frame_app_name)
    if ret:
        frame_name = ret.group(1) # mini_frame
        app_name = ret.group(2) # application
    else:
        print('请按照以下格式运行代码')
        print('python xxx.py 7788 mini_frame:application')
        return  # return没有返回值，执行到此结束函数

    # 因为只是一个文件，不是文件夹，./可以省略
    with open('./web_server.conf') as f:
        # eval() 函数用来执行一个字符串表达式，并返回表达式的值
        # f.read()读取结果是str，eval返回字符串的值
        # 字符串的值读取时是普通字符串，但在py中就是字典格式了，就将其转为字典了
        conf_info = eval(f.read())
        # {
        #     "static_path":"./static",
        #     "dynamic_path":"./dynamic"
        # }


    # 将dynamic模块文件夹路径加入到系统路径中，下面的__import__就可以到文件夹中去查找了
    sys.path.append(conf_info['dynamic_path'])
    # 变量名作为模块导入，使用__import__
    frame = __import__(frame_name) # 返回值标记导入的这个模块
    app = getattr(frame, app_name) # 返回值app此时就指向了dynamic文件夹中mini_frame模块的application函数
    # print(frame, app) # <module 'mini_frame' from './dynamic\\mini_frame.py'> <function application at 0x0000026B29E4FF28>

    # 将静态文件夹路径传递给WSGIServer，顶部加入到类属性中，用于调用
    wsgi_server = WSGIServer(port, app, conf_info['static_path'])
    wsgi_server.run_forever()


if __name__ == "__main__":
    main()

# CMD窗口激活虚拟环境，然后切换到web_server.py所在的目录
# 然后使用python web_server.py 7788 mini_frame:application指定端口和框架运行
# 然后网页打开http://127.0.0.1:7788/index.py

# (venv) D:\Hello World\python_work\Python_advanced_learning\03_Python_network_programming\
# 005_MSGI_Mini_Web框架\005_MiniWeb_Web服务器_实现模板文件_指定端口及框架>python web_server.py 7788 mini_frame:application