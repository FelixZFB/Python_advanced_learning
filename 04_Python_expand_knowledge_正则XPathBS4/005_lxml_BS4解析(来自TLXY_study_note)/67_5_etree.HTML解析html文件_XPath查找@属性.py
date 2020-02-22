# 属性匹配

from lxml import etree


text='''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">第一个</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
     </ul>
 </div>
'''

html=etree.HTML(text,etree.HTMLParser())

# 访问属性采用[@属性]
result=html.xpath('//li[@class="item-1"]')
print(result)