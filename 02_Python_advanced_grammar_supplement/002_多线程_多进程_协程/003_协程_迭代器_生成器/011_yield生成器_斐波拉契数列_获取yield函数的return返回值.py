# -*- coding:utf-8 -*-


def fib_generator(all_num):
    """斐波那契数列生成器"""

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
        yield num1
        num1, num2 = num2, num1+num2
        current_num += 1
    return 100


if __name__ == '__main__':
    # 生成斐波那契数列的前10个数
    fib = fib_generator(10)
    while True:
        try:
            print(next(fib))
        except Exception as e:
            print(e)


# 先next取出所有的值，最后出现异常时候，才返回函数中return的返回值
# 运行以下停止，结果向上面滚动才能看见
