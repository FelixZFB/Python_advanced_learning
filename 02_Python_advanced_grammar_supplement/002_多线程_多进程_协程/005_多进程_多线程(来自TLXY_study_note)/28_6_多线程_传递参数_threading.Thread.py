# 多线程实例
# 多线程传递参数
# 包threading

import time
import threading

# 单线程实例

def loop1(in1):
    # ctime得到当前的时间
    print("Start loop 1 at: ", time.ctime())
    print("我是参数", in1)
    # 睡眠一定时间，单位是秒
    time.sleep(2)
    print("End loop 1 at: ", time.ctime())

def loop2(in1, in2):
    # ctime得到当前的时间
    print("Start loop 2 at: ", time.ctime())
    print("我是参数", in1, "和参数", in2)
    # 睡眠一定时间，单位是秒
    time.sleep(3)
    print("End loop 2 at: ", time.ctime())

def main():
    print("Starting at: ", time.ctime())
    # 生成threading.Thread()实例
    t1 = threading.Thread(target=loop1, args=("Felix",))
    t1.start()
    t2 = threading.Thread(target=loop2, args=("Fang", "Bai"))
    t2.start()
    # time.sleep(6)知道上面的程序时间，手动添加等待时间
    # 使用join()函数，等待多线程执行完毕，在执行之后的代码,替代上面手动等待的功能
    t1.join()
    t2.join()
    print("All done at: ", time.ctime())



if __name__ == '__main__':
    main()






