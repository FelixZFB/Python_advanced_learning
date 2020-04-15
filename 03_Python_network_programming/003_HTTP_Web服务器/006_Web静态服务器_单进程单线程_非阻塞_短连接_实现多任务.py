# -*- coding:utf-8 -*-

# 创建一个Web服务器，客户端请求后，返回显示所需要的页面，下面代码中已经加入了html文件夹的系统路径
# 打开一个网页后，所有连接都可以打开了，程序会根据请求提取出名字，然后进入到html文件中查找匹配相关文件，然后再浏览器中显示出来

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
        # 再发送body信息,上面是str格式，需要进行编码
        client_socket.send(response_body.encode("utf-8"))
    else:
        # 2.1 组织相应头信息(header)，浏览器中换行使用\r\n
        response_header = "HTTP/1.1 200 OK\r\n"  # 200表示找到这个资源
        response_header += "\r\n"  # 用一个空的行与body进行隔开，作为换行符
        # 组织内容(body)
        # 返回一个本地已经编辑好的前端html页面
        response_body = f.read()
        f.close()

        # 2.2 组织响应报文，发送数据,由于已经不是单纯的字符串，不能使用拼接
        # 头和体信息单独发送
        # response = response_header + response_body
        # 先发送头header信息
        client_socket.send(response_header.encode("utf-8"))
        # 再发送body信息
        client_socket.send(response_body)


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
                    # 下面2行代码注释掉就变成了长连接模式了，参考代码底部运行方式4的说明
                    client_socket.close()
                    client_socket_list.remove(client_socket)
                else:
                    # 如果没有消息或者对方调用close关闭客户端，并从列表中移除
                    client_socket.close()
                    client_socket_list.remove(client_socket)
                    print('---客户端已经关闭---')
        print(client_socket_list)


if __name__ == "__main__":
    main()

# 运行方式1：
# while True之后加入等待时间
# 运行代码
# 打开三个网络调试助手，作为TCP客户端，连接到该服务器
# 可以看到连接状态，由于代码处理的是浏览器的请求，网络调试助手发送消息过来会产生错误
# 参考006_单进程单线程非阻塞运行运行结果1

# 运行方式2：
# 使用网络调试助手模拟浏览器的请求
# 请求一个网页，发送消息里面模拟浏览器的 请求头消息：get /index.html
# 程序运行结果打印出消息，程序将header和body信息返回给调试助手
# 参考006_单进程单线程非阻塞运行运行结果2


# 运行方式3（展示多任务执行效果）：
# 打开2个网络调试助手，模拟两个浏览器客户端
# 多任务模式
# 同时连接然后，发送消息，都收到消息后，断开连接
# 运行结果里面list有两个socket客户端
# 参考006_单进程单线程非阻塞运行运行结果3


# 运行方式4（浏览器实现多任务）：
#                 if request_data:
#                     # 对方发送过来了数据
#                     print('---客户端发来了消息---')
#                     service_client(request_data, client_socket)
#                     client_socket.close()
#                     client_socket_list.remove(client_socket)
# 上面代码，服务器完成一次数据接收，发送一次数据给客户端后，套接字就关闭了
# 下次浏览器请求又是一次新的连接，加上上面代码就相当于短连接
# 打开火狐和QQ浏览器，分别请求不同的网页，实现多任务效果


# 如果将上面最后两行代码注释掉，就变成长连接了，浏览器请求数据过来后，service_client发送数据给客户端
# 但是service_client中并没有调用close，就一直处于连接状态，
# 浏览器作为客户端并不知道数据发送完没有，就会等待继续接收数据，先前的数据存在缓存中
# 我们使用浏览器请求一个页面会发现一直在转圈，页面不会显示出来，如果停止代码运行，相当于主动关闭了连接
# 浏览器页面才会显示出请求的页面
# 代码运行结果可以看见，浏览器一直处于刷新状态，客户端会越来越多，电脑CPU慢慢就被占满了
# 打印出来的socket_client_list会越来越多

# 如何即保持长连接，又可以使浏览器每请求一次就正常显示页面？
# 即告诉浏览器，这次请求的数据已经全部发送完毕，浏览器客户端就会主动关闭，断开连接
# 只需要在header里面加上Content-Length即可，表明要发送给客户端数据的长度，浏览器接收数据达到规定的长度
# 就会主动断开连接，显示出接收到的数据
# 参考007案例
