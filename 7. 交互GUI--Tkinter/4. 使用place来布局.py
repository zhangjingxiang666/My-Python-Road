from tkinter import *
def buttonclick():
    button2.config(text='呜呜呜，你点我了')
win1=Tk()
button1=Button(win1,text='Hello, place')
button1.place(x=20,y=20,anchor=NW)#NW的意思为锚定点为西北，即左上
button2=Button(win1,text='我一直在中心',command=buttonclick)
button2.place(relx=0.5,rely=0.5,anchor=CENTER)#relx和rely代表相对整个窗口的位置，CENTER的意思为锚定点为中心
win1.mainloop()