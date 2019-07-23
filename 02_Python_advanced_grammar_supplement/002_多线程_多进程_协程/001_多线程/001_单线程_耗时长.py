#coding=utf-8
import time
import threading

def saySorry():
    print("亲爱的，我错了，我能吃饭了吗？")
    time.sleep(5)

if __name__ == "__main__":
    for i in range(5):
        saySorry()

# 单线程每5秒执行一次，下一个循环执行时候需要等待上一个saySorry()执行完毕
# 然后才开始下一个循环中的saySorry()，全部执行完需要25秒