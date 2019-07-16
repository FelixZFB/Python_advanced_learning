# 多线程共享变量
# 锁案例
# 共享变量是sum, 锁住sum

import threading

sum = 0
loopSum = 10000000

lock = threading.Lock()

def myAdd():
    global sum, loopSum
    for i in range(1, loopSum):
        # 上锁，申请锁
        lock.acquire()
        sum += 1
        # 释放锁
        lock.release()

def myMinu():
    global sum, loopSum
    for i in range(1, loopSum):
        # 上锁，申请锁
        lock.acquire()
        sum -= 1
        # 释放锁
        lock.release()


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
    # 才会执行下一个程序
    print("Done...{0}".format(sum))





