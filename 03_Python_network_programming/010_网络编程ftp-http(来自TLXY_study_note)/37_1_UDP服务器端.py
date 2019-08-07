import socket

# 模拟服务器的函数
# 建立一个服务器端

def serverFunc():
    # 1. 建立socket套接字对象
    # socket.socket(AddressFamily, Type)
    # 函数 socket.socket 创建一个socket对象，该函数带有两个参数：
    # Address Family：可以选择AF_INET（用于 Internet 进程间通信）或者 AF_UNIX（用于同一台机器进程间通信）,实际工作中常用AF_INET
    # Type：套接字类型，可以是SOCK_STREAM（流式套接字，主要用于TCP协议）或者SOCK_DGRAM（数据报套接字，主要用于UDP协议）
    # socket.AF_INET:使用ipv4协议
    # socket.SOCK_DGRAM使用UDP通信
    # socket.SOCK_STREAM使用TCP通信
    # 返回sock套接字对象
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.绑定ip和port
    # 127.0.0.1这个IP代表机器自身
    # 7852 随机指定的端口号
    # 地址是一个tuple类型（ip, port)
    addr = ('127.0.0.1', 7852)
    # 绑定地址和端口
    sock.bind(addr)

    # 3.接受对方消息
    # 等待方式为死等，没有其他可能性
    # recvfrom接受的返回值是一个tuple,前一项表示数据，后一项表示地址
    # recvfrom参数的含义是缓冲区大小
    data, addr = sock.recvfrom(500)
    print(data)

    # 发送过来的数据时bytes格式，必须通过解码才能得到格式的内容
    # decode解码函数默认参数是utf8
    text = data.decode()
    print(text)

    # 4.给对方返回消息
    # 发送的消息需要编码成bytes格式
    # encode默认也是utf8
    # 注意编码和解码要一致
    rsp = '我已经收到你的爱了，我也爱你'
    data = rsp.encode()
    sock.sendto(data, addr)

    # 5. 关闭套接字对象
    sock.close()

if __name__ == '__main__':
    print("Starting server......等待客户端消息")
    serverFunc()
    print("Ending server......关闭服务器端")





