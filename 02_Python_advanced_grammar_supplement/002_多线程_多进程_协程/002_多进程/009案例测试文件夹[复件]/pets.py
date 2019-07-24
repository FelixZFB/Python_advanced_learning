# coding=utf-8
# 采用while循环，remove函数，删除列表中所有的cat
# 当cat还在pets列表中时，while函数为True，就会不断循环运行

pets = ['dog', 'cat', 'snake', 'pig', 'cat', 'goldfish', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
