import time
import random

def Downloadtask(videoname):
    print('开始下载',videoname)
    time.sleep(random.randint(5,10))#模拟下载期间所花费的时间
    print("下载结束",videoname)

def Main():
    starttime=time.time()
    Downloadtask('a.mp4')
    Downloadtask('b.mp4')
    Downloadtask('c.mp4')
    endtime=time.time()
    duringtime=endtime-starttime
    print('总共花费时间',duringtime)

if __name__=='__main__':
    Main()
