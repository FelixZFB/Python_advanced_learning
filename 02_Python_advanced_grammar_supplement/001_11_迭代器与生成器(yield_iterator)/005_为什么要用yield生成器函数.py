# -*- coding:utf-8 -*-

# 为什么用这个生成器，是因为如果用List的话，会占用更大的空间，
# 比如说取0,1,2,3,4,5,6............1000
# 下面举例，只取到10,1000结果太长了
for n in range(10):
    a=n
    print(a) # 相当于return a
print("*" * 100)

# 生成器实现
def foo(num):
    print("starting...")
    while num<10:
        num=num+1
        yield num

for n in foo(0):
    print(n)

# 上面for循环执行过程(自动调用的next函数)(参考001案例中详细解释)：
# 调用可迭代对象的__iter__方法返回一个迭代器对象（iterator）
# 不断调用迭代器的__next__方法返回元素
# 直到迭代完成后，处理StopIteration异常


# 上面两种方式都可以得到0-10之间的数字，但是占用内存不同：
# 第一种直接使用for循环：
# for循环运行时，所有的0-10之间数字都存在内存之中
# 需要消耗极大的内存，如果数字是10000，可能for循环直接就将电脑内存消耗完了
# 后面的代码，其它程序就无内存可用了

# 第二种，虽然也是for循环，但是内部加入了yield：
# for循环每次调用时，yield生成器(generator)能够迭代的关键是它有一个next()方法，
# 工作原理就是通过重复调用next()方法，直到捕获一个异常,for循环自动结束
# 每次执行到yield，因为底层的实现就是中断的原理，保存栈帧，加载栈帧。
# 每次执行结束内存释放，执行的时候占用一点内存，消耗的内存资源就很少


# yield的好处：
# 1. 不会将所有数据取出来存入内存中；而是返回了一个对象；可以通过对象获取数据；用多少取多少，可以节省内容空间。
# 2. 除了能返回一个值，还不会终止循环的运行；
# 3. 每次执行到yield，因为底层的实现就是中断的原理，保存栈帧，加载栈帧。
# 4. 每次执行结束内存释放，执行的时候占用一点内存，消耗的内存资源就很少

# 通常yield都是放在一个函数中，该函数就变成了生成器函数，该函数就变成了一个迭代器
# 生成器函数一般都是通过for循环调用，for循环自带next方法

# 爬虫经常使用到yield request，yield item
# 可以参考Spider_development_study_note中ch12中cnblogSpider和shtspider
# 爬虫主程序中，yield直接写在for循环内部
# parse函数内部有for循环，有request，
# 调用了parse_body(代码中有yield item),for循环最后是yield request
# 爬虫代码运行时候，for循环自动调用next方法，yield就会不断执行，直到爬取结束
# 使用yield也会大大减少内存的消耗



# 通常的for...in...循环中，in后面是一个数组，这个数组就是一个可迭代对象，
# 类似的还有链表，字符串，文件。它可以是mylist = [1, 2, 3]，也可以是mylist = [x*x for x in range(3)]。

# 补充：
# 注意的是python3时已经没有xrange()了，在python3中，
# range()就是xrange()了，你可以在python3中查看range()的类型，
# 它已经是个<class 'range'>了，而不是一个list了，毕竟这个是需要优化的
print("*" * 50)
print(type(range(10)))