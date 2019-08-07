- 005_MiniWeb_Web服务器_实现模板文件_指定端口及框架
    运行代码时候指定端口和框架
    我们就可以指定不同的接口和框架了
    运行代码时候传参数，只需要主代码main函数中加入sys.argv
    argv就是CMD窗口中运行时python之后传递来的参数
    然后服务器main函数中提取出传递的参数
    
    第一步：指定端口
    main函数中修改代码用于接收port参数，然后WSGIServer(port)传递到
    self.tcp_server_socket.bind(("", port))中绑定端口
    CMD虚拟环境下指定端口运行代码：
    python web_server.py 7888
    
    第二步：指定框架
    main函数中修改代码用于接收框架的参数，然后WSGIServer(port, app)传递到
    self.application = app 
    # 直接使用外面传入的模块参数self.application = app
    body = self.application(env, self.set_response_header)
    CMD虚拟环境下指定端口运行代码：
    python web_server.py 7788 mini_frame:application