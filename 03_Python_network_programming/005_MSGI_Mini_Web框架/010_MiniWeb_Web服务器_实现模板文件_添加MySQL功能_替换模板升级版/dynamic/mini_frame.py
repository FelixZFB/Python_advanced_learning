# -*- coding:utf-8 -*-

import re
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

    # static里面的index.html原始文件读取结果content里面有{%content%}数据，我们对其进行替换
    # {}一般用来表示匹配的长度，只限制{}它前面的一个字符，下面大括号前面加\就是去转义，匹配{和}左右大括号字符
    # my_stock_infos = "这里是从MySQL数据库中查询出来的数据"
    # content = re.sub(r"\{%content%\}", my_stock_infos, content)

    # 上面代码用于演示原理，下面我们使用mysql中查询到的数据进行模板替换
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

    # 我们使用一个前端模板，替换原html中的{%content%},即向标题行下面不断添加一行一行的数据
    # tr是行标签，td是列标签
    # 我们进入数据库查看原始数据，一列8行，正好对应html标题栏中的前8行
    # stock_infos里面存储的每一个小元组就是一行数据，都是字符串，我们下面使用%s取出
    # mysql> select * from info;
    # +----+--------+----------+---------+----------+-------+-------+------------+
    # | id | code   | short    | chg     | turnover | price | highs | time       |
    # +----+--------+----------+---------+----------+-------+-------+------------+
    # |  1 | 000007 | 全新好   | 10.01%  | 4.40%    | 16.05 | 14.60 | 2017-07-18 |
    # |  2 | 000036 | 华联控股 | 10.04%  | 10.80%   | 11.29 | 10.26 | 2017-07-20 |
    # |  3 | 000039 | 中集集团 | 1.35%   | 1.78%    | 18.07 | 18.06 | 2017-06-28 |
    tr_template = '''
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td> 
        <td>%s</td> 
        <td>
            <input type="button" value="添加" id="toAdd" name="toAdd" systemidvalue="000007">
        </td>
    </tr>
    '''

    # 创建一个空html模板字符串，数据库查询出来有多少个数据，上面的一行就加多少次
    # 最终有多少个元组，及多少支股票数据，就有多少行
    html_template = ''
    for line_info in stock_infos:
        # 使用%s字符串替换，使用查询到的数据替换给定模板中的数据
        html_template += tr_template % (
            line_info[0],
            line_info[1],
            line_info[2],
            line_info[3],
            line_info[4],
            line_info[5],
            line_info[6],
            line_info[7],
        )
    content = re.sub(r"\{%content%\}", html_template, content)
    return content

@route("/center.py")
def center():
    with open("./templates/center.html",encoding="utf-8") as f:
        content = f.read()
    # 替换center.html源代码中的{%content%}
    my_stock_infos = "这里是从MySQL数据库中查询出来的数据"
    content = re.sub(r"\{%content%\}", my_stock_infos, content)
    return content


# 定义一个函数，用于处理连接MySQL获取数据并返回数据
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

# 009项目升级，替换模板数据，使用mysql中查询到数据替换指定模板中的数据
# index.py处理去寻找static中的index.html模板文件
# 原始模板文件里面有个{%content%}，我们将其进行替换
# 上面替换，使用%s字符串替换，元组切片取出数据

# CMD虚拟环境下指定端口运行代码：
# python web_server.py 7788 mini_frame:application
# 浏览器打开：http://127.0.0.1:7788/index.py

