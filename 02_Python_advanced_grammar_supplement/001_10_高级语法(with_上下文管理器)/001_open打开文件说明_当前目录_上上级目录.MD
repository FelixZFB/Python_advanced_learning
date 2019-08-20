# 注意：

# 一般情况下：
# open打开文件时，当前运行主代码程序所在的文件夹作为当前目录
# 如果文件夹在当前目录，直接使用.,在上级目录使用..,在上上级使用../..


# 比如以下文件中，请求的文件在上一级目录，使用../html，要是在当前目录就可以直接使用./html
# 比如03_Python_network_programming\005_MSGI_Mini_Web框架\003_MSGI_MiniWeb_Web服务器__dict使用(通过传递字典实现浏览器不同的动态请求)
\MSGI_面向对象_Web服务器_集成解析动态资源请求_升级版_支持MSGI接口.py的51行代码


# 特殊情况：
# 程序里面封装了多个模块，多个包，运行的主代码，只有一个，其它代码都是作为包导入
# 但是包里面有open打开文件，此时，当前路径并不是包所在文件夹，而是主代码所在的文件夹

# web_server.py所在的目录就是当前目录
# dynamic文件夹中的mini_frame.py需要打开templates中的文件
# 使用的是一个点：./templates/index.html
# 如果使用../templates/index.html，就是到web_server.py上一级目录里面去找templates文件夹了
# 比如03_Python_network_programming\005_MSGI_Mini_Web框架\004_MiniWeb_Web服务器_实现模板文件
\web_server.py
