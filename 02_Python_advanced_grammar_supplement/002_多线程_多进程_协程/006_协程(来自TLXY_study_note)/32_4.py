# 协程案例2

def simpel_coroutine(a):
    print("start")
    b = yield a
    print("recived", a, b)
    c = yield a + b
    print("recived", a, b, c)

# 主程序，先生成一个协程
# 将5赋值给a
sc = simpel_coroutine(5)
# 预激协程，执行打印开始，执行yield,将a的值返回
# a返回的值是5，返回后赋值给aa，协程暂停
aa = next(sc)
# 打印出a的值5
print(aa)
# 继续执行协程，6赋值给b,接着执行打印语句
# 打印出5和6，然后执行yield，返回a+b的值
# 返回的值给bb,协程然后暂停
bb = sc.send(6)
print(bb)
# 类似，7赋值给c,然后执行打印，然后再执行没有了
# 所以返回一个StopIteration的错误
cc = sc.send(7)
print(cc)
