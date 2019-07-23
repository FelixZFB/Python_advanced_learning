# yield from案例
def gen():
    for c in "AB":
        yield c

# 先返回A,再返回B
print(list(gen()))

def gen_new():
    yield from "AB"

# 直接返回A和B
print(list(gen_new()))


# 委派生成器