- 009_MiniWeb_Web服务器_实现模板文件_添加MySQL功能_替换模板
    008项目升级，替换模板数据
    index.py处理去寻找static中的index.html模板文件
    原始模板文件里面有个{%content%}，我们将其进行替换
    上面代码全部使用指定的前端模板文件替换，还未使用mysql中数据
    我们运行查看效果
    010中我们将前端模板中的固定数据替换为我们查询出来的数据
    
    CMD虚拟环境下指定端口运行代码：
    python web_server.py 7788 mini_frame:application
    浏览器打开：http://127.0.0.1:7788/index.py