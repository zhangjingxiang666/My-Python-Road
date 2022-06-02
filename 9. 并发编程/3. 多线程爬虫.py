import 爬虫1
import threading
import time

def single_thread():
    for url in 爬虫1.urls:    #for...in...是遍历字符串，不用加range
        爬虫1.Web_Crawler(url)

def multi_thread():
    threads=[]
    for url in 爬虫1.urls:    #先用一个循环来创建进程组
        t=threading.Thread(target=爬虫1.Web_Crawler,args=(url,))
        threads.append(t)
    for t in threads:   #再用一个循环来开始进程
        t.start()
    for t in threads:   #最后用一个循环来等待进程结束（阻塞）
        t.join()

if __name__=='__main__':
    time1=time.time()
    single_thread()
    time2 = time.time()
    print('单线程所花的时间为',time2-time1)
    time3 = time.time()
    multi_thread()
    time4 = time.time()
    print('多线程所花的时间为',time4 - time3)

