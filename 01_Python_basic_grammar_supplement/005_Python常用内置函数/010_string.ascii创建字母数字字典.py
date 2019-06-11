import string

# 创建字母ASCII值
print(string.ascii_uppercase[0:5])
print(string.ascii_lowercase[0:5])
print(string.ascii_letters[0:5])

# 创建一个字母和数字的字典
a = {string.ascii_uppercase[i]:i for i in range(10)}
print(a)