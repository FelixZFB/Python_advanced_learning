实例参考04/004中网络爬虫通用模块

- 访问网络的两种方法
    - get 
        - 利用参数给服务器传递信息
        - 参数为dict,使用parse编码
        - 看实例43_4
    - post
        - 一般向服务器传递参数使用
        - post是把信息自动加密处理
        - 我们如果想使用post信息，需要使用data参数
        - 使用post,意味着http请求头可能需要更改:
            - Content-Type: application/x-www.form-urlencode
            - Content-Length: 数据长度
            - 简而言之，一旦更改请求方法，注意其它请求头部信息相适应         
            - 看实例43_5/6
            - 为了更多的设置请求信息，单纯通过urlopen就不太适用了
            - 需要使用request.Request类 

- get与post的区别：
    POST请求的参数都在放在formdata中，可以查看有道翻译，翻译一个单词，
    检查network中headers，里面有formdata，里面有发送请求的相关参数。
    浏览器地址栏中的网址没有发生变化。可以参考有道翻译：
    http://fanyi.youdao.com/

    get请求：请求的参数直接放在url地址之中，
    请求的参数进行url编码直接放在地址中，可以参考豆瓣的电影排行榜:
    https://movie.douban.com/typerank?type_name=剧情&type=11&interval_id=100:90&action=
    
    具体区别：
        参考案例43_18_1为有道post请求
        43_4为get请求

（注：判断post与get请求最显著的区别就是url地址是否发生变化，发生变化了就是get，反之则是post请求，post请求的参数是在表单里） 