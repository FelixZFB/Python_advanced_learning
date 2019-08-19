# -*-coding:utf-8 -*-

import logging
import logging.handlers
import datetime


# 第一步，创建一个logger对象，用于记录日志的对象
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关

# 第二步，创建一个handler，该对象用于写入日志文件
logfile = './log.txt'
fh = logging.FileHandler(filename=logfile, mode='a', encoding='utf-8')  # open的打开模式这里可以进行参考
fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

# 第三步，再创建一个handler，该对象用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)   # 输出到console的log等级的开关

# 第四步，定义handler的输出格式，并将上面两个对象设置格式
# 打印日志的时间---打印当前执行程序名[ 打印日志的当前行号]---打印日志级别名称---打印日志信息
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 第五步，将handler对象添加到logger日志记录对象里面
logger.addHandler(fh)
logger.addHandler(ch)

# 日志message要显示出来的内容
logger.debug('这是 logger debug message')
logger.info('这是 logger info message')
logger.warning('这是 logger warning message')
logger.error('这是 logger error message')
logger.critical('这是 logger critical message')


# 此时，运行代码，会在终端显示，同时输出记录文件