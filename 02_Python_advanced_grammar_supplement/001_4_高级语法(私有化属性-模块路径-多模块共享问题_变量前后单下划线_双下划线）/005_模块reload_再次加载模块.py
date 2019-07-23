import aaa

from imp import reload
reload(aaa)

# reload再次下载模块

# 用途：一个程序不能停止，但是导入的一个模块发生了修改，要实现修改后的功能
# 此时程序里面就可以使用reload，注意reload使用之前，程序必须使用了import导入了模块