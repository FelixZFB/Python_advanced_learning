# -*- coding:utf-8 -*-

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

# 006项目升级，if语句升级，如果有大量的功能，则需要非常多的elif语句
# elif超过四五个，就使用字典存储起来，然后再调用
# 字典的key是请求的文件名，value是要被调用的函数
# 上面字典利用了装饰器可以传递参数和函数名，同时装饰器并不需要被装饰的函数执行，
# 只要代码被导入，装饰器@就被执行了，这样所有的动态请求的网址名称和用于处理动态请求的函数名称就都加入字典了

# 路由是什么？
# 根据浏览器的请求是什么，到时候就调用什么函数为其服务,就是路由实现的
# 什么请求用什么服务，安排这个步骤的就是路由

# 上面是使用装饰器和字典实现了路由功能