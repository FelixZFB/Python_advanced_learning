# lambda表达式可以定义一个匿名函数，一般用于定义一个小型函数
# lambda一般都是单一的参数表达式，内部没有类似def函数的语句

# 下面就是一个lambda匿名函数，传入参数，返回值就是表达式的计算结果
func = lambda x: x * x - x

res = func(3)

print(res)