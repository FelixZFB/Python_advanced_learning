import re

title = '世界 你好，hello world'

# 匹配中文字符，找出所有的中文字符
p = re.compile(r'[\u4e00-\u9fa5]+')
rst1 = p.findall(title)
print(rst1)

# 以下方式匹配只从第一个字符开始，匹配到一个符合条件的纠结束了
rst2 = re.match(r'[\u4e00-\u9fa5]+', title)
print(rst2[0])




