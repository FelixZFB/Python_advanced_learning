# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2019/12/16 11:52
Desc:
'''


# Selector和SelectorList都是属于selector.py模块，只是两种对象的结果不一样
# scrapy里面的xpath默认就是使用的Selector下的xpath方法,返回的是一个Selector列表
# lxml里面的xpath默认就是使用的SelectorList下的xpath方法，返回的是一个内容列表



from scrapy.selector import Selector

body = '<body>hello</body><body>world</body>'

# scrapy下使用的是Selector类(返回结果是selector对象)下，
selectors = Selector(text=body)
print(type(selectors.xpath('//body/text()')))
print(selectors.xpath('//body/text()')) # 结果是一个selector列表
print(selectors.xpath('//body/text()').extract()) # 内容的列表
print(selectors.xpath('//body/text()').extract()[0])
print(selectors.xpath('//body/text()').extract_first()) # 推荐写法
print(selectors.xpath('//body/text()')[0])  # 不推荐写法
print(selectors.xpath('//body/text()')[0].extract())  # 不推荐写法
print('*' * 50)

# lxml下使用的xpath是SelectorList类(返回结果是selector对象的内容对象)下，因此可以直接列表取出内容
html = etree.HTML(body, etree.HTMLParser())
print(type(html.xpath('//body/text()')))
print(html.xpath('//body/text()'))
print(html.xpath('//body/text()')[0])
print(html.xpath('//body/text()')[-1])