
# 列表前后元素组成一个新列表
l = ['a', 'b', 'c', 'd', 'e','f']

l1 = zip(l[:-1],l[1:])
for i in l1:
    print(i)

# 前面加一个*,列表的每一个元素当做一个迭代对象
# 生成一个新的元组列表
nums = ['flower','flow','flight']
for i in zip(*nums):
    print(i)