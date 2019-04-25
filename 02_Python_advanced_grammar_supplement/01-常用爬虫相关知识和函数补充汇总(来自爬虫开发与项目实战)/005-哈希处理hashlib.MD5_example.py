# Python生成MD5

# 方法1：使用hashlib(推荐使用)
import hashlib
text = 'this is a MD5 test' # 用于MD5处理的字符串
m = hashlib.md5() # 生成一个MD5处理的实例
m.update(text.encode('utf-8')) # 将上面字符串传入
md5 = m.hexdigest() # MD5处理之后字符串
print(md5)
print(md5[8:-8]) # python处理后的MD5有256位，只取中间的128位

# 方法1简写形式，推荐上面分步写法
md5=hashlib.md5('this is a MD5 test'.encode('utf-8')).hexdigest()
print(md5)






