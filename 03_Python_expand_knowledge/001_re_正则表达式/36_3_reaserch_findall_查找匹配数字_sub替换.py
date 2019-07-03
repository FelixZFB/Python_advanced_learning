import re

# 寻找数字
p = re.compile(r'\d+')
m = p.search("one12dfe1266edaf3")
print(type(m))
print(m)

# 查找所有
rst = p.findall("one12dfe1266edaf3")
print(type(rst))
print(rst)


# sub替换案例
phone = "2004-959-559 # 这是一个电话号码"
# 删除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码 : ", num)
# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)




