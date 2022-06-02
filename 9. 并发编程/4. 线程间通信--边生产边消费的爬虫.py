'''
多组件pipline技术架构：复杂步骤一步步完成。处理器1➡中间数据➡处理器2➡中间数据➡......。
这样的好处是可以为生产者和消费者配制不同的线程；可以将生产者和消费者分给不同的人开发
'''

'''
多线程之间的数据通信：queue.Queue()的使用:
1. 导入类库
import queue
2. 创建Queue
q=queue.Queue()
3.为queue里面添加元素
q.put(item)
4. 从queue里面获取元素
item=q.get()
阻塞的：当里面没有元素的时候，q.get()会卡住；当里面满的时候，q.put(item)会卡住
5. 查询状态
查看元素多少：q.qsize()
判断是否为空：q.empty()
判断是否已满：q.full()
'''
import queue
import 爬虫2
import time
import random
import threading

def main():
    '''先创建存储爬取网址的队列'''
    global url_queue    #global声明全局变量，否则后面的函数用不了
    url_queue = queue.Queue()
    '''再创建存储爬取完成待解析的html页面的队列'''
    global html_queue
    html_queue = queue.Queue()
    global url  #url是 爬虫2.py 文件里面所定义的网址
    for url in 爬虫2.urls:    #遍历字符串是for...in...不带range
        url_queue.put(url)  #将每条网址放进爬取队列里面

    for idx in range(3):#启动3个线程来爬取。爬取函数为后续定义的Crawing
        t=threading.Thread(target=Crawing,args=(url_queue,html_queue),name=f"爬取线程{idx}")
        t.start()

    file=open("网页链接标题.txt","w") #新建一个txt文档来存放解析结果
    for idx in range(2):#启动2个线程来解析。解析函数为后续定义的Parsing
        t=threading.Thread(target=Parsing,args=(html_queue,file),name=f"解析线程{idx}")
        t.start()

#负责爬取的函数，生产者
'''定义一个函数Crawing,其参数为url_queue作为输入，html_queue作为输出。两个参数的类型均为queue.Queue'''
def Crawing(url_queue:queue.Queue,html_queue:queue.Queue):#冒号后面是声明类型，类型都是队列queue.Queue
    while True:
        WebAddress=url_queue.get()  #从url_queue这个队列里面获取元素作为WebAddress网址
        html=爬虫2.Web_Crawler(WebAddress)    #使用爬虫2.py里面的Web_Crawler函数解析WebAddress网址
        html_queue.put(html)    #将爬取的结果放入进html_queue中

        time.sleep(random.randint(1,2))
        print(threading.current_thread().name,f"正在爬取{WebAddress}","待爬取的网址队列元素数量为",url_queue.qsize())

#负责解析的函数，消费者
def Parsing(html_queue:queue.Queue,file):
    while True:
        html=html_queue.get()   #从html_queue这个队列里面获取元素作为解析的页面
        results=爬虫2.Parser(html)    #使用爬虫2.py里面的Parser函数解析html页面
        for result in results:
            file.write(str(result)+"\n")#换行 #将解析结果写入文档

        print(threading.current_thread().name, f"正在解析{url}", "爬取完待解析的元素数量为", html_queue.qsize())
        time.sleep(random.randint(1, 2))

if  __name__=='__main__':
    main()






