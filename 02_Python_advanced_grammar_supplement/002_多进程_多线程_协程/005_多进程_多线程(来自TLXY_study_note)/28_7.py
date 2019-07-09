# 非守护线程实例

import time
import threading

def fun():
    print("Start fun")
    time.sleep(2)
    print("end fun")

print("Main thread")

# 设置一个多线程
t1 = threading.Thread(target=fun, args=())
t1.start()

time.sleep(1)
print("Main thread end")
