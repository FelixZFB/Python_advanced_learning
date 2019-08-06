004_MiniWeb_Web服务器_实现模板文件
    各功能进行封装到包里面
    web_server作为服务器控制整个过程
    dynamic里面放置web框架，用于处理动态请求
    static里面放置css js静态文件，静态请求直接打开调用
    templates放置一些固定的前端html框架页面，到时候动态请求可以直接调用 