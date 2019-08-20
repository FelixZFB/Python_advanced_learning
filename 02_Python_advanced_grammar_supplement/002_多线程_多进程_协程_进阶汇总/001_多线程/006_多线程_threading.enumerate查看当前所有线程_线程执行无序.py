# -*- coding:utf-8 -*-

# 多线程start()之后执行的循序不确定，并不一定按启动顺序执行
# 要想按顺序执行，可以加入延时功能

import threading
import time


def test1():
    for i in range(5):
        print('-----test1-----%d-----' % i)


def test2():
    for i in range(5):
        print('-----test2-----%d-----' % i)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    time.sleep(1)
    print('-----1-----')

    t2.start()
    time.sleep(1)
    print('-----2-----')

    print(threading.enumerate())


if __name__ == '__main__':
    main()