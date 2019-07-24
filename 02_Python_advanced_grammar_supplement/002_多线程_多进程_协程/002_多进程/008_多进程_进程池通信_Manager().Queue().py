# -*- coding:utf-8 -*-

# 修改import中的Queue为Manager
from multiprocessing import Manager,Pool
import os,time,random


# 存入数据到队列中
def reader(q):
    print("reader子进程启动(%s),父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到消息：%s" % q.get(True))
        time.sleep(1)


# 从队列中读取数据
def writer(q):
    print("writer子进程启动(%s),父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in "ABCDEFG":
        q.put(i)


def main():
    print("主进程(%s) start" % os.getpid())

    # 此处注意和进程通信multiprocessing.Queue()的区别
    # 使用multiprocessing中Manager()中的Queue()
    q = Manager().Queue()
    po = Pool()
    po.apply_async(writer, (q,))

    # 等待3秒，先让上面的任务向Queue存入数据，然后再让下面的任务开始从中取数据
    time.sleep(3)

    po.apply_async(reader, (q,))
    # 关闭进程池
    po.close()

    # 等待子进程结束
    po.join()

    print("主进程(%s) End" % os.getpid())


if __name__=="__main__":
    main()