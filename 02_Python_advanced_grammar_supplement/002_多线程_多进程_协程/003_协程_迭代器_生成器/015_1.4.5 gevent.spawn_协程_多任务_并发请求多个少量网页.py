# 由于IO操作非常耗时，程序经常会处于等待状态
# 比如请求多个网页有时候需要等待，gevent可以自动切换协程

# 遇到阻塞自动切换协程，程序启动时执行monkey.patch_all()即可自动切换

# 首行添加下面的语句即可，如果没有，则会变成单任务，一个请求阻塞后
# 得到结果后，才会进行下一个网页请求，可以将首行注释掉，然后查看运行结果
# 都是一个网页请求完了，才开始下一个
# monkey.patch_all()相当于给代码打了一个补丁，只要遇到任何延时操作就可以自动切换
# 014案例gevent.sleep(1)如果换成time.sleep(1)就不行了
# monkey.patch_all()会把所有代码读一遍，延时操作自己更换为gevent.sleep延时


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
    # 一个列表，传入多个任务，一次添加多个任务
    # spawn传入函数名和参数
    greenlets = [gevent.spawn(run_task, url) for url in urls]
    # 打印出多个任务的名称
    print(greenlets)
    # 添加多个协程任务，并且启动运行
    # joinall接收一个多任务列表
    gevent.joinall(greenlets)

# 查看运行结果可以发现，三个协程是同时触发的，但是结束顺序不同
# gevent一大特点就是遇到延时会自动切换任务
# 网页请求的时间不同，故结束顺序不同
# 但是该程序其实只有一个线程，但是多个任务再相互切换运行



