# 模块会自动从选择的解释器中进行搜索
# 如果是同级文件夹下自定义模块，则首先搜索


import random

# 显示模块搜索所在的路径
print(random.__file__)

rand = random.randint(0, 10)

print(rand)
