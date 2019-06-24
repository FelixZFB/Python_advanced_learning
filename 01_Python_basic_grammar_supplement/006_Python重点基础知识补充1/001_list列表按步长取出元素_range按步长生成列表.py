
a = range(1, 10, 2)
print(list(a))

# 生成0到99的列表，刚刚100个元素
b = list(range(100))
print(b)
print(len(b))

# 我们从0开始，按步长5取出数字，
# 即第一次取0，然后间隔5取出第六个元素5
# 取出结果0 0+5 0+5+5  0+5+5+5 。。。
c = b[::5]
print(c)
print(len(c))

d = b[::3]
print(d)
print(len(d))