# 多线程共享变量

import threading

sum = 0
loopSum = 1000000

def myAdd():
    global sum, loopSum
    # sum初始值是0，循环第一次0+1=1，循环第二次1+1=2，循环第99次等于98+1=99
    for i in range(1, loopSum):
        sum += 1

def myMinu():
    global sum, loopSum
    for i in range(1, loopSum):
        sum -= 1

if __name__ == '__main__':
    myAdd()
    print(sum)
    # 执行myMinu时候，是在print(sum)之后，此时sum的值是99
    # sum=99，第一次循环为99-1=98，第二次98-1=97，第99次为1-1=0
    myMinu()
    print(sum)


# 改写为多线程执行
if __name__ == '__main__':
    print("Starting...{0}".format(sum))

    # 开始多线程实例，多次执行，看看执行结果是否一样
    # 由于t1和t2同时开始，互相调用他们之间的运行结果sum值，
    # 最终完成后的sum值就会一直变化
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # 加减同时执行，最后发现每次的运行结果都不同
    # 多线程共享变量出现测冲突问题
    print("Done...{0}".format(sum))





