# 非守护线程实例

import time
import threading

def fun():
    print("Start fun")
    time.sleep(3)
    print("end fun")

print("Main thread")

# 设置一个多线程
t1 = threading.Thread(target=fun, args=())
t1.start()

time.sleep(1)
print("Main thread end")

# 非守护线程，主代码已经执行结束
# 子线程t1还是会继续执行，直到子线程代码执行结束，整个程序才算结束
