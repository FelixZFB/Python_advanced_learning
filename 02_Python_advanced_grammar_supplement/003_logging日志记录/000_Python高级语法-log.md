# **Python高级语法——log——学习心得笔记**

参考博客：Python之日志处理-logging模块(https://www.cnblogs.com/yyds/p/6901864.html)

# 1. 日志相关概念
- 日志的级别
    - 不同用户关注不同的程序信息
    - 日志的级别如下,从低到高
    - NOTSET
    - DEBUG
    - INFO
    - NOTICE
    - WARNING
    - ERROR
    - CRITICAL
    
    - ALERT
    - EMERGENCY
    
- IO操作=》不要频繁操作
- LOG的作用
    - 调试
    - 了解软件的运行情况
    - 分析定位问题
    
- 日志信息
    - time
    - location
    - level
    - content
    
- 成熟的第三方日志模块
    - log4j
    - log4php
    - logging

# 2. logging模块
- logging模块下日志级别（默认6种）
    - 级别可以自定义(可以自己添加自定义等级及等级数值)
    - NOTSET 0
    - DEBUG 10
    - INFO 20
    - WARNING 30 
    - ERROR 40 
    - CRITICAL 50
- 初始化/写日志实例需要指定级别，只有当级别等于或等于指定级别才被记录
- 使用方式
    - 直接使用logging（封装了其它组件）
    - logging有四大组件

## 2.1. logging模块级别的日志使用

- 日志记录方法（一般记录5个级别）
    - logging.debug(msg, *args, **kwargs)	创建一条严重级别为DEBUG的日志记录
    - logging.info(msg, *args, **kwargs)	创建一条严重级别为INFO的日志记录
    - logging.warning(msg, *args, **kwargs)	创建一条严重级别为WARNING的日志记录
    - logging.error(msg, *args, **kwargs)	创建一条严重级别为ERROR的日志记录
    - logging.critical(msg, *args, **kwargs)	创建一条严重级别为CRITICAL的日志记录

logging.log(level, *args, **kwargs)	创建一条严重级别为level的日志记录
logging.basicConfig(**kwargs)	对root logger进行一次性配置   

- logging.basicConfig(**kwargs)
- 对root logger进行一次性配置
- 只在第一次调用时起作用
- 不配置则使用默认值
    - 输出：sys.stder
    - 级别：WARNING（该级别以上的才会显示）
    - 格式：level:log_name:content
- 27_1.py 
- P07_logging_record_crawl_process（来自Python_development_skills_summary）


## 2.2. logging模块的处理流程
- 四大组件
    - 日志器（Logger):产生日志的一个接口
    - 处理器（Handler):把产生的日志发送到相应的目的地
    - 控制器（Filter):更精细的控制哪些日志的输出
    - 格式器（Formatter):对输出的信息进行格式化
- Logger
    - 产生一个日志
    - 日志操作
         Logger.setLevel()	设置日志器将会处理的日志消息的最低严重级别
         Logger.addHandler() 和 Logger.removeHandler()	
         为该logger对象添加 和 移除一个handler对象
         Logger.addFilter() 和 Logger.removeFilter()	    
         为该logger对象添加 和 移除一个filter对象  
         Logger.debug(), Logger.info(), Logger.warning(), Logger.error(), Logger.critical()	
         创建一个与它们的方法名对应等级的日志记录
         Logger.exception()	创建一个类似于Logger.error()的日志消息
         Logger.log()	需要获取一个明确的日志level参数来创建一个日志记录 

    - 如何得到一个logger对象
        - 实例化
        - logging.getLogger()
        
- Handler
    - 把log发送到指定位置
    - 方法
        - setLevel
        - setFormat
        - addFilter, removeFilter     
    - 不需要直接使用，Handler是基类
    logging.StreamHandler	将日志消息发送到输出到Stream，如std.out, std.err或任何file-like对象。
    logging.FileHandler	将日志消息发送到磁盘文件，默认情况下文件大小会无限增长
    logging.handlers.RotatingFileHandler	将日志消息发送到磁盘文件，并支持日志文件按大小切割
    logging.hanlders.TimedRotatingFileHandler	将日志消息发送到磁盘文件，并支持日志文件按时间切割
    logging.handlers.HTTPHandler	将日志消息以GET或POST的方式发送给一个HTTP服务器
    logging.handlers.SMTPHandler	将日志消息发送给一个指定的email地址
    logging.NullHandler	该Handler实例会忽略error messages，通常被想使用logging的library
    开发者使用来避免'No handlers could be found for logger XXX'信息的出现。  
          
- Format类
    - 直接实例化
    - 可以继承Format添加特殊雷人
    - 三个参数
        logging.Formatter.__init__(fmt=None, datefmt=None, style='%')
        
        fmt：指定消息格式化字符串，如果不指定该参数则默认使用message的原始值
        datefmt：指定日期格式字符串，如果不指定该参数则默认使用"%Y-%m-%d %H:%M:%S"
        style：Python 3.2新增的参数，可取值为 '%', '{'和 '$'，如果不指定该参数则默认使用'%'         
        
- Filter类



1. 需求
现在有以下几个日志记录的需求：

1）要求将所有级别的所有日志都写入磁盘文件中
2）all.log文件中记录所有的日志信息，日志格式为：日期和时间 - 日志级别 - 日志信息
3）error.log文件中单独记录error及以上级别的日志信息，日志格式为：日期和时间 - 日志级别 - 文件名[:行号] - 日志信息
4）要求all.log在每天凌晨进行日志切割

2. 分析
1）要记录所有级别的日志，因此日志器的有效level需要设置为最低级别--DEBUG;
2）日志需要被发送到两个不同的目的地，因此需要为日志器设置两个handler；另外，两个目的地都是磁盘文件，因此这两个handler都是与FileHandler相关的；
3）all.log要求按照时间进行日志切割，因此他需要用logging.handlers.TimedRotatingFileHandler; 
    而error.log没有要求日志切割，因此可以使用FileHandler;
4）两个日志文件的格式不同，因此需要对这两个handler分别设置格式器；

3. 代码实现
- 看实例27_2.py

4. 常用输出格式设置
- logging.basicConfig函数中，可以指定日志的输出格式format，这个参数可以输出很多有用的信息，如下:

    %(levelno)s: 打印日志级别的数值
    %(levelname)s: 打印日志级别名称
    %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
    %(filename)s: 打印当前执行程序名
    %(funcName)s: 打印日志的当前函数
    %(lineno)d: 打印日志的当前行号
    %(asctime)s: 打印日志的时间
    %(thread)d: 打印线程ID
    %(threadName)s: 打印线程名称
    %(process)d: 打印进程ID
    %(message)s: 打印日志信息

- 在工作中给的常用格式如下:
- format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
- 这个格式可以输出日志的打印时间，是哪个模块输出的，输出的日志级别是什么，以及输入的日志内容。
