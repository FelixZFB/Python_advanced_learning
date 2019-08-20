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

    for i in range(5):
        p = Process(target=run_proc, args=(str(i),))
        print("Process will start.")
        p.start()
    # join()实现进程间的同步，等待所有子进程运行结束，再运行之后的代码
    p.join()
    print("Process end.")
    # 查看运行结果发现，run_proc结果还没运行出来，循环都已经结束了
    # 循环中所有的Process will start.都已经执行出来了
    # 才开始执行各个子进程



