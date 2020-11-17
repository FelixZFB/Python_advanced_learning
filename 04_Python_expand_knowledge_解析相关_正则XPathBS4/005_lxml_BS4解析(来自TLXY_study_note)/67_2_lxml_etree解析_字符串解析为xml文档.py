# lxml解析案例

from lxml import etree

text='''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">第一个</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0"><a href="link5.html">a属性</a>
     </ul>
 </div>
'''

# 利用etree把字符串解析成一个XML文件,并自动补全缺失项
html = etree.HTML(text)
print(type(html))  # <class 'lxml.etree._Element'>

# 将上面解析后的html文件又解析成字节文件
result = etree.tostring(html, encoding='utf-8')
print(type(result))
# 字节使用utf-8编码格式解码为字符串
print(type(result.decode('utf-8')))
print(result.decode('utf-8'))

