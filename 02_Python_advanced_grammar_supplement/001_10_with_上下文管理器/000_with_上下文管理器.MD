# with常用于打开文件，使用with可以自动关闭，即使出现错误

# 什么是上下文（context）？
- context其实说白了，和文章的上下文是一个意思，在通俗一点，我觉得叫环境更好
- 上下文虽然叫上下文，但是程序里面一般都只有上文而已，只是叫的好听叫上下文。。
- 进程中断在操作系统中是有上有下的，不过不这个高深的问题就不要深究了

任何实现了 __enter__() 和 __exit__() 方法的对象都可称之为上下文管理器，
上下文管理器对象可以使用with关键字。显然，文件（file）对象也实现了上下文管理器。

那么文件对象是如何实现这两个方法的呢？我们可以模拟实现一个自己的文件类，
让该类实现 __enter__() 和 __exit__() 方法。

class File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("entering")
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, *args):
        print("will exit")
        self.f.close()
        
__enter__() 方法返回资源对象，这里就是你将要打开的那个文件对象，
__exit__() 方法处理一些清除工作。

with File('out.txt', 'w') as f:
    print("writing")
    f.write('hello, python')
    
你就无需显示地调用 close 方法了，由系统自动去调用，哪怕中间遇到异常 close 方法也会被调用。
