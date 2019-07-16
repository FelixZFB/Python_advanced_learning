# 多线程类继承实例

import time
import threading

# 1.类继承多线程父类
class MyThread(threading.Thread):
    def __init__(self, arg):
        super(MyThread, self).__init__()
        self.arg = arg

    # 2.必须重写run函数，run函数代表的是真正执行的功能
    # 干活的都是run,所有执行的任务都写在run下面
    def run(self):
        time.sleep(2)
        print("The args for this class is {0}".format(self.arg))

for i in range(5):
    t = MyThread(i)
    t.start()
    # print(threading.enumerate())
    t.join()

# 最后执行的主线程
print("Main thread is done!")

