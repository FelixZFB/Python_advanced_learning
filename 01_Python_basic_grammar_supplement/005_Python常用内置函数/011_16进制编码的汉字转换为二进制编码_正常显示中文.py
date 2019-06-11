# 16进制的汉字编码（属于python的byte类型）
# 下面可以采用两种方式转换可以正常显示的中文字符
# 下面转码过程，必须原编码是汉字转换过来的才行

# 16进制的汉字编码
bytes1 = b'\xe5\xae\x89\xe5\x85\xa8\xe5\x8d\x9a\xe5\xae\xa2'

# 方法1：
str1 = str(bytes1, encoding='utf-8')
print(str1)

# 方法2：
str2 = bytes.decode(bytes1)
print(str2)
