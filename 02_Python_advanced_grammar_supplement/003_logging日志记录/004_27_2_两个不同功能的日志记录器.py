
import logging

import logging.handlers
import datetime

# 设置一个logger实例--->设置日志格式--->
# 分别设置两个日志处理器，设置配置信息（名称，级别等信息）--->
# 设置要输出各个级别message要显示的内容


# 定义logger，实例化一个logger
logger = logging.getLogger('mylogger')
# 设置日志级别为DEBUG
logger.setLevel(logging.DEBUG)



# 设置第一个handler,级别为all(debug),需要按时间切割
rf_handler = logging.handlers.TimedRotatingFileHandler('all.log-日志记录', encoding='utf-8', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

# 设置第二个handler，级别为error
f_handler = logging.FileHandler(filename='error.log-日志记录', mode='a', encoding='utf-8')
f_handler.setLevel(logging.ERROR)
# 打印日志的时间---打印当前执行程序名[ 打印日志的当前行号]---打印日志级别名称---打印日志信息
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))


# 加入上面两个日志处理器
logger.addHandler(rf_handler)
logger.addHandler(f_handler)


# 设置不同级别日志的message显示的内容，要输出显示的message内容
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')