# 序列化操作案例
# 变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling

# coding: utf-8
import pickle

# 序列化写入一个列表
a = [20, 'Felix', 'Zhang']

# 序列化写入上面的数据
with open('006-pickle_example.txt', 'wb') as f:
    pickle.dump(a, f)

# 反序列化，读取文件
with open('006-pickle_example.txt', 'rb') as f:
    a = pickle.load(f)
    print(a)