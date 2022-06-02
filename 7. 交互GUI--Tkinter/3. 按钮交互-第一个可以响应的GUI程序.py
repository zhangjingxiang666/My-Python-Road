#点button2，button1响应
from tkinter import *
win = Tk()
button1=Button(win,text="OK",fg="red")
def button1process():
    button1.config(text="你点按钮啦~")
def main():
    button2 = Button(win, text="OK2", fg="blue", command=button1process)
    button1.pack()
    button2.pack()
    win.mainloop()
main()