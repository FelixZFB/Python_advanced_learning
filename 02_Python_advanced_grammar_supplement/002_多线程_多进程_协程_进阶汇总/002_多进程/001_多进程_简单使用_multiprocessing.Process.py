# -*- coding:utf-8 -*-

import multiprocessing
import os
from time import sleep, ctime


def sing():
    for i in range(3):
        print("正在唱歌...%d" % i)
        sleep(1)
        print("process1 id: ", os.getpid())


def dance():
    for i in range(3):
        print("正在跳舞...%d" % i)
        sleep(1)
        print("process2 id: ", os.getpid())


def main():
    # 写函数名，没有括号，告诉Process函数在哪里
    # sing()有括号是调用执行函数
    p1 = multiprocessing.Process(target=sing)
    p2 = multiprocessing.Process(target=dance)

    # 调用start后，进程才正式开始执行
    p1.start()
    print(p1.name)
    print(p1.pid)
    p2.start()
    print(p2.name)
    print(p2.pid)

if __name__ == '__main__':
    # 获取父进程ID,即整个if __name__ == '__main__':下面的代码
    print("parent process: ", os.getppid())
    main()


# 代码+资源 主进程  (main)
# 代码+资源 子进程1（p1）
# 代码+资源 子进程2 (p2)
# 相对于多线程，占用的资源更多了



