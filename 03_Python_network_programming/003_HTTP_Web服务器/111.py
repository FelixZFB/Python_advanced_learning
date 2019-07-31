#coding=utf-8
import socket
import re
import multiprocessing


class WSGIServer(object):

    def __init__(self, server_address):
        # 创建一个tcp套接字
        self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 允许立即使用上次绑定的port
        self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定
        self.listen_socket.bind(server_address)
        # 变为被动，并制定队列的长度
        self.listen_socket.listen(128)

    def serve_forever(self):
        "循环运行web服务器，等待客户端的链接并为客户端服务"
        while True:
            # 等待新客户端到来
            client_socket, client_address = self.listen_socket.accept()
            print(client_address)  # for test
            new_process = multiprocessing.Process(target=self.handleRequest, args=(client_socket,))
            new_process.start()

            # 因为子进程已经复制了父进程的套接字等资源，所以父进程调用close不会将他们对应的这个链接关闭的
            client_socket.close()

    def handleRequest(self, client_socket):
        "用一个新的进程，为一个客户端进行服务"
        recv_data = client_socket.recv(1024).decode('utf-8')
        print(recv_data)
        requestHeaderLines = recv_data.splitlines()
        for line in requestHeaderLines:
            print(line)

        request_line = requestHeaderLines[0]
        get_file_name = re.match("[^/]+(/[^ ]*)", request_line).group(1)
        print("file name is ===>%s" % get_file_name) # for test

        if get_file_name == "/":
            get_file_name = DOCUMENTS_ROOT + "/index.html"
        else:
            get_file_name = DOCUMENTS_ROOT + get_file_name

        print("file name is ===2>%s" % get_file_name) # for test

        try:
            f = open(get_file_name, "rb")
        except IOError:
            response_header = "HTTP/1.1 404 not found\r\n"
            response_header += "\r\n"
            response_body = "====sorry ,file not found===="
        else:
            response_header = "HTTP/1.1 200 OK\r\n"
            response_header += "\r\n"
            response_body = f.read()
            f.close()
        finally:
            client_socket.send(response_header.encode('utf-8'))
            client_socket.send(response_body)
            client_socket.close()


# 设定服务器的端口
SERVER_ADDR = (HOST, PORT) = "", 8888
# 设置服务器服务静态资源时的路径
DOCUMENTS_ROOT = "./html"


def main():
    httpd = WSGIServer(SERVER_ADDR)
    print("web Server: Serving HTTP on port %d ...\n" % PORT)
    httpd.serve_forever()

if __name__ == "__main__":
    main()