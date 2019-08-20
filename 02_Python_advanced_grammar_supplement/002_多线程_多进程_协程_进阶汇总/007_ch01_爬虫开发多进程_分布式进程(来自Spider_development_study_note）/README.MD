# Python爬虫开发与项目实战(学习笔记)

- This project is a study note of Spider Development ans Project Training.
- 本项目是爬虫开发与项目实战的学习笔记.

- 前面几章很多都是学习过的内容，快速浏览
- 参考书本和TLXY_study_note中的内容


# 1 第一章 回顾Python编程
- 案例放置在ch01之中

## 1.4 进程与线程

- 进程与线程的区别

- 进程：程序运行的一个状态
    - 包含地址空间，内存，数据栈
    - 每个进程有自己独立的运行环境
    - 多进程共享数据是一个问题

- 线程
    - 一个进程的独立运行片段，一个进程可以有多个线程
    - 轻量化的进程
    - 一个进程的多个线程共享数据和上下文运行环境
    - 共享互斥问题

- 多进程使用multiprocessing模块
- 多线程使用threading模块
    
 
### 1.4.1 多进程
- 使用multiprocessing模块创建多进程
    - 使用multiprocessing模块中的Process创建少量的多进程
    - 创建子进程，函数只需要执行函数的名称和执行函数的参数即可
    - 参考实例1.4.1 

- 大量进程，上千上万个进程使用multiprocessing模块中的Pool类
    - 创建进程池对象
    - Pool默认的进程数量是CPU的核数或者规定的进程数量
    - 如果池中的进程没有满，就会自动创建进程
    - 如果池中已满或者达到规定数量，进程就会等待，池中进程结束一个，才会创建新的进程 
    - 先创建Pool()实例，然后用apply_async()创建子进程
    - 进程池使用join()函数之前，需要先调用close()函数，然后所有任务就自动开始了，关闭某个进程
    - 相对于Process,不需要执行start()函数
    - 使用用close()之后，就不能再添加Process子进程了
    - 然后下一个进程在开始进程，具体参考实例
    - 参考实例1.4.2

- 进程之间的通信
    - 两个进程使用Pipe
    - 多个进程使用Queue
    - Queue实际就是一个安全队列
    - Queue提供了一个基本的FIFO容器,
    - Queue有两个方法Put和Get
    - put()方法向容器中存入数据，按顺序存入
    - get()方法从容器中取出数据，按循序取出
    - 参考实例1.4.3/1.4.4

- 队列补充知识：
    - queue.Queue()
    - 基本队列，先进先出
    - 参考1.4.3_1
    - LIFO队列，后进先出
    - 参考1.4.3_2

- multiprocessing.Queue()和queue.Queue()的区别
    - 参考：https://blog.csdn.net/u011318077/article/details/88089843
    - 参考：https://www.cnblogs.com/itogo/p/5635629.html
     
    
### 1.4.2 多线程
- threading模块
- 方法1：创建Thread实例
- 方法2：直接继承threading.Thread类
- 参考书中案例
- 参考TLXY_study_note中的高级语法，多线程

### 1.4.3 协程
- 可以使用yield生成器实现
- 推荐使用gevent包,用于请求访问多个网址或者网络请求
- 使用gevent.spawn和gevent.joinall方法添加启动多个协程
- 参考实例1.4.5

- 处理大量的网络请求和并发出处理
- gevent提供的池，对并发数进行管理限制
- 使用pool.map执行任务
- 参考实例1.4.6

### 1.4.4 分布式进程
- multiprocessing模块
- managers子模块支持把多个进程分布到多台机器上
- 可以写一个服务进程作为调度者，将任务分布到其它多个进程中，然后通过网络通信进行管理
- 比如爬取图片：一般一个进程负责抓取图片的地址，将地址放在Queue（容器）队列中
- 另外一个进程负责从Queue队列中取出链接地址进行图片下载和存储到到本地
- 上述爬取图片的过程就可以做成分布式，一台机器负责获取链接，另外一台机器负责下载存储
- 上述问题核心：将Queue队列暴露到网络中，让其他机器可以访问

- 分布式进程的步骤
    - 建立Queue队列,负责进程之间的通信，任务队列task_queue,结果队列result_queue
    - 把第一步中的两个队列在网络中注册,注册时候将队列重新命名
    - 创建一个Queuemanager(BaseManager)的实例manager，相当于一个服务器，给定IP地址、端口和验证码
    - 启动实例manager
    - 访问Queue对象，即创建网络中暴露重命名后的Queue实例
    - 创建任务到本地队列中，自动上传任务到网络队列中，分配给任务进程进行处理
    - 任务进程先从网络中任务队列中取出任务，然后执行，将执行结果放入到网络中的结果队列中
    - 服务进程从结果队列中取出结果，直到执行完所有任务和取出所有的结果，任务进程关闭，然后服务进行关闭

- 先创建服务进程，再创建任务进程
- 参考实例1.4.7 1.4.8 运行正常
-
- 案例补充知识
- 知识补充1
    当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，但是，在分布式多进程环境下，
    添加任务到Queue不可以直接对原始的task_queue进行操作，那样就绕过了QueueManager的封装，
    必须通过manager.get_task_queue()获得的Queue接口添加。
    然后，在另一台机器上启动任务进程（本机上启动也可以）

- 知识补充2
    其中task_queue和result_queue是两个队列，分别存放任务和结果。它们用来进行进程间通信，交换对象。
    因为是分布式的环境，放入queue中的数据需要等待Workers机器运算处理后再进行读取，
    QueueManager.register(‘get_task_queue’, callable=return_task_queue)
    QueueManager.register(‘get_result_queue’, callable=return_result_queue)
    这样就需要对queue用QueueManager进行封装放到网络中，这是通过上面的2行代码来实现的。
    我们给return_task_queue的网络调用接口取了一个名get_task_queue,
    而return_result_queue的名字是get_result_queue，
    方便区分对哪个queue进行操作。task.put(n)即是对task_queue进行写入数据，
    相当于分配任务。而result.get()即是等待workers机器处理后返回的结果。

- 知识补充3
    这个简单的Master/Worker模型有什么用？其实这就是一个简单但真正的分布式计算，把代码稍加改造，
    启动多个worker，就可以把任务分布到几台甚至几十台机器上，
    比如把计算n*n的代码换成发送邮件，就实现了邮件队列的异步发送。
    Queue对象存储在哪？注意到task_worker.py中根本没有创建Queue的代码，
    所以，Queue对象存储在taskManager.py进程中：
    参考图片分布式进程
    
    而Queue之所以能通过网络访问，就是通过QueueManager实现的。
    由于QueueManager管理的不止一个Queue，所以，要给每个Queue的网络调用接口起个名字，
    比如get_task_queue。taskWorker这里的QueueManager注册的名字必须和taskManager中的一样。
    对比上面的例子，可以看出Queue对象从另一个进程通过网络传递了过来。
    只不过这里的传递和网络通信由QueueManager完成。

    authkey有什么用？这是为了保证两台机器正常通信，不被其他机器恶意干扰。
    如果task_worker.py的authkey和taskManager.py的authkey不一致，肯定连接不上。
    
    参考文章：https://blog.csdn.net/u011318077/article/details/88094583 
    

    
## 1.5 网络编程
- TCP协议：服务器端与客户端要建立可靠的连接
- UDP协议：服务器端与客户端不需要建立连接
- 参考书本内容和TLXY_study_note中的高级语法，网络编程