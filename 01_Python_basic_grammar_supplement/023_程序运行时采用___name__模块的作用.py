# 全局变量、函数、类，注意：直接执行的代码不是向外界提供的工具！

def say_hello():
    print("你好你好，我是 say hello")


# 如果直接执行模块，__main__
if __name__ == "__main__":
    # 文件被导入时，能够直接执行的代码不需要被执行！我们只是需要使用模块中的方法
    # 意思就是该模块导入到别的脚本中，以下代码不会被执行
    # 如果if __name__ == "__main__":不加该语句
    # 下面的代码，被导入到一个新的脚本时候，新的脚本执行时候，
    # 该代码中下面的三行代码会自动执行，这并不是我们所希望的
    # 因为我们导入模块，一般只是需要调用模块中的方法

    print(__name__)
    print("小明开发的模块")
    say_hello()


'''
print(__name__)
print("小明开发的模块")
say_hello()
'''