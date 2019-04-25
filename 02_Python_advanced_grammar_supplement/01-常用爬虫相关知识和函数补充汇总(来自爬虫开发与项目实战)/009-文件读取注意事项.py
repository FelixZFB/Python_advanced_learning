# 文件读取常用方法
# 使用with open语句，读取写入完毕后会自动关闭文件
# read（） 一次将文件内容读取到内存，如果文件过大，会出现内存不足的问题
# read（size）一次最多读取size字节，多次调用读取大文件
# 文本文件使用逐行读取更合理
# readline().每次读取一行的内容
# readlines(),读取所有的内容，按行返回一个列表，for循环取出
# 常用参数（文件访问模式）参考：
# https://blog.csdn.net/u011318077/article/details/86667197

# 一次全部读取
with open(r'009-filename.txt', 'r', encoding='utf-8') as f:
    r1 = f.read()
    print(r1)

# 每次只读取一行
with open(r'009-filename.txt', 'r', encoding='utf-8') as f:
    r2 = f.readline()
    print(r2)
    r3 = f.readline()
    print(r3)

# 按行全部读取为列表
with open(r'009-filename.txt', 'r', encoding='utf-8') as f:
    r4 = f.readlines()
    print(r4)
    for r in r4:
        print(r)
