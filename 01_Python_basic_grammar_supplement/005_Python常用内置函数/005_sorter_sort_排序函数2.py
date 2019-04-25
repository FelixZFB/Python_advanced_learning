# 排序案例补充

# sorted案例
astr = ['abc', 'Tian', 'hafj', 'Xixi']

# 按字母升序排列
str2 = sorted(astr, key=str.lower)
print(str2)

# 按字母降序排列
str2 = sorted(astr, key=str.lower, reverse=True)
print(str2)