# -*- coding:utf-8 -*-


def fib_generator(all_num):
    """斐波那契数列生成器"""
    print('-----1-----')
    # current_num用来保存当前生成到数列中的第几个数了，用来计数
    current_num = 0
    # num1用来保存前一个数，初始值为数列中的第一个数0
    num1 = 0
    # num2用来保存后一个数，初始值为数列中的第二个数1
    num2 = 1

    # 该处从计数从0开始，要用小于，如果小于等于就会多生成一个数
    # 当前生成的个数小于给定的个数就不断生成
    while current_num < all_num:
        # 第一次调用是，current_num=0, num1=0
        print('-----2-----')
        yield num1
        print('-----3-----')
        num1, num2 = num2, num1+num2
        current_num += 1
        print('-----4-----')

# 通过上面的1234可以查看函数每次运行了哪些代码，在哪里终止
# 调用函数是并不会执行，而是生成了一个yield生成器对象
fib = fib_generator(3)

# 使用next函数访问生成器对象
# 第一次调用
print('*' * 50)
print(next(fib))
print('*' * 50)

# 第二次调用
print(next(fib))
print('*' * 50)

# 第三次调用
print(next(fib))
print('*' * 50)

# 第四次调用，已经没有值可以访问了，抛出异常StopIteration
print(next(fib))
print('*' * 50)

# 运行结果可以发现，每次运行到yield语句后，函数暂停
# 再次调用next函数时，接着暂停之后的代码继续运行

# yield函数执行步骤参考001_11_迭代器与生成器(yield_iterator)文件中相关案例

