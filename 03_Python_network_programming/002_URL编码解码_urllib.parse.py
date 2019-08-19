# URL编码是浏览器传输数据时候出现错误
# 浏览器会自动进行URL编码，%xx%xx%xx
# 数据库要使用浏览器传过来的数据就需要解码

import urllib.parse

# Python3 url编码
print(urllib.parse.quote("天安门"))

# Python3 url解码
print(urllib.parse.unquote("%E5%A4%A9%E5%AE%89%E9%97%A8"))