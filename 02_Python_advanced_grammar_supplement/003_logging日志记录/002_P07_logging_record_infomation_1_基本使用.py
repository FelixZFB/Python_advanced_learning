# -*- coding: utf-8 -*-
# logging模块记录输出日志信息
# 参考TLXY_study_note中高级语法log-日志记录

import logging

# 自定义记录格式：时间，日志级别，日志内容
# 打印日志的时间---打印当前执行程序名[ 打印日志的当前行号]---打印日志级别名称---打印日志信息
LOG_FORMAT = "%(asctime)s---%(filename)s[line:%(lineno)d]---%(levelname)s: %(message)s"
LOG_FH = [logging.FileHandler(filename='logging_record_information_1.log', mode='a', encoding='utf-8')]

# 设置输出的日志文件，设置输出什么级别的日志和日志的格式
# 该函数只在程序第一次调用时生效
# 文件内容保存到文件中，格式为自定义格式level设置的级别及该级别一上的才会打印
# 如果要设置编码格式，则需要将文件名放到handlers中
# WARNING以上进行打印，格式使用上面自定义的格式，文件名，编码，追加方式记录
logging.basicConfig(
    # filename='logging_record_information_1.log',
    level=logging.WARNING,
    format=LOG_FORMAT,
    handlers= LOG_FH
)

# 设置相应级别的日志输出实例，括号中就是日志输出的内容，用于日志的输出的message内容
logging.debug("This is a debug log: 日志内容.")
logging.info("This is a info log: 日志内容.")
logging.warning("This is a warning log: 日志内容.")
logging.error("This is a error log: 日志内容.")
logging.critical("This is a critical log: 日志内容.")