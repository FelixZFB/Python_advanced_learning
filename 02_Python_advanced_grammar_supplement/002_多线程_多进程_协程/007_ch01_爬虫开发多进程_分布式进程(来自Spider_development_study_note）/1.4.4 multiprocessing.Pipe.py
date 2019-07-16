# 创建两个进程，一个子进程通过Pipe发送数据
# 一个子进程通过Pipe接受数据

import multiprocessing
import random
import time, os

# 先定义一个发送数据的方法
def proc_send(pipe, urls):
    for url in urls:
        print("Process(%s) send: %s" %(os.getpid(), url))
        pipe.send(url)
        time.sleep(random.random())

# 再定义一个接受数据的方法
def proc_recv(pipe):
    while True:
        print("Process(%s) rev:%s" %(os.getpid(), pipe.recv()))
        time.sleep(random.random())

# 定义主程序
if __name__ == '__main__':

    # 创建一个Pipe通信的实例
    pipe = multiprocessing.Pipe()
    # 创建两个子进
    # urls=['url_'+str(i) for i in range(10)]就是url_0到url_9的一个列表
    # 为什么传递pipe参数需要加0和1？？？
    p1 = multiprocessing.Process(target=proc_send, args=(pipe[0], ['url_'+str(i) for i in range(10)]))
    p2 = multiprocessing.Process(target=proc_recv, args=(pipe[1],))
    # 开始两个子进程
    p1.start()
    p2.start()
    # 等待两个子进程执行完毕
    p1.join()
    p2.join()
    p1.close()
    p2.close()

