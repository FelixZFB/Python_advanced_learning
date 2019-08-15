# -*- coding:utf-8 -*-

import re
from pymysql import connect

# 定义一个字典，用于存储url（即被请求的file_name ）和对应要被调用的函数
URL_FUNC_DICT = dict()

# 下面的url都是装饰器参数，是我们给定的，一个专门处理请求的函数对应一个url
# 定义一个带参数装饰器，用于传递参数url(/.index.py请求的网址名file_name)和func(inex函数名)
def route(url):
    def set_func(func):
        URL_FUNC_DICT[url] = func
        # {"/index.py": index}
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func


# 定义一个函数专门用于查询数据
def conn_sql(find_sql):
    # 创建Connection连接
    conn = connect(
        host='localhost', port=3306, database='stock_db',
        user='root', password='00116656', charset='utf8'
    )
    # 获得Cursor对象，该对象用于执行sql语句
    cs = conn.cursor()
    cs.execute(find_sql)
    # 取出所有的数据,每一行是一个元组，所有的行数据放在嵌套元组中
    stock_infos = cs.fetchall()
    # 关闭Cursor对象，关闭Connection对象
    cs.close()
    conn.close()
    return stock_infos


# mini_frame.py一被导入，@装饰器就被执行了
# 利用了装饰器只要被导入或者运行，@后面的代码就被执行
# 利用装饰器自身参数和函数名就可以实现传递参数
# 装饰器最终执行的还是func()，即index()
@route("/index.html")
def index(ret):
    with open("./templates/index.html",encoding="utf-8") as f:
        content = f.read()

    # static里面的index.html原始文件读取结果content里面有{%content%}数据，我们对其进行替换
    # {}一般用来表示匹配的长度，只限制{}它前面的一个字符，下面大括号前面加\就是去转义，匹配{和}左右大括号字符
    # my_stock_infos = "这里是从MySQL数据库中查询出来的数据"
    # content = re.sub(r"\{%content%\}", my_stock_infos, content)

    # 上面代码用于演示原理，下面我们使用mysql中查询到的数据进行模板替换
    # 创建Connection连接

    '''
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
    '''

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

    # 调用上面的查询语句,并将返回值赋值给stock_infos
    find_sql = "select * from info;"
    stock_infos = conn_sql(find_sql)

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
            <input type="button" value="添加" id="toAdd" name="toAdd" systemidvalue="%s">
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
            line_info[1],
        )
    content = re.sub(r"\{%content%\}", html_template, content)
    return content


