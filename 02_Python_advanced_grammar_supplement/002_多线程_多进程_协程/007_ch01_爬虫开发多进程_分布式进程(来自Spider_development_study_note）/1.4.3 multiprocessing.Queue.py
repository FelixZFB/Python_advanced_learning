# 在父进程中创建三个子进程
# 多个进程之间的通信使用Queue
# 两个子进程向Queue中写入数据
# 一个子进程从Queue中读取数据

from multiprocessing import Process, Queue
import os, time, random

# 先定义写入和读取的方法
# 写数据进程, 执行的代
# Queue实例的put方法，向进程队列中写入url，按循序写入
def proc_write(q, urls):
    print("Process(%s) is writing..." % os.getpid())
    for url in urls:
        q.put(url)
        print("Put %s to queue..." % url)
        # time.sleep(random.random())
        time.sleep(10)


# 读数据进程, 执行的代码
# get方法从进程队列中取出数据，按循序取出
def proc_read(q):
    print("Process(%s) is reading..." % os.getpid())
    while True:
        url = q.get(True)
        print("Get %s from queue." % url)


# 定义主程序
if __name__ == '__main__':
    # 父进程创建Queue,并传给各个子进程
    # 创建一个Queue的实例
    q = Queue()
    # 传入两个参数，q和一个URL列表就是上面的urls
    proc_writer1 = Process(target= proc_write, args=(q,['url_1', 'url_2', 'url_3']))
    proc_writer2 = Process(target= proc_write, args=(q,['url_4', 'url_5', 'url_6']))
    proc_reader = Process(target=proc_read, args=(q,))
    # 启动子进程proc_writer,写入
    proc_writer1.start()
    proc_writer2.start()
    # 启动子进程proc_reader,读取
    proc_reader.start()
    # 等待proc_writer进程结束
    proc_writer1.join()
    proc_writer2.join()
    # proc_reader进程是死循环，无法等待结束，强行终止
    proc_reader.terminate()

# 查看运行结果
# 先启动了写入函数的进程，运行了两个写入函数，
# 同时分别向队列中写入了url列表中的第一个url，先存入1和4
# 然后读取函数启动了，一起取出了前面写入的两个url，取出了1和4
# 然后执行写入2和5，取出2和5
# 写入函数的两个进程执行结束，但是取出函数一直是真，会不断循环
# 但是队列中已经没有url可以取出了，程序不会停止，因此加上的强制终止代码
# 强制终止代码去掉，程序不会停止



