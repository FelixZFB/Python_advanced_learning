# -*- coding:utf-8 -*-

# 使用while循环，反复查看线程数量
# 运行结果显示，运行过程中，有一个主线程和两个子线程
# 子线程结束后，最后只有一个主线程运行


import threading
import time


def test1():
    for i in range(5):
        print('-----test1-----%d-----' % i)
        time.sleep(1)


def test2():
    for i in range(5):
        print('-----test2-----%d-----' % i)
        time.sleep(1)

def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    t2.start()

    while True:
        print(threading.enumerate())
        # 子线程全部结束，只有一个主线程后，退出循环

        if len(threading.enumerate()) <= 1:
            break

        time.sleep(1)


if __name__ == '__main__':
    main()