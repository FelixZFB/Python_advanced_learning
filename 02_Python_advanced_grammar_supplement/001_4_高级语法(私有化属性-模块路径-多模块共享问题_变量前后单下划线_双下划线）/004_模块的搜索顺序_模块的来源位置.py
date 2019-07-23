# 模块会自动从选择的解释器中进行搜索
# 如果是同级文件夹下自定义模块，则首先搜索

# 虚拟环境创建时候，勾选了Inherit global site-packages
# 勾选之后，会继承所选择的Anaconda的python解释器中对应的库
# 即继承了Anaconda环境的安装文件夹中本地所有的库
# 但是只是可以使用其中的库，这些库并没有复制到项目文件中的venv文件夹中

# 注意库虽然没有复制过来，但是虚拟环境venv\Scripts中
# 已经基于Anaconda中安装的python重新新建了python.exe虚拟环境下独立的解释器

# 查看库的路径来源


# 这两个库是直接调用的Anaconda环境中
import scrapy
import random


# 这个库是后期Pycharm安装的，安装在项目文件下的venv中
import Asterisk

# 显示模块搜索所在的路径
print(random.__file__)
print(scrapy.__file__)
print(Asterisk.__file__)