@route("/center.html")
def center(ret):
    with open("./templates/center.html",encoding="utf-8") as f:
        content = f.read()
    # 替换center.html源代码中的{%content%}
    # my_stock_infos = "这里是从MySQL数据库中查询出来的数据"
    # content = re.sub(r"\{%content%\}", my_stock_infos, content)

    # center个人中心使用查询到的数据，整个流程和index中一样
    # 直接将上面代码复制下来进行修改

    # 创建Connection连接

    '''
    conn = connect(
        host='localhost', port=3306, database='stock_db',
        user='root', password='00116656', charset='utf8'
    )
    # 获得Cursor对象，该对象用于执行sql语句
    cs = conn.cursor()
    cs.execute("select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info as i inner join focus as f on i.id=f.info_id;")
    # 取出所有的数据,每一行是一个元组，所有的行数据放在嵌套元组中
    stock_infos = cs.fetchall()
    # 关闭Cursor对象，关闭Connection对象
    cs.close()
    conn.close()
    '''

    # 我们使用一个前端模板，替换原html中的{%content%},即向标题行下面不断添加一行一行的数据
    # tr是行标签，td是列标签
    # 我们进入数据库查看原始数据，一列8行，正好对应html标题栏中的前8行
    # 个人信息focus表要和股票信息info表进行关联查询
    # 使用内连接进行关联查询
    # mysql> select * from info as i inner join focus as f on i.id=f.info_id;
    # +----+--------+----------+---------+----------+-------+-------+------------+----+------------------+---------+
    # | id | code   | short    | chg     | turnover | price | highs | time       | id | note_info        | info_id |
    # +----+--------+----------+---------+----------+-------+-------+------------+----+------------------+---------+
    # | 36 | 300268 | 万福生科 | -10.00% | 0.27%    | 31.77 | 13.57 | 2017-04-10 |  2 | 你确定要买这个？ |      36 |
    # | 37 | 300280 | 南通锻压 | 3.31%   | 0.66%    | 32.20 | 32.00 | 2017-04-11 |  3 | 利好             |      37 |
    # | 88 | 601678 | 滨化股份 | 0.13%   | 2.47%    |  7.92 |  7.91 | 2017-07-20 |  9 |                  |      88 |
    # | 89 | 601918 | 新集能源 | 1.23%   | 3.11%    |  4.93 |  4.92 | 2017-07-19 | 10 |                  |      89 |
    # |  1 | 000007 | 全新好   | 10.01%  | 4.40%    | 16.05 | 14.60 | 2017-07-18 | 13 |                  |       1 |
    # +----+--------+----------+---------+----------+-------+-------+------------+----+------------------+---------+
    # 然后只取出个人信息标题中需要的信息即可
    # 方法1:使用上面查询语句的结果，然后切片取出
    # 方法2：sql语句升级，直接提取出需要的结果
    # mysql> select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info as i inner join focus as f on i.id=f.info_id;
    # +--------+----------+---------+----------+-------+-------+------------------+
    # | code   | short    | chg     | turnover | price | highs | note_info        |
    # +--------+----------+---------+----------+-------+-------+------------------+
    # | 300268 | 万福生科 | -10.00% | 0.27%    | 31.77 | 13.57 | 你确定要买这个？ |
    # | 300280 | 南通锻压 | 3.31%   | 0.66%    | 32.20 | 32.00 | 利好             |
    # | 601678 | 滨化股份 | 0.13%   | 2.47%    |  7.92 |  7.91 |                  |
    # | 601918 | 新集能源 | 1.23%   | 3.11%    |  4.93 |  4.92 |                  |
    # | 000007 | 全新好   | 10.01%  | 4.40%    | 16.05 | 14.60 |                  |
    # +--------+----------+---------+----------+-------+-------+------------------+

    # 调用上面的查询语句,并将返回值赋值给stock_infos
    find_sql = "select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info as i inner join focus as f on i.id=f.info_id;"
    stock_infos = conn_sql(find_sql)

    tr_template = '''
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td> 
        <td>
            <a type="button" class="btn btn-default btn-xs" href="/update/%s.html">
            <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
        </td> 
        <td>
            <input type="button" value="删除" id="toDel" name="toDel" systemidvalue="%s">
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
            line_info[0],
            line_info[0],
        )
    content = re.sub(r"\{%content%\}", html_template, content)
    return content


# 定义一个函数，用于处理连接MySQL获取数据并返回数据
@route("/my_sql.html")
def my_sql(ret):
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


# 定义一个函数，专门用来关注股票
# 给路由添加正则表达式的原因：在实际开发时，url中往往会带有很多参数，例如/add/000007.html中000007就是参数
# 如果没有正则的话，就需要编写N次@route来进行添加url对应的函数到字典中，此时字典中的键值对有N个，浪费空间
# 而采用正则的话，那么只要编写一次@route就可以完成多个url，例如/add/000007.html /add/000036.html等对应同一个函数
# 此时字典中键值对对应的个数就会少很多
# \d+ 匹配数字一次或者多次,\.匹配.,股票代码进行一个分组
# 此时网页请求http://127.0.0.1:7788/add/000007.html，返回结果add (000007) ok
@route(r"/add/(\d+)\.html")
def add_focus(ret):
    # 1. 获取股票代码
    # 取出ret中的第一个分组，即股票代码
    stock_code = ret.group(1)

    # 2. 判断以下是否有这个股票代码
    # 创建Connection连接
    conn = connect(
        host='localhost', port=3306, database='stock_db',
        user='root', password='00116656', charset='utf8'
    )
    # 获得Cursor对象，该对象用于执行sql语句
    cs = conn.cursor()
    find_sql = "select * from info where code=%s;"
    # 上面不直接使用stock_code，防止sql注入
    cs.execute(find_sql, (stock_code,))
    # 如果没有这个股票代码，则认为是非法的请求
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "没有这只股票"

    # 3. 如果股票存在，则先判断一下是否已经关注,没关注，则将其加入关注数据里面
    else:
        find_sql = "select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s;"
        cs.execute(find_sql, (stock_code,))
        if cs.fetchone():
            return "已经关注过该股票，请勿重复关注"
        # 4. 添加关注
        # 网页运行http://127.0.0.1:7788/add/000060.py
        # 然后再打开个人中心http://127.0.0.1:7788/center.py，股票已经添加关注了
        else:
            find_sql = "insert into focus (info_id) select id from info where code=%s;"
            cs.execute(find_sql, (stock_code))
            conn.commit()
            cs.close()
            conn.close()
            return "关注股票%s成功" % stock_code

    # return "add (%s) ok" % stock_code


# 取消关注股票的函数
@route(r"/del/(\d+)\.html")
def add_focus(ret):
    # 1. 获取股票代码
    # 取出ret中的第一个分组，即股票代码
    stock_code = ret.group(1)

    # 2. 判断以下是否有这个股票代码
    # 创建Connection连接
    conn = connect(
        host='localhost', port=3306, database='stock_db',
        user='root', password='00116656', charset='utf8'
    )
    # 获得Cursor对象，该对象用于执行sql语句
    cs = conn.cursor()
    find_sql = "select * from info where code=%s;"
    # 上面不直接使用stock_code，防止sql注入
    cs.execute(find_sql, (stock_code,))
    # 如果没有这个股票代码，则认为是非法的请求
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "没有这只股票"

    # 3. 如果股票存在，则先判断一下是否已经关注,已关注，则将其取消关注
    else:
        find_sql = "select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s;"
        cs.execute(find_sql, (stock_code,))
        if not cs.fetchone():
            return "没有关注该股票，不用取消关注"
        # 4. 取消关注
        # 网页运行http://127.0.0.1:7788/add/000060.py
        # 然后再打开个人中心http://127.0.0.1:7788/center.py，股票已经添加关注了
        else:
            # find_sql = "insert into focus (info_id) select id from info where code=%s;"
            find_sql = "delete from focus where info_id = (select id from info where code=%s);"
            cs.execute(find_sql, (stock_code))
            conn.commit()
            cs.close()
            conn.close()
            return "取消关注股票%s成功" % stock_code

    # return "add (%s) ok" % stock_code


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
        # func = URL_FUNC_DICT[file_name]
        # return func()
        # {
        #   "/index.py": index,
        #   "/center.py": center,
        # }
        # 上面的url就是存储的已经有的处理对应xxx.py的file_name,# {"/index.py": index}
        # 字典中的url是在装饰器参数中手动给定的，然后和传过来的file_name进行匹配，一摸一样就可以匹配出来结果ret
        # 字典中已经储存的url可以匹配到web_server传过来的env['PATH_INFO']的file_name
        # 就可以执行，没有的话就返回else
        for url, func in URL_FUNC_DICT.items():
            ret = re.match(url, file_name)
            if ret:
                # 正则结果传进去，处理函数需要用ret的就用，不需的就不用
                # index,center不需要使用，但是还是需要传进去，add_focus需要使用，传进去，然后取出使用
                return func(ret)
        # 请求的函数可能没有，就执行下面的语句
        else:
            response = "请求的URL(%s)没有对应的函数..."
            return response

    # 其它错误都按以下处理，返回错误的原因
    except Exception as ret:
        # 由于上面header已经有start_response返回了，所以浏览器中查看请求状态是200，下面返回的只是body部分
        response = "------该动态请求未找到，请输入正确的xxx.py-----异常信息：%s" % ret
        return response

# 011项目升级，替换模板数据，使用mysql中查询到数据替换指定模板中的数据
# index.py和center.py处理去寻找static中的index/center.html模板文件
# 原始模板文件里面有个{%content%}，我们将其进行替换
# 原始模板HTML源码中有center.py和index.py，我们将其修改为.html
# 上面装饰器参数也都修改为.html，虽然还是动态请求，但是我们将其后缀改为html，就变成了伪静态了

# 012增加添加关注股票的功能函数
# 由于index.py股票信息还没有源代码添加还没进行JS接口
# 我们进行手动测试，添加关注股票
# 此时网页请求http://127.0.0.1:7788/add/000822.html，返回结果：关注股票000822成功
# 然后查看个人中心，最底部已经增加了刚刚关注的数据
# http://127.0.0.1:7788/add/000055.html,结果：没有这只股票
# 再次刷新：http://127.0.0.1:7788/add/000822.html，结果：已经关注过该股票，请勿重复关注

# 013增加删除关注股票的功能函数，和关注股票基本一致
# 运行：http://127.0.0.1:7788/del/300268.html，取消关注股票300268成功
# 再次刷新：http://127.0.0.1:7788/del/300268.html，没有关注该股票，不用取消关注



# 如果要在页面直接点击，添加或者删除，需要修改源码

# 先启动数据库然后使用stock_db数据库：
# CMD窗口执行：mysql -u root -p  密码：00xxx56
# show databases;
# use stock_db;
# CMD虚拟环境下指定端口运行代码：
# python web_server.py 7788 mini_frame:application
# 浏览器打开：http://127.0.0.1:7788/index.py

