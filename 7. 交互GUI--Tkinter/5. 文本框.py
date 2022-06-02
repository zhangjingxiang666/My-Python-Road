from tkinter import *
win1=Tk()
win1.title('计算平抛飞行')
win1.geometry('800x600')    #注意用×这个乘号，不要用星号！
label1=Label(win1,text='请输入初速度')    #注意别忘了text=这个东西
label1.place(x=50,y=50,anchor=NW)   #anchor为小写！
textbox1=Text(win1)
textbox1.place(width=100, height=50,x=50,y=80)  # width:长度；height:高度

def main():
    a=textbox1.get('0.0','end')
    print(a)

label2=Label(win1,text='请输入飞行时间')
label2.place(relx=0.5,rely=0.5,anchor=CENTER)
textbox2=Text(win1)
textbox2.place(width=100, height=50,relx=0.5,rely=0.6,anchor=CENTER)
label3=Label(win1,text='还没计算呢')
label3.place(relx=0.8,rely=0.65,anchor=CENTER)
button1=Button(win1,text='点击输出文本框一的内容',command=main)
button1.place(width=160, height=30,relx=0.8,rely=0.5,anchor=CENTER)


win1.mainloop()