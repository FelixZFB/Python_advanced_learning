# 两个装饰器函数执行顺序

def deco1(func):
    print("001装饰器开始对函数进行装饰")
    def wrapper():
        print("001装饰器内函数开始执行")
        return " (001) " + func() + " (001) "
    return wrapper

def deco2(func):
    print("002装饰器开始对函数进行装饰")
    def wrapper():
        print("002装饰器内函数开始执行")
        return " [002] " + func() + " [002] "
    return wrapper

@deco2
@deco1
def func_a():
    print("...003原始函数终于执行了...")
    return "Hello Python Decorator"

ret = func_a()
print(ret)

print("\n--------------------------\n")
print(type(func_a))
print(type(ret))
print(func_a)

# 上面函数的执行顺序是,主代码运行后,依次运行@deco2,@deco1：
# 1. 运行主代码，首先运行到@deco2时，发现是一个装饰器函数，需要对后面的函数进行装饰
# 2. 因此向下执行寻找deco2中的参数func，但是下一行代码是@deco1，并不是一个函数名，而又是一个装饰器函数
# 3. 此时，@deco2暂时执行，执行接下来的装饰器@deco1,然后向下执行找到函数名func_a
# 4. func_a作为参数传给装饰器@deco1，@deco1开始执行，从而打印出：001装饰器开始对原始函数进行装饰
# 5. 然后@deco1内部函数开始对func_a进行装饰，装饰之后，deco1返回值为内函数wrapper，
# 6. 此时，原始函数func_a已经指向了deco1的内函数wrapper的地址，即func_a = deco1.wrapper
# 7. 然后又返回继续执行@deco2，把新的func_a(@deco1装饰之后的func_a)作为参数传个deco2函数
# 8. 执行deco2函数，从而打印出：002装饰器开始对函数进行装饰，
# 9. 然后@deco2内部函数开始对新func_a进行装饰，装饰之后，deco2返回值为内函数wrapper，
# 10. 此时，新函数func_a已经又指向了deco2的内函数wrapper的地址，即func_a = deco2.wrapper

# 经过上述步骤，@deco2和@deco1都已经运行,并且func_a函数已经被两个函数进行了装饰

# 11. 继续执行代码 ret = func_a(),即运行原始函数func_a函数
# 12. 但是，func_a经过装饰后，最后指向的是deco2.wrapper，从而运行deco2.wrapper函数
# 13. 因此打印出：002装饰器内函数开始执行，同时继续执行代码：return " [002] " + func() + " [002] "
# 14. 即返回一个" [002] " + func() + " [002] "，此时func()返回值的最外层已经被装饰002
# 15. 语句中的func()执行的时候寻找到的是func_a的上一级地址deco1.wrapper(deco2.wrapper地址已经使用过了)
# 16. 上面14返回值中的func()即deco1.wrapper运行后的返回值：" (001) " + func() + " (001) "
# 17. 因此deco2.wrapper函数返回的实际是：" [002] " + " (001) " + func() + " (001) " + " [002] "
# 18. deco1.wrapper运行时，首先打印出：001装饰器内函数开始执行，
# 19. 同时继续执行代码：return " (001) " + func() + " (001) "
# 16. 这时语句中的func()才是指向的原始函数func_a的地址，执行原始函数func_a,打印出：...003原始函数终于执行了...
# 17. 原始函数func的返回值是："Hello Python Decorator"
# 18. 因此最终func_a函数运行后的返回值是：" [002] " + " (001) " + "Hello Python Decorator" + " (001) " + " [002] "
# 19. 最后执行print(ret)即打印出经过装饰之后func_a()函数的返回值

# 总之，装饰器装饰的时候，从最靠近原始函数开始进行装饰，逐级向外进行(外函数)，
# 所有装饰函数装饰结束后，再执行原始函数，此时原始函数指向的是最后一个装饰器内函数的地址，
# 内函数又外外面的装饰器开始执行，逐级向里面执行（内函数），所有内函数开始执行完了，最后开始执行原始函数下的代码
# 先里后外，再外后里，最后原始

print("\n--------------------------")
print(" [002] " + " (001) " + "Hello Python Decorator" + " (001) " + " [002] ")