# -*- coding:utf-8 -*-

import gevent

def f1(n):
    for i in range(n):
        # gevent.getcurrent()显示当前的协程任务
        print(gevent.getcurrent(), i)
        #用来模拟一个耗时操作，注意不是time模块中的sleep
        gevent.sleep(1)

def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        #用来模拟一个耗时操作，注意不是time模块中的sleep
        gevent.sleep(1)

def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        #用来模拟一个耗时操作，注意不是time模块中的sleep
        gevent.sleep(1)

# spawn传入函数名，函数的参数
print('-----1-----')
g1 = gevent.spawn(f1, 5)
print('-----2-----')
g2 = gevent.spawn(f2, 5)
print('-----3-----')
g3 = gevent.spawn(f3, 5)
print('-----4-----')

# 可以一次加入所有的任务，主进程等待每个任务结束，使用列表传入
# joinall会等待里面所有的任务结束
gevent.joinall([g1, g2, g3])

# 或者使用join等待每个任务执行结束
# g1.join()
# g2.join()
# g3.join()

# 运行结果显示，三个任务都是同时开始的
#
# gevent一大特点就是遇到超时阻塞，就会自动切换任务
# 所有最常用在网页请求中，参考015案例
