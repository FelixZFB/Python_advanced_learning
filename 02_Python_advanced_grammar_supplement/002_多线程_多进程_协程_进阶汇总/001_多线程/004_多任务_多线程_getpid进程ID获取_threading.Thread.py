# -*- coding:utf-8 -*-

import threading
import os
from time import sleep, ctime


def sing():
    for i in range(3):
        print("正在唱歌...%d" % i)
        sleep(1)


def dance():
    for i in range(3):
        print("正在跳舞...%d" % i)
        sleep(1)


def main():
    # 写函数名，没有括号，告诉Thread函数在哪里
    # sing()有括号是调用执行函数
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    # 调用start后，线程才正式开始执行
    t1.start()
    t2.start()

if __name__ == '__main__':
    # 获取父线程ID,即整个if __name__ == '__main__':下面的代码
    print("parent process: ", os.getppid())

    main()

    # 获取子线程ID
    print("process id: ", os.getpid())

# 每次唱歌跳舞都是同时执行的

# getpid():返回当前进程的id
# getppid():返回当前进程父进程的id



