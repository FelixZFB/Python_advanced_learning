# 两种方式：%和format

# >>>"{} {}".format("hello", "world") # 不设置指定位置，按默认顺序
# 'hello world'
# >>> "{0} {1}".format("hello", "world") # 设置指定位置
# 'hello world'
# >>> "{1} {0} {1}".format("hello", "world") # 设置指定位置
# 'world hello world'

# 参考网址1：https://www.cnblogs.com/fat39/p/7159881.html
# 参考网址2：http://www.runoob.com/python/att-string-format.html


# 定义字符串变量name，使用%s, 输出我的名字叫小明，请多多关照！
name = "大小明"
print("我的名字叫 %s，请多多关照！" % name)

# 定义整数变量，使用%d, student_no，输出我的学号
student_no = 100123456
print("我的学号是 %d" % student_no)

# 定义小数 price、weight、money，
# 输出 苹果单价 9.00 元／斤，购买了 5.00 斤，需要支付 45.00 元
price = 8.5
weight = 7.5
money = price * weight
print("苹果单价 %.2f 元／斤，购买了 %.3f 斤，需要支付 %.4f 元" % (price, weight, money))

# 定义一个小数 scale，输出 数据比例是 10.00%
scale = 0.8
print("数据比例是 %.2f%%" % (scale * 100))

# 符号使用%c
print("1 %c 1 %c %d" % ('+', '=', 2))
