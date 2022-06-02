import datetime
import time
import webbrowser
import tkinter.messagebox
from tkinter import *

def doSth():
    webbrowser.open("http://www.weather.com.cn/weather/101020100.shtml")#打开指定网页
    time.sleep(60)
    tkinter.messagebox.showwarning("快睡觉", '该回寝室睡觉啦！！！')
    mainloop()

def main(h=22, m=45):
    '''h表示设定的小时，m为设定的分钟'''
    while True:
        # 判断是否达到设定时间，例如0:00
        while True:
            now = datetime.datetime.now()
            # 到达设定时间，结束内循环
            if now.hour==h and now.minute==m:
                break

            # 不到时间就等20秒之后再次检测
            time.sleep(20)
        # 执行函数，一天做一次
        doSth()

main()



