#coding=utf-8
import threading
import time

def saySorry():
    print("亲爱的，我错了，我能吃饭了吗？")
    time.sleep(5)

# if开始是主线程
# t.start()开始的就是子线程
if __name__ == "__main__":

    # 循环启动多个线程
    for i in range(5):
        # 传入函数名，函数不需要括号，有括号就是调用函数了
        t = threading.Thread(target=saySorry)
        t.start() #启动线程，即让线程开始执行

    print()
    # activeCount()查看当前进行的线程数量
    print(threading.activeCount())
    # enumerate() 返回当前所有活跃线程列表
    # 一个主线程（即当前的进程），下面有5个子线程
    print(threading.enumerate())
    # 返回当前线程数量
    print(len(threading.enumerate()))


# 多线程并发执行，saySorry一个接着一个启动，不需要等待第一个执行完毕
# 总执行时间才花了5秒多一点

# 可以明显看出使用了多线程并发的操作，花费时间要短很多
# 当调用start()时，才会真正的创建线程，并且开始执行
