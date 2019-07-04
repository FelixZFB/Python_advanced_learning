# 读取HTML文件，进行解析
# etree和XPath的配合使用

from lxml import etree

# 打开HTML文件
#指定解析器HTMLParser会根据文件修复HTML文件中缺失的如声明信息
html = etree.parse('./67_3.html', etree.HTMLParser())
print(type(html))

# 获取所有的子孙节点
result = html.xpath('//*')
print(type(result))
print(result)

# 获取
result1 = html.xpath('//h2')
print(result1)