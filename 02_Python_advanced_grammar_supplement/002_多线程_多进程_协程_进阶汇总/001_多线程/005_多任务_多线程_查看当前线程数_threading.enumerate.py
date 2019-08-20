# -*- coding:utf-8 -*-

import threading
from time import sleep,ctime

def sing():
    for i in range(3):
        print("正在唱歌...%d"%i)
        sleep(1)

def dance():
    for i in range(3):
        print("正在跳舞...%d"%i)
        sleep(1)

if __name__ == '__main__':
    print('---开始多线程任务---:%s'%ctime())

    # 写函数名，没有括号，告诉Thread函数在哪里
    # sing()有括号是调用执行函数
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    # 调用start后，线程才正式开始执行
    t1.start()
    t2.start()

    while True:
        # 获取当前程序的线程数
        length = len(threading.enumerate())
        print('当前运行的线程数为：%d' % length)

        # 子线程全部结束，只有一个主线程后，退出循环
        if length <= 1:
            break

        sleep(0.9)