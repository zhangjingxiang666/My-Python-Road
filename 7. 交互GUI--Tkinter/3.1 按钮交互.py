from tkinter import *
win=Tk()

def button1process():
    button1.config(text="你点击了")

button1=Button(win,text="你没点呢",command=button1process) #注：调用定义的函数，后面不带括号时，调用的是这个函数本身 ，是整个函数体，是一个函数对象，不须等该函数执行完成; 二、带括号（参数或者无参），调用的是函数的执行结果，须等该函数执行完成的结果
button1.pack()
win.mainloop()