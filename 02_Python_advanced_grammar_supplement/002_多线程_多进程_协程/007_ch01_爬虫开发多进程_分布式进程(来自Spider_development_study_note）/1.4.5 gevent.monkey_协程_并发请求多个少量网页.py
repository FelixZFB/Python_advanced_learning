# 由于IO操作非常耗时，程序经常会处于等待状态
# 比如请求多个网页有时候需要等待，gevent可以自动切换协程
# 遇到阻塞自动切换协程，程序启动时执行monkey.patch_all()解决
# 首行添加下面的语句即可
from gevent import monkey; monkey.patch_all()
import gevent
from urllib import request
def run_task(url):
    print("Visit --> %s" % url)
    try:
        response = request.urlopen(url)
        data = response.read()
        print("%d bytes received from %s." %(len(data), url))
    except Exception:
        print("error")

if __name__ == '__main__':
    urls = ['https://github.com/', 'https://blog.csdn.net/', 'https://www.hao123.com/']
    # 定义协程方法，传入函数和参数
    # 一个列表，传入多个任务
    greenlets = [gevent.spawn(run_task, url) for url in urls]
    print(greenlets)
    # 添加多个协程任务，并且启动运行
    gevent.joinall(greenlets)

# 查看运行结果可以发现，三个协程是同时触发的，但是结束顺序不同
# 网页请求的时间不同，故结束顺序不同
# 但是该程序其实只有一个线程



