# -*- coding:utf-8 -*-


import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            # 等待1秒后执行
            time.sleep(3)
            # name属性中保存的是当前线程的名字
            msg = "I'm "+self.name+' @ '+str(i)
            print(msg)


def test():
    # 使用for循环，创建5个子线程
    for i in range(5):
        t = MyThread()
        t.start()


if __name__ == '__main__':
    test()

# test函数循环5次，for循环第一次时：
# 创建类对象，创建了第一个线程Thread-1，调用类中的run函数
# run函数中的for循环第一次，等待3秒后，执行语句结果I'm Thread-1 @ 0
# 然后又等待3秒后执行出I'm Thread-1 @ 1，又等待3秒最后一次结果：I'm Thread-1 @ 2

# 但是test中的for循环时没有等待时间的，即for循环5次瞬间就执行完毕了
# 然后同时启动了5个子线程，5个子线程都开始run中的第一次循环
# 单从结果可以发现5个子线程开始时间，并不是按创建顺序保持一致的
# 多线程执行顺序是不固定的
# 多次运行，发现顺序会发生变化

# I'm Thread-1 @ 0
# I'm Thread-2 @ 0
# I'm Thread-3 @ 0
# I'm Thread-5 @ 0
# I'm Thread-4 @ 0

# I'm Thread-2 @ 1
# I'm Thread-1 @ 1
# I'm Thread-3 @ 1
# I'm Thread-4 @ 1
# I'm Thread-5 @ 1

# I'm Thread-1 @ 2
# I'm Thread-2 @ 2
# I'm Thread-3 @ 2
# I'm Thread-4 @ 2
# I'm Thread-5 @ 2