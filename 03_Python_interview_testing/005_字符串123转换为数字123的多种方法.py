# 使用ord函数，将str类型或unicode类型转换为ascii数值
# ord返回值为十进制整数，是int类型

def atoi(s):
    num = 0
    for v in s:
        num = num * 10 + ord(v) - ord('0')
    print(num)
    return num

atoi("123")


# 上面函数第一次执行时：num=0 v=1 num = 0*10 + 49 - 48 = 1
# 上面函数第二次执行时：num=1 v=2 num = 1*10 + 50 - 48 = 12
# 上面函数第三次执行时：num=12 v=2 num = 12*10 + 51 - 48 = 123

# print(ord("0")) 48
# print(ord("1")) 49
# print(ord("2")) 50
# print(ord("3")) 51


# 上面的代码可以简写为以下形式
from functools import reduce
def atoi(s):
    return reduce(lambda num, v: num * 10 + ord(v) - ord('0'), s, 0)
print(atoi("123"))