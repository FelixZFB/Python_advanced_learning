# 由于IO操作非常耗时，程序经常会处于等待状态
# 比如请求多个网页有时候需要等待，gevent可以自动切换协程
# 遇到阻塞自动切换协程，程序启动时执行monkey.patch_all()解决
# 多个协程，可以采用pool管理并发数，限制并发任务数

from gevent import monkey
monkey.patch_all()
from urllib import request
from gevent.pool import Pool

def run_task(url):
    print("Visit --> %s" % url)
    try:
        response = request.urlopen(url)
        data = response.read()
        print("%d bytes received from %s." %(len(data), url))
    except Exception:
        print("error")
    return 'url:%s -->finish' % url

if __name__ == '__main__':
    pool = Pool(2)
    urls = ['https://github.com/', 'https://blog.csdn.net/', 'https://bbs.csdn.net/']
    # 协程池执行任务
    results = pool.map(run_task, urls)
    # 打出结果，打出上面返回的结果
    # map最终返回的值是一个列表，就是每个任务执行完成之后的返回值
    print(results)

# 查看运行结果可以发现，先访问了两个网址
# 第一个协程执行完毕后，开始第三个协程
# 最终的结果为每次任务执行完成后返回值，组成的一个列表
# 可以查看map帮助



