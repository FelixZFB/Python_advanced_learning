# 遍历文档树
# 父节点,兄弟节点

from bs4 import BeautifulSoup

# 打开爱丽丝梦游仙境的html文档
with open('./67_12.html') as f:
    soup = BeautifulSoup(f, 'lxml')

# 打印出第一个a标签节点
link = soup.a
print(link)
# 打印出所有的父节点
print(type(link.parents))
print("*" * 50)

# 取出所有上面a节点的父节点的名称
for parent in link.parents:
        print(parent.name)
print("*" * 50)

# 兄弟节点，同一级别