import socket

# Client端流程
# 客户端
# 1.建立通信的socket
# 2.发送内容到指定的服务器
# 3.接受服务器给定的反馈内容

def clientFunc():
    # 建立连接socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 编码消息
    text = 'I love you baby'
    data = text.encode()
    # 发送消息到服务器端
    sock.sendto(data, ('127.0.0.1', 7852))
    # 接受服务器的消息,并对其解码
    data, addr = sock.recvfrom(200)
    text = data.decode()
    print(text)

if __name__ == '__main__':
    clientFunc()

