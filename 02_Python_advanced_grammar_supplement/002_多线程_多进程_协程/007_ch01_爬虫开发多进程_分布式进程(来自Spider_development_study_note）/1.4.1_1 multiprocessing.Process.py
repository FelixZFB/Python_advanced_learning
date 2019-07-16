import os
from multiprocessing import Process

# 子进程要执行的代码
def run_proc(name):
    # 获取子进程的进程识别码
    print("Child process %s (%s) Running..." % (name, os.getpid()))

if __name__ == '__main__':
    # 获取父进程的进程识别码
    print("Parent process %s." % os.getppid())
    # 创建10个子进程
    for i in range(10):
        p = Process(target=run_proc, args=(str(i),))
        print("Process will start.")
        p.start()
    # join()实现进程间的同步，等待所有子进程运行结束，再运行之后的代码
    p.join()
    print("Process end.")
    # 可以和1.4.1中只创建了5个子进程对比，主程序（父进程）按着自己的节奏执行
    # 子进程开始执行时，print("Process will start.")属于父进程，父进程都要执行完毕了
    # 可以多次运行该程序，可以发现，子程序并不一定是按照顺序执行的




