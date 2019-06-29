# -*- coding:utf-8 -*-

# 参考我的博文(归纳汇总了yield生成器):
# Python3中yield理解与使用（一遍就懂系列，绝不反驳）
# https://blog.csdn.net/u011318077/article/details/93749143

# 如果你还没有对yield有个初步分认识，那么你先把yield看做“return”，
# 这个是直观的，它首先是个return，普通的return是什么意思，
# 就是在程序中返回某个值，返回之后程序就不再往下运行了。
# 看做return之后再把它看做一个是生成器（generator）的一部分
# （带yield的函数才是真正的迭代器），好了，如果你对这些不明白的话，
# 那先把yield看做return,然后直接看下面的程序，你就会明白yield的全部意思了


# 一个普通函数：
def foo():
    print('Starting.....')
# 调用函数，直接执行语句
g = foo()
print("*" * 100)

# 包含yield关键字，就变成了生成器函数
# 调用函数并不会执行语句
def foo():
    print('Starting.....')
    while True:
        res = yield 4
        print("res:", res)

# 下面调用函数并没有执行，可以先将后面的语句注释掉
# 逐行运行代码观察效果
g = foo()
print("第一次调用执行结果：")
print(next(g))
print("*" * 100)

print("第二次调用执行结果：")
print(next(g))
print("*" * 100)

print("第三次调用执行结果(已经开始了While循环)：")
print(next(g))
print("*" * 100)

# 下面解释代码运行顺序，相当于代码单步调试()：
# 1.程序开始执行以后，因为foo函数中有yield关键字，所以foo函数并不会真的执行，
# 而是先得到一个生成器g(相当于一个对象)，函数的一个状态，函数相当于暂停了

# 2.执行第一次调用，直到遇到next方法，foo函数正式开始执行，先执行foo函数中的print方法，然后进入while循环

# 3.程序遇到yield关键字，然后把yield想想成return,return了一个4之后，程序停止，
# 但是，程序只是返回了一个值4，并没有执行将4赋值给res操作，此时next(g)语句执行完成，
# 所以第一次调用后的结果有两行（第一个是while上面的print的结果,第二个是return出的结果）
# 也就是执行print(next(g))先调用函数，最后打印出了返回值4
#
# 4.程序执行print("*" * 100)，输出100个*
#
# 5.执行第二次调用，又开始执行下面的print(next(g)),这个时候和上面那个差不多，不过不同的是，
# 这个时候是从刚才那个next程序停止的地方开始执行的，也就是要执行res的赋值操作语句，
# 这时候要注意，yield 4返回值4后就停止了，并没有赋值给前面的res, （因为刚才那个是return出去了，
# 并没有给赋值操作的左边传参数），此时代码实际是从print("res:", res)开始执行，
# 这个时候res赋值是空，是None,所以接着下面的输出就是res:None,
#
# 6.程序会继续在while里执行，又一次碰到yield,这个时候同样return出4，然后程序停止，print函数输出的4就是这次return出的4.
#
# 7. 接着第三次调用,不断进行while循环，之后的结果都一样

# 到这里你可能就明白yield和return的关系和区别了，带yield的函数是一个生成器，
# 而不是一个函数了，这个生成器有一个函数就是next函数，next就相当于“下一步”生成哪个数，
# 这一次的next开始的地方是接着上一次的next停止的地方执行的，
# 所以调用next的时候，生成器并不会从foo函数的开始执行，只是接着上一步停止的地方开始，
# 然后遇到yield后，return出要生成的数，此步就结束。


# 上面的foo()就是一个生成器函数，当一个生成器函数调用yield，生成器函数的“状态”会被冻结，
# 所有的变量的值会被保留下来，下一行要执行的代码的位置也会被记录，就是yield这行代码结束的位置
# 直到再次调用next()。一旦next()再次被调用，生成器函数会从它上次离开的地方开始。
# 如果永远不调用next()，yield保存的状态就被无视了。


# generator是用来产生一系列值的，yield则像是generator函数的返回结果，(yield也可以看似return)
# yield唯一所做的另一件事就是保存一个generator函数的状态
# （yield和return的区别，return执行后会继续执行后面的代码，但是yield会停止之后的代码继续执行，
# 注意，只是停止生成器函数内部的代码，生成器函数外部代码不受影响）
# generator就是一个特殊类型的迭代器（iterator）和迭代器相似，我们可以通过使用next()来从generator中获取下一个值

# yield访问的两种方法：调用next()或者send()函数，使用for循环



