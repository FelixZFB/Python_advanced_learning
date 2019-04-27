# set()函数使用方法

x = set('world')
y = set('goole')

# 创建一个无序不重复元素集，重复的元素被删除了
print(x)
print(y)

# 交集
print(x & y)
# 并集
print(x | y)
# 差集
print(x - y)

