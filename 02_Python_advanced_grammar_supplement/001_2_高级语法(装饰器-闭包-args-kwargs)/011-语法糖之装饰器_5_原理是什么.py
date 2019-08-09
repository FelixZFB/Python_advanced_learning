# 前面已经1234已经讲了装饰器的简单实例
# 那么究竟装饰器的原理是什么？
# 先看下面这个例子：

def deco(func):
    def wrapper():
        print("...开始验证权限...")
        func()
    return wrapper

@deco
def func_a():
    print("...权限验证通过...")

func_a()
# 代码原理及执行循序如下：
# 1. 当运行该程序代码时，执行到@deco时，就会调用deco函数，发现该函数是一个装饰函数，向下继续执行
# 2. 此时，被装饰的函数func_a会作为参数传递给deco函数，即deco中的参数func=func_a
# 3. 然后开始执行内部函数wrapper，里面有一个打印语句，和一个func函数
# 4. func_a作为参数传进来，实际最终执行的是func_a()，但该处并不是把func_a函数下的代码运行出来
# 5. 而是，deco函数返回值是内部函数wrapper，该处返回的是已经加了装饰的func_a函数了
# 6. 原始函数func_a函数的地址已经指向了deco.wrapper的函数地址

# 装饰后的func_a = deco(原始函数的func_a)
# 7. 因此，主代码执行@deco后，再执行func_a()(该func_a已经被装饰了),就会指向deco.wrapper的函数地址
# 8. 主代码执行func_a()，实际代码输出结果就是：执行deco.wrapper函数，先打印出开始权限认证，然后执行func(),
# 9. 也就是被当成参数传进来的原始函数func_a，打印出权限验证通过

# 经过上述步骤，func_a就被装饰了

