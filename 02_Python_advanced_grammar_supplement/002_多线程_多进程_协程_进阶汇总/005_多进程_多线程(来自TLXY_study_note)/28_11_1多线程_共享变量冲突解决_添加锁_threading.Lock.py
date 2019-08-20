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
    print(sum)

def myMinu():
    global sum, loopSum
    for i in range(1, loopSum):
        # 上锁，申请锁
        lock.acquire()
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

# 和28_11运行结果对比发现，add加完之后的结果并不是9999999
# 但是最终结果减完还是0
# 上面代码执行顺序是：add先加，获得锁，释放锁，然后minu再减，获得锁，释放锁
# t1和t2线程依次交换执行，整个过程保持同步，所以最后结果还是0
# 但是上面其实还是每次只有一个线程在运行


# 锁阻止了多线程并发执行（一个线程的锁执行时候，另外一个线程的锁必须等待，
# 此时CPU的多核就存在浪费，没有利用起来实现多并发）







