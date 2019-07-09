# 协程案例

def simple_coroutine():
    print("->start")
    x = yield
    print("->recived", x)

# 第一步生成一个协程
sc = simple_coroutine()
# 执行一个语句
print(111)
# 预激协程
next(sc)
print(222)
sc.send("Done over")

# 上述代码的执行步骤，参看视频协程的1小时23分钟前后

