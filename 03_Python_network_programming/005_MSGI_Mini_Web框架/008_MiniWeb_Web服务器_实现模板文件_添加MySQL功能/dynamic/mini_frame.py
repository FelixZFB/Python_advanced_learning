# -*- coding:utf-8 -*-

from pymysql import connect

# 定义一个字典，用于存储url（即被请求的file_name ）和对应要被调用的函数
URL_FUNC_DICT = dict()

# 定义一个带参数装饰器，用于传递参数url(/.index.py请求的网址名file_name)和func(inex函数名)
def route(url):
    def set_func(func):
        URL_FUNC_DICT[url] = func
        # {"/index.py": index}
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func

# mini_frame.py一被导入，@装饰器就被执行了
# 利用了装饰器只要被导入或者运行，@后面的代码就被执行
# 利用装饰器自身参数和函数名就可以实现传递参数
# 装饰器最终执行的还是func()，即index()
@route("/index.py")
def index():
    with open("./templates/index.html",encoding="utf-8") as f:
        content = f.read()
    return content

@route("/center.py")
def center():
    with open("./templates/center.html",encoding="utf-8") as f:
        content = f.read()
    return content

# 定义一个函数，处理连接MySQL获取数据
@route("/my_sql.py")
def my_sql():
    # 创建Connection连接
    conn = connect(
        host='localhost', port=3306, database='stock_db',
        user='root', password='00116656', charset='utf8'
    )
    # 获得Cursor对象，该对象用于执行sql语句
    cs = conn.cursor()
    cs.execute("select * from info;")
    # 取出所有的数据,每一行是一个元组，所有的行数据放在嵌套元组中
    stock_infos = cs.fetchall()
    # 关闭Cursor对象，关闭Connection对象
    cs.close()
    conn.close()
    # 返回信息给body,返回数据必须是str，然后经过编码，浏览器才能打开
    return str(stock_infos)

def application(env, start_response):
    # start_response的值返回给headers
    # application函数的返回值作为body
    # application的调用过程参考002文件夹支持MSGI接口中的说明
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    # web_server里面传过来的字典
    file_name = env['PATH_INFO']
    # file_name = "/index.py"

    '''
    if file_name == "/index.py":
        return index()
    elif file_name == "/center.py":
        return center()
    else:
        return 'Hello World! 我爱你中国....'
    '''
    # 可能存在动态请求的xxx.py不存在，因此加入try语句
    try:
        func = URL_FUNC_DICT[file_name]
        return func()

    except Exception as ret:
        # 由于上面header已经有start_response返回了，所以浏览器中查看请求状态是200，下面返回的只是body部分
        response = "------该动态请求未找到，请输入正确的xxx.py-----异常信息：%s" % ret
        return response

# 007项目升级，支持查询MySQL数据，然后将其返回
# 专门定义一个my_sql()函数，用于连接数据库，查询数据，然后返回数据作为body
# CMD虚拟环境下指定端口运行代码：
# python web_server.py 7788 mini_frame:application
# 浏览器打开：http://127.0.0.1:7788/my_sql.py

# 此时打开页面就会显示所有的股票信息，就是格式不好看
# 接下来进一步优化