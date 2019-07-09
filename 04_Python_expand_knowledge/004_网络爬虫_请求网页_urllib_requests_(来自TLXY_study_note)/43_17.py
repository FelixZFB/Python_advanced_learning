# 遇到不信任的SSL证书
# 如果要继续访问，则需要执行忽略处理

import ssl
from urllib import request

# 利用非认证的上下文环境替换认证的上下文环境
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.12306.cn'
rsp = request.urlopen(url)
html = rsp.read().decode()
print(html)

