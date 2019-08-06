
def index():
    with open("./templates/index.html",encoding="utf-8") as f:
        content = f.read()
    return content

def center():
    with open("./templates/center.html",encoding="utf-8") as f:
        return f.read()
     

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    
    file_name = env['PATH_INFO']
    # file_name = "/index.py"

    if file_name == "/index.py":
        return index()
    elif file_name == "/center.py":
        return center()
    else:
        return 'Hello World! 我爱你中国....'

# 注意，open知识补充
# 特殊情况：
# 程序里面封装了多个模块，多个包，运行的主代码，只有一个，其它代码都是作为包导入
# 但是包里面有open打开文件，此时，当前路径并不是包所在文件夹，而是主代码所在的文件夹

# web_server.py所在的目录就是当前目录
# dynamic文件夹中的mini_frame.py需要打开templates中的文件
# 使用的是一个点：./templates/index.html
# 如果使用../templates/index.html，就是到web_server.py上一级目录里面去找templates文件夹了
# 比如03_Python_network_programming\005_MSGI_Mini_Web框架\004_MiniWeb_Web服务器_实现模板文件
# \web_server.py
