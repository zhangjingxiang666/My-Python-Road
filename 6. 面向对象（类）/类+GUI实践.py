from tkinter import *
class Qianqiu:
    def __init__(self,v0,t):
        self.x=v0*t
        self.y=-0.5*9.8*t*t

def getinputs():
    a=int(textbox1.get('0.0','end'))
    b=int(textbox2.get('0.0','end'))
    return a,b

def main():
    v0, t = getinputs()
    Object1 = Qianqiu(v0, t)
    print('在%s秒后铅球的位置为%s,%s' % (t, Object1.x, Object1.y))
    label3.config(text='在%s秒后铅球的位置为%s,%s'% (t, Object1.x, Object1.y))

win1=Tk()
win1.title('计算平抛飞行')
win1.geometry('800x600')    #注意用×这个乘号，不要用星号！
menubar = Menu(win1) #这是横向的那一大栏
win1.config(menu=menubar)    #这是让那一大栏显示在win窗体上
filemenu1 = Menu(menubar, tearoff=0) #建立纵向的一小栏，命名为filemenu1
menubar.add_cascade(label='文件', menu=filemenu1)#命名filemenu1这一小栏的名字
filemenu1.add_command(label='退出',command=quit)#命名filemenu1这一小栏点开的选项
label0=Label(win1,text='平抛计算器',font=("微软雅黑", 24))    #注意别忘了text=这个东西
label0.place(x=400,y=100,anchor=CENTER)   #anchor为小写！
label1=Label(win1,text='请输入初速度')    #注意别忘了text=这个东西
label1.place(x=50,y=50,anchor=NW)   #anchor为小写！
textbox1=Text(win1)
textbox1.place(width=100, height=50,x=50,y=80)  # width:长度；height:高度
label2=Label(win1,text='请输入飞行时间')
label2.place(relx=0.5,rely=0.5,anchor=CENTER)
textbox2=Text(win1)
textbox2.place(width=100, height=50,relx=0.5,rely=0.6,anchor=CENTER)
label3=Label(win1,text='还没计算呢')
label3.place(relx=0.8,rely=0.65,anchor=CENTER)
button1=Button(win1,text='点击开始计算',command=main)
button1.place(width=160, height=30,relx=0.8,rely=0.5,anchor=CENTER)
win1.mainloop()


