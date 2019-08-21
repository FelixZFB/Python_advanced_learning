# 有时候导入模块时候搜索不到路径
# 只会搜索系统路径，pycharm可以直接标记文件夹文件系统路径文件

# 使用sys.path.append('绝对路径或相对路径')
# 比如:程序当前文件夹中的dynamic文件夹，sys.path.append('./dynamic')

# 搜索路径顺序：
# # 最先搜索当前路径
# # 然后搜索上级目录
# # 再搜索当前项目虚拟环境
# # 再搜索Anaconda环境

# 导入代码中间的变量名作为模块，不能直接使用from xxx import xxx
# 要使用aaa = __import__(xxx)，返回值aaa标记导入的xxx对应的模块xxx.py
# 然后使用：函数名 = getattr(模块名, 函数名)得到模块中的一个函数

# 具体参考003网络编程中的005web框架中的005和012的web_server.py中代码
# 参考008案例，直接复制过来的005



