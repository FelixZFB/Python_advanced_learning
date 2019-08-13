- 010_MiniWeb_Web服务器_实现模板文件_添加MySQL功能_替换模板升级版
    009项目升级，替换模板数据，使用mysql中查询到数据替换指定模板中的数据
    index.py处理去寻找static中的index.html模板文件
    原始模板文件里面有个{%content%}，我们将其进行替换
    上面替换，使用%s字符串替换，元组切片取出数据
    
    CMD虚拟环境下指定端口运行代码：
    python web_server.py 7788 mini_frame:application
    浏览器打开：http://127.0.0.1:7788/index.py