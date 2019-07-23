# 多线程共享变量
# 锁案例
# 共享变量是sum, 锁住sum

import threading

sum = 0
loopSum = 10000000

lock = threading.Lock()

def myAdd():
    global sum, loopSum
    # 上锁，申请锁
    lock.acquire()
    for i in range(1, loopSum):
        sum += 1
    # 释放锁
    lock.release()
    print(sum)

def myMinu():
    global sum, loopSum
    # 上锁，申请锁
    lock.acquire()
    for i in range(1, loopSum):
        sum -= 1
    # 释放锁
    lock.release()
    print(sum)


if __name__ == '__main__':
    myAdd()
    print(sum)
    myMinu()
    print(sum)

# 改写为多线程执行
if __name__ == '__main__':
    print("Starting...{0}".format(sum))

    # 开始多线程实例，看看执行结果是否一样
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # 加锁之后，只有第一个程序执行完毕，释放锁之后
    # 即上面的加循环执行完毕，才会开始执行减循环
    # 才会执行下一个程序
    print("Done...{0}".format(sum))

# t1.start()先上锁了，只有t1的锁释放了
# t2.start()才会获得锁，然后t2线程开始

# 但是上面上锁的范围很多，直接将t1的for循环锁死了，for循环只有运行结束了
# t2线程才会开始，相当于同时执行的只有一个线程

# 上面的锁范围较大，实际是两个线程依次运行，并不是并发进程，执行时间较长
# 下面将锁放到for循环里面，查看28_11_1案例





