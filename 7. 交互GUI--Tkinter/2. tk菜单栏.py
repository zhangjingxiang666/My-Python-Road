from tkinter import *
def new():
    win2=Tk()
win=Tk()
win.title('标题')
win.geometry('300x200')
#下面开始设置菜单栏
menubar = Menu(win) #这是横向的那一大栏
win.config(menu=menubar)    #这是让那一大栏显示在win窗体上
filemenu1 = Menu(menubar, tearoff=0) #建立纵向的一小栏，命名为filemenu1
menubar.add_cascade(label='文件', menu=filemenu1)#命名filemenu1这一小栏的名字
filemenu1.add_command(label='新建',command=new)#命名filemenu1这一小栏点开的选项
filemenu1.add_command(label='退出',command=quit)#命名filemenu1这一小栏点开的选项
filemenu2 = Menu(menubar, tearoff=0)#建立纵向的第二小栏，命名为filemenu2
menubar.add_cascade(label='布局', menu=filemenu2)#命名filemenu2这一小栏的名字
filemenu2.add_command(label='编辑')#命名filemenu2这一小栏点开的选项
win.mainloop()
