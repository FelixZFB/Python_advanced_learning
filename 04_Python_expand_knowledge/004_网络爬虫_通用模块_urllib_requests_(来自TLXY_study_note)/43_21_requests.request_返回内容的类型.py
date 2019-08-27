import requests

# 两种请求方式

url = 'http://www.baidu.com'

# rsp = requests.get(url)
# print(rsp.text)

rsp = requests.request('get', url)
# 获取网页内容
html = rsp.text
print(html)
# 响应类型
print(type(rsp))
# 字符串类型
print(type(html))