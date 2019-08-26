# __str__ 和 __repr__的区别

class A():
    def __str__(self):
        return "__str__"

a = A()
print(a)

class A():
    def __repr__(self):
        return "__repr__"

a = A()
print(a)


# str和repr同时存在时候，返回字符串执行的是str函数
class A():
    def __str__(self):
        return "__str__"
    def __repr__(self):
        return "__repr__"

a = A()
print(a)


# str和repr本质区别，查看官方文档实例
import datetime
today = datetime.date.today()

# str返回的字符串可读性更强
print(str(today))

# repr返回结果应更准确。存在的目的在于调试，便于开发者使用。
# 细心的读者会发现将 __repr__ 返回的方式直接复制到命令行上，是可以直接执行的。
print(repr(today))