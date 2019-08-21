# -*- coding: utf-8 -*-

# 字符串转化为字节有两种方式
str0 = 'zifuchuan哈哈哈'
print(type(str0))

# 注意：utf-8编码下，汉字占3个字节，可以输出结果查看，
# 哈哈哈一共有九个字节表示，反斜杠代表转移符，双反斜杠才代表一个斜杠
# 第一种
str1 = bytes(str0, encoding='utf-8')
print(str1)

# 第二种
str2 = str0.encode('utf-8')
print(str2)


# 字节转化为字符串有两种方式
bytes0 = b'zifuchuan\xe5\x93\x88\xe5\x93\x88\xe5\x93\x88'
print(type(bytes0))

# 第一种
bytes1 = str(bytes0, encoding='utf-8')
print(bytes1)

# 第二种
bytes2 = bytes.decode(bytes0)
print(bytes2)