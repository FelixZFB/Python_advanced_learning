# -*- coding:utf-8 -*-


from multiprocessing import Process
import os
from time import sleep


def run_proc(name, age, **kwargs):
    for i in range(100):
        print('子进程运行中，name= %s,age=%d ,pid=%d...' % (name, age, os.getpid()))
        print(kwargs)
        sleep(0.2)

if __name__=='__main__':
    print('父进程开始运行：' + str(os.getppid()))
    p = Process(target=run_proc, args=('test',18), kwargs={"m":20})
    p.start()
    sleep(3)  # 3秒中之后，强制结束子进程
    p.terminate()
