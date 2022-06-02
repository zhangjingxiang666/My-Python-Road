from tkinter import *
import webbrowser

def open_url():
   quit()

win1=Tk()
win1.title('请登记')
win1.geometry('800x600')    #注意用×这个乘号，不要用星号！
url= 'https://www.tutorialspoint.com/'

label1=Label(win1,text='姓名')    #注意别忘了text=这个东西
label1.configure(font=('Ariel',15))
label1.place(relx=0.5,rely=0.2,anchor=CENTER)   #anchor为小写！
label1.bind("<Button-1>",lambda e:open_url())#这里需要个lamda函数
label1.pack()

win1.mainloop()
