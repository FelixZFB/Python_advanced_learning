# -*- coding:utf-8 -*-


import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(1)
            msg = "I'm "+self.name+' @ '+str(i) #name属性中保存的是当前线程的名字
            print(msg)


if __name__ == '__main__':
    t = MyThread()
    t.start()

# 线程类继承，必须重写run函数，run函数下面就是线程要具体执行的内容
# 相当于threading.Thread(target=XXX)传入的函数名
# 创建自定义的类对象后，直接继承了父类的start方法
# 调用start方法，就会自动调用类中的run方法

# 要传入参数，参考011，需要加入__init__函数，传入参数