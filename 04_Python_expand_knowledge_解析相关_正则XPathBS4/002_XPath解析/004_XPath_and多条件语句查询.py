# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/16 14:49
Desc:
'''
from lxml import etree


xml111 = '''
<Test>
<cell><data type="String">Alpha</data></cell> 
<cell><data type="Number1">200</data></cell> 
<cell><data type="Number2">200</data></cell>
<cell><data type="Number3">200</data></cell>
<cell><data type="Boolean">true</data></cell> 
<cell><data type="Number2">true</data></cell> 
</Test> 
'''

html = etree.HTML(xml111, etree.HTMLParser())
print(html.xpath('//cell//data[text()=200]/text()'))
print(html.xpath('//cell//data[text()=200 and @type="Number2"]/text()'))


