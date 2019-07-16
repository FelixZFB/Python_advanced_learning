# 生成器案例,yield
def odd():
    print("Step 1")
    yield 1
    print("Step 2")
    yield 2
    print("Step 3")
    yield 3

# 调用生成器
# next调用函数，执行过的就不在执行，执行没有被执行的
# 先生成一个生成器g
# yield先调用函数执行语句，然后返回yield之后的值
g = odd()
one = next(g)
print(one)
two = next(g)
print(two)


# for循环调用生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1
    return "Done"

# 生成一个生成器
g = fib(5)
for i in range(6):
    rst = next(g)
    print(rst)

for i in g:
    print(i)


