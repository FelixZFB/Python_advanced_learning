# 闭包使用注意事项

# 1. 闭包中是不能修改外部作用域的局部变量的
def outer():
    m = 0
    def inner():
        m = 1
        print(m)
    print(m)
    inner()
    print(m)
outer()
print('*' * 50)

# 运行结果发现，最后一个m还是0
# 闭包函数不会修改外部作用域局部变量的值

# 2. 闭包中常见的一个错误
def outer():
    m = 1
    def inner():
        m = m + 1
        return m
    return inner
res = outer()
# print(res())
print(res.__name__)
print('*' * 50)
# print(res())
# 本来是想运行之后，m变成2，但是运行并没有返回2
# 上部代码右边的m已经标红，鼠标方上去，提示未找到参考即未找到变量引用
# 执行res()时会出现错误，执行闭包函数时，python会导入全部的闭包函数体inner()
# 来分析其的局部变量，python规则指定所有在赋值语句左面的变量都是局部变量，
# 则在闭包inner()中，变量m在赋值符号"="的左面，被python认为是inner()内部函数中的局部变量。
# 再接下来执行print(res())时，程序运行至m = m + 1时，因为先前已经把m归为inner()内部中的局部变量，
# 所以python会在inner()中去找在赋值语句右面的m的值，不会找到外部函数中的m，结果找不到值，就会报错

# 上面代码修改一下，上述问题就可以解决
def outer():
    m = 1
    def inner():
        # 指定m不是闭包的局部变量,inner中的m就可以找到外部的m
        nonlocal m
        m = m + 1
        return m
    return inner
res = outer()
print(res.__name__)
print(res())

# 我们发现上面错误代码中outer中的m是灰色，inner中的m不会找到他
# 修改后代码,内部的m就可以找到外部的m，所有m最终结果就是2

