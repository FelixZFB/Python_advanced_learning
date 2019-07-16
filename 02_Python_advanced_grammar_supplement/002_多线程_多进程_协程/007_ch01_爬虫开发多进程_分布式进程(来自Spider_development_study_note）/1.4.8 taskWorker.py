# coding: utf-8
# 定义具体的任务进程，具体的工作任务是什么

import time, sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager,继承BaseManager,用于后面创建管理器
class QueueManager(BaseManager):
    pass

# 第一步：使用QueueManager注册用于获取Queue的方法名称
# 前面服务进程已经将队列名称暴露到网络中，
# 该任务进程注册时只需要提供名称即可，与服务进程中队列名称一致
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 第二步：连接到服务器,也就是运行服务进程代码的机器
server_addr = '127.0.0.1'
print("Connet to server %s..." % server_addr)
# 创建一个管理器实例，端口和验证口令保持与服务进程中完全一致
m = QueueManager(address=(server_addr, 8001), authkey=b'abc')
# 连接到网络服务器
m.connect()

# 第三步：从网络上获取Queue对象，并进行本地化，与服务进程是同一个队列
task = m.get_task_queue()
result = m.get_result_queue()

# 第四步：从task队列获取任务，并把结果写入到resul队列
for i in range(50):
    try:
        # 前面服务进程向task队列中放入了n,这里取出n
        # n和n相乘，并将相乘的算式和结果放入到result队列中去
        n = task.get(timeout=1) # 每次等待1秒后取出任务
        print("run task %d * %d..." % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1) # 设置睡眠时间，缓慢输出计算结果
        result.put(r)
    except queue.Empty:
        print("task queue is empty.")

# 任务处理结束
print("worker exit.")


