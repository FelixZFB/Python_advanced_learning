import socket

# Client端流程
# 客户端
# 1.建立通信的socket
# 2.发送内容到指定的服务器
# 3.接受服务器给定的反馈内容

def clientFunc():

    # 1. 建立socket连接
    # 建立连接socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 向服务器端发送消息
    # 编码消息
    text = '我爱你'
    data = text.encode()
    # 发送消息到服务器端
    sock.sendto(data, ('127.0.0.1', 7852))

    # 3. 接受服务器端信息
    # 接受服务器的消息,并对其解码
    data, addr = sock.recvfrom(200)
    text = data.decode()
    print(text)

if __name__ == '__main__':
    clientFunc()

