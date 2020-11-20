# 遍历文档树
# 子孙节点信息
# string实例

from bs4 import BeautifulSoup

# 打开爱丽丝梦游仙境的html文档
with open('./67_12.html') as f:
    soup = BeautifulSoup(f, 'lxml')
print(soup.string)

# 类型是一个生成器，可以使用for循环取出内容
print(type(soup.strings))
# for string in soup.strings:
    # print(string)

# 内容含了很多空格或空行, 使用.stripped_strings
# 可以去除多余空白内容
for string in soup.stripped_strings:
    print(string)




