from tkinter import *
win=Tk()    # 注意Tk的大小写
win.title('GUI，你好呀')
win.geometry('800x600')
win['background']='red'#设置背景
label1=Label(win,text="你好，GUI")
button1=Button(win,text="这是第一个GUI界面呢")
button1['background']='green'
label1.pack()     #pack() 方法指示这个 Label 的大小为正好可以包裹其中的文字
button1.pack(side=TOP, expand=YES, fill=Y)#expand为是否随窗口的扩大而改变，fill为改变的话为横向X还是纵向Y填充
win.mainloop()