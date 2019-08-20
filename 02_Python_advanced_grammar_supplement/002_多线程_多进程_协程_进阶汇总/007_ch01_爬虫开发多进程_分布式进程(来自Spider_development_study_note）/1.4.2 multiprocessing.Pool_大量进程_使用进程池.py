import os, time, random
from multiprocessing import Pool

# 创建子进程具体执行的内容
def run_task(name):
    print("Task %s (pid = %s) is running..." % (name, os.getpid()))
    # random.random()生成0和1之间的随机浮点数float
    f = random.random() * 3
    time.sleep(f)
    print(f)
    print("Task %s end." % name)

if __name__ == '__main__':
    # 获取下面一行代码的进程代码
    print("Current process %s." % os.getpid())
    # 创建一个容量为3的进程池,每次同时运行的进程只能是3个
    # p = Pool() 未传入参数，则默认是CPU核数，可以发现同时进行了4个任务
    p = Pool(processes=3)
    # 向进程池中添加6个任务
    for i in range(6):
        # 使用apply_async创建进程
        p.apply_async(run_task, args=(i,))
    print("Waiting for all subprocesses done...")
    # 关闭进程池，关闭后p不再接收新的请求
    p.close()
    # 等待所有进程执行结束，再继续执行主代码
    # 等待po中所有子进程执行完成，必须放在close语句之后
    p.join()
    print("All subprocesses done.")
    # 查看运行结果发现，同时开始的只有三个进程
    # 同时结束一个进程之后，开始一个新的进程
    # 新开始的进程使用的是原来的进程
    # 结束和开始的进程的进程代码pid是一样的
