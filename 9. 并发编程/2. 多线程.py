'''CPU密集型使用多进程；IO密集型使用多线程；此外还有多协程，是函数的异步执行'''
'''Python中有全局解释器锁（GIL），即只有一个线程真正在占用CPU运行，其他线程只有利用别的线程IO的空隙才能执行'''
'''python创建多线程的方法：
1. 准备一个函数 
def myfunc(a,b)
    doSth(a,b)
2. 创建多个线程
import threading
t1=threading.thread(target=myfunc,args=(1,2)）
3. 启动线程
t1.start()
4. 等待结束(可选）
t1.join()

'''
from threading import Thread
from time import time,sleep
from random import randint

def Downloadtask(videoname):
    print('开始下载{0}'.format(videoname))
    sleep(randint(2,5))#模拟下载时间
    print('完成下载{0}'.format(videoname))

def main():
    starttime = time()
    T1=Thread(target=Downloadtask,args=('a.mp4',))#  如果只有一个参数的话，后面一定别忘加逗号！！！因为args里面放的是元组型数据。不加逗号的话会当成字符串处理而报错
    T1.start()
    '''start() 的意思是开始这个线程'''
    T2 = Thread(target=Downloadtask, args=('b.mp4',))
    T2.start()
    T3 = Thread(target=Downloadtask, args=('c.mp4',))
    T3.start()
    '''至此已经有三个线程在运行中。即：把这三个进程都开启后就继续执行下面的代码'''

    '''join()的意思是等待进程执行完成。
    如果不join的话,上面三个进程在后台继续跑着，就已经开始执行后续的代码了
    join()了之后就是，等待三个进程跑完，再执行后续的代码。
    可以把join()注释掉看一下差别'''
    T1.join()
    T2.join()
    T3.join()
    endtime = time()
    duringtime = endtime - starttime
    print('总共花费时间', duringtime)

if __name__=='__main__':
    main()

