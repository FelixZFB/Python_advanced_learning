# 日志实例

# 设置日志格式--->设置配置信息（名称，级别等信息）--->设置要输出各个级别message要显示的内容

import logging

# 自定义记录格式
LOG_FORMAT = "%(asctime)s=====%(levelname)s+++++%(message)s"

# 设置输出的日志文件，设置输出什么级别的日志和日志的格式
# 该函数只在程序第一次调用时生效
# 文件内容保存到文件中，格式为自定义格式level设置的级别及该级别一上的才会打印
logging.basicConfig(filename="27_1.log", filemode='a', level=logging.WARNING, format=LOG_FORMAT)

# 上面输出乱码，要设置编码，需要在handlers中设置，参考002，003案例

# 设置相应级别的日志，就是要输出显示的message内容
logging.debug("This is a debug log-日志记录.")
logging.info("This is a info log-日志记录.")
logging.warning("This is a warning log-日志记录.")
logging.error("This is a error log-日志记录.")
logging.critical("This is a critical log-日志记录.")
