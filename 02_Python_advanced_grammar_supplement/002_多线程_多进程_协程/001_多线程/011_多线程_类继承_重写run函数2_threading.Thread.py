# -*- coding:utf-8 -*-

# 多线程类继承实例

import time
import threading

# 1.类继承多线程父类
class MyThread(threading.Thread):
    def __init__(self, arg):
        super(MyThread, self).__init__()
        self.arg = arg
        # self.login()

    # 2.必须重写run函数，run函数代表的是真正执行的功能
    # 干活的都是run,所有执行的任务都写在run下面
    def run(self):
        time.sleep(2)
        print("The args for this class is {0}".format(self.arg))

    def login(self):
        print('我是一个方法')


# 使用for循环，创建5个子线程
for i in range(5):
    t = MyThread(i)
    t.start()
    # print(threading.enumerate())
    # 等待子线程执行结束，再打印下面主线程的语句
    t.join()

# 最后执行的主线程
print("Main thread is done!")

# 如果MyThread类里面还想写别的方法，先写方法
# 然后使用self.方法名加入的__init__方法中
# 最后run函数调用是，会自动调用__init__包含的方法
# 不能直接使用t.方法名调用，这样调用就变成了普通方法了，不是多任务了

# 上面解释存在问题：
# __init__方法在创建类时，就会自动执行
# 就是只要创建了t = MyThread(i)类，就自动执行了__init__方法中的self.login()