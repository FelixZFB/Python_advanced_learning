# -*- coding:utf-8 -*-

# 全部的全局变量都放在一个字典中
glo = globals()
print(type(glo))
# print(glo)
print('*' * 50)

# __builtins__对应的就是内置模块
# glo是一个字典，我们使用字典的键取出对应的值
# 键__builtins__对应的值就是模块builtins，<module 'builtins' (built-in)>
# 上面的globals,ctrl然后查看源码，globals就是位于builtins.py中
print(glo['__builtins__'])
print('*' * 50)

# __dict__可以查看模块或类的所有内置函数
# 取出所有内置模块的函数
bul = glo['__builtins__'].__dict__
print(bul)
print('*' * 50)

# __builtins__里面所有函数又是一个字典
print(bul['print'])
print('*' * 50)

# 查看内置模块的所有函数，里面就有print等等函数
# 'print': <built-in function print>,
# 'TimeoutError': <class 'TimeoutError'>,
# 'open': <built-in function open>,
# 'quit': Use quit() or Ctrl-Z

# 当我们调用一个变量时候，首先在全局变量里面找，如果里面没有
# 就进built_in内置函数里面找
# 如果还没找到，就报错