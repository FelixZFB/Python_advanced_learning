# 注意：元组是不可修改对象，如果元组里面元素也是不可修改对象，
# 使用浅拷贝和深拷贝，都只是复制引用，类似于赋值

# 注意：但是，元组里面的对象是可修改对象，比如列表，字典，
# 则深拷贝则是深拷贝，地址会发生变化，浅拷贝还是复制引用

import copy

# 1. 元组内部为不可修改对象
a = (1, 2)
b = copy.copy(a)
c = copy.deepcopy(a)
print(id(b))
print(id(c))

# 2. 元组内部为可修改对象
a = [1, 2]
b = [3, 4]
c = (a, b)
d = copy.copy(c)
e = copy.deepcopy(c)
print()
print(id(c))
print(id(d))
print(id(e))
a.append(5)
print(d)
print(e)
# 输出结果不同，深拷贝是所有拷贝，地址已发生变化，但是浅拷贝还是仅复制了引用