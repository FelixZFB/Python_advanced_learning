# -*- coding:utf-8 -*-


class FibIterator(object):
    """斐波那契数列迭代器"""
    def __init__(self, n):
        """
        :param n: int, 指明生成数列的前n个数
        """
        self.n = n
        # current用来保存当前生成到数列中的第几个数了，用来计数
        self.current = 0
        # num1用来保存前一个数，初始值为数列中的第一个数0
        self.num1 = 0
        # num2用来保存后一个数，初始值为数列中的第二个数1
        self.num2 = 1

    def __next__(self):
        """被next()函数调用来获取下一个数"""
        # 该处从计数从0开始，要用小于，如果小于等于就会多生成一个数
        if self.current < self.n:
            # 第一次调用是，num=0
            num = self.num1
            self.num1, self.num2 = self.num2, self.num1+self.num2
            self.current += 1
            return num
        else:
            raise StopIteration

    def __iter__(self):
        """迭代器的__iter__返回自身即可"""
        return self


if __name__ == '__main__':
    # 生成斐波那契数列的前10个数
    fib = FibIterator(10)
    # 调用for循环，取出每一个数
    for num in fib:
        print(num, end=" ") # end是打印结尾，每个数打印末尾空格

# 即使生成10000个数，也会很快生成，因为每次都是调用的迭代器的next方法
# 调用的是方法，而不是保存了大量的数据，再取出数据

# 006案例中，是生成了大量数据，保存在一个列表中，占用了大量内存
# 但是006使用的是while循环生成列表后，nums使用for循环取出就会调用迭代器，就实现了迭代器的功能

# 007案例是用迭代器实现生成数据的方法，缓存中并不会保存每一个数据，保存的是生成数据的方法
# 保存的某个数生成前后的一个状态，底层的实现就是中断的原理，保存栈帧，加载栈帧
