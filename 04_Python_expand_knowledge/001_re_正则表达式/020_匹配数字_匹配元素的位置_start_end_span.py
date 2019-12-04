# 导入正则表达式的包
import re

# 查找数字
# 编写一个正则表达式的对象
pattern = re.compile(r'\d+')  # 用于匹配至少一个数字
p = pattern
m = p.match('d2kjf349jfd39fak4j42j') # 查找头部，没有匹配
print(m)
m1 = p.match('2d2kjf349jfd39fak4j42j') # 查找头部，匹配到2
print(m1)
m = p.match('d2kjf349jfd39fak4j42j', 5, 15) # 从第6个字符开始匹配到第15个字符结束
# 查找的结果只包含第一次成功的对象，打印出来是349，从第6个开始到第9个截止
print(m)


# 取出匹配到的元素
print(m[0])
print(m.group())
# 打出找出的元素开始和结束的位置
print(m.start(0))
print(m.end(0))
print(m.span(0))