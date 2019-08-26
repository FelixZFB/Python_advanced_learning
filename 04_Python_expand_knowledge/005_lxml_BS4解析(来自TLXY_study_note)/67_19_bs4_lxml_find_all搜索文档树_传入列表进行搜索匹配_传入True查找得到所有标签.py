# 搜索文档树


from bs4 import BeautifulSoup

# 打开爱丽丝梦游仙境的html文档
with open('./67_12.html') as f:
    soup = BeautifulSoup(f, 'lxml')

# 找到文档中所有<a>标签和<b>标签
print(soup.find_all(['a','b']))

# True 可以匹配任何值的标签，即返回所有标签的名称的列表
# 查找到所有的tag,但是不会返回字符串节点
print(soup.find_all(True))

# 遍历取出所有标签的name
for tag in soup.find_all(True):
    print(tag.name)