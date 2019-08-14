- 011_MiniWeb_Web服务器_实现模板文件_添加MySQL功能_替换模板升级版Plus 
    010项目升级，替换模板数据，使用mysql中查询到数据替换指定模板中的数据
    011里面加入了个人中心的数据，使用内连接查询两个数据表，提取出个人中心的数据
    index.py和center.py处理去寻找static中的index/center.html模板文件
    原始模板文件里面有个{%content%}，我们将其进行替换
    上面替换，使用%s字符串替换，元组切片取出数据

    先启动数据库然后使用stock_db数据库：
    CMD窗口执行：mysql -u root -p  密码：00xxx56
                show databases;
                use stock_db;
    CMD虚拟环境下指定端口运行代码：
    python web_server.py 7788 mini_frame:application
    浏览器打开：http://127.0.0.1:7788/index.py
    
    上面都使用了mysql查询数据，就是查询语句不一样，因此我们可以重新一个函数
    conn_sql()专门用于查询数据,传入查询语句作为参数，返回查询的结果