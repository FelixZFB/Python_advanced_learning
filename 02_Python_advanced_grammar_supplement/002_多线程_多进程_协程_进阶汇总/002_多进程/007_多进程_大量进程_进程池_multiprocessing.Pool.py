# -*- coding:utf-8 -*-

from multiprocessing import Pool
import os, time, random

def worker(msg):
    t_start = time.time()
    print("%s开始执行,进程号为%d" % (msg,os.getpid()))
    # random.random()随机生成0~1之间的浮点数
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕，耗时%0.2f" % (t_stop-t_start))

def main():
    po = Pool(3)  # 定义一个进程池，最大进程数3
    for i in range(0,10):
        # Pool().apply_async(要调用的目标,(传递给目标的参数元祖,))
        # 每次循环将会用空闲出来的子进程去调用目标
        # 上一个进程结束后，开始下一个新的进程
        # 子进程会使用前面结束的进程号，进程号中国只有3个，3会使用第一个结束的进程号
        po.apply_async(worker,(i,))

    print("----start----")
    po.close()  # 关闭进程池，关闭后po不再接收新的请求
    # 进程池必须加上join()，不然主进程不会等待子进程，直接结束了
    po.join()  # 等待po中所有子进程执行完成，必须放在close语句之后
    print("-----end-----")

if __name__ == '__main__':
    main()