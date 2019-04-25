# sorted() 函数对所有可迭代的对象进行排序操作

# sort 与 sorted 区别：
# sort是应用在list上的方法，sorted可以对所有可迭代的对象进行排序操作。
# list的sort方法返回的是对已经存在的列表进行操作，无返回值，
# 而内建函数sorted方法返回的是一个新的list，而不是在原来的基础上进行的操作
# reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）

a = [5, 7, 6, 3, 4, 1, 2]

# 保留原列表，生成一个新列表，默认升序排列
b = sorted(a) # 升序
c = sorted(a, reverse=True) # 降序
print(a)
print(b)
print(c)


# 按照绝对值排序，由大到小排列
l = [3, 45, -7, 23, 54, -43, -78, 63, 24, 67, -120, 5, 6, 9, 8]
al = sorted(l, key=abs, reverse=True)
print(al)