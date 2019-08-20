# -*- coding:utf-8 -*-

import time

def work1():
    while True:
        print("----work1---")
        time.sleep(0.3)
        yield

def work2():
    while True:
        print("----work2---")
        time.sleep(0.3)
        yield

# 协程实现多任务
def main():
    w1 = work1()
    w2 = work2()
    while True:
        next(w1)
        next(w2)

if __name__ == "__main__":
    main()

# 我们先将上面yield注释掉，就变成了普通函数，main函数运行后只会一直运行work1
# work2并不会执行，因为work1执行完了才会执行work2

# 我们加上yield,就可以实现多任务了，work1执行到yield时候暂停，此时cpu释放
# work2执行，然后都yield暂停，又执行work1，反复轮流执行
# 如此就实现了协程多任务（并发），两个函数同时交替执行
# 协程多任务类似于多线程的执行，但是消耗的资源更少了


# 协程的切换只是单纯的操作CPU的上下文
# 协程的切换：每个线程都有自己缓存Cache等等数据，
# 操作系统还会帮你做这些数据的恢复操作。所以线程的切换非常耗性能