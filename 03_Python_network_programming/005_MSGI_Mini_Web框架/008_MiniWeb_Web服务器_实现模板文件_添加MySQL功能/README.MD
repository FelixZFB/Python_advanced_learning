- 008_MiniWeb_Web服务器_实现模板文件_添加MySQL功能   
    - 导入外部的sql数据文件到本地MySQL数据库
        - 先切换到要导入数据的数据库
            use stock_db
        - 导入数据
            source sql文件的路径  
            （注意你的文件路径要是复制来的，windows下要将"\"全部换成“/”）
            mysql> source D:/stock_db.sql
    007项目升级，支持查询MySQL数据，然后将其返回
    专门定义一个my_sql()函数，用于连接数据库，查询数据，然后返回数据作为body
    先启动数据库然后使用stock_db数据库：
    CMD窗口执行：mysql -u root -p  密码：00xxx56
                show databases;
                use stock_db;
    CMD虚拟环境下指定端口运行代码：
    python web_server.py 7788 mini_frame:application
    浏览器打开：http://127.0.0.1:7788/my_sql.py 