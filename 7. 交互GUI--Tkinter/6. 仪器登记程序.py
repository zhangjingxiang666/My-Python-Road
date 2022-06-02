from tkinter import *
import time
import csv
import subprocess

win1=Tk()
win1.title('请登记')
win1.geometry('800x600')    #注意用×这个乘号，不要用星号！

def hide_widget(widget):
   widget.pack_forget()


label6=Label(win1,text='请完整填写')
label6.configure(font=('Ariel',1),fg='Red')
label6.place(relx=0.5,rely=0.8,anchor=CENTER)


label1=Label(win1,text='姓名')    #注意别忘了text=这个东西
label1.configure(font=('Ariel',15))
label1.place(relx=0.5,rely=0.2,anchor=CENTER)   #anchor为小写！
label1.bind("<Button-1>",lambda e:zjx())
textbox1=Text(win1)
textbox1.place(width=100, height=50,relx=0.5,rely=0.3,anchor=CENTER)  # width:长度；height:高度

label2=Label(win1,text='教研室')
label2.place(relx=0.5,rely=0.5,anchor=CENTER)
label2.configure(font=('Ariel',15))
textbox2=Text(win1)
textbox2.place(width=100, height=50,relx=0.5,rely=0.6,anchor=CENTER)


def zjx():
    user_name='张景翔'#姓名
    print(user_name)
    user_affilation='军特药'#教研室
    print(user_affilation)
    use_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    row = [user_name, user_affilation, use_time]
    out = open("使用记录.csv", "a", newline="")
    csv_writer = csv.writer(out, dialect="excel")
    csv_writer.writerow(row)
    subprocess.Popen('C:\\Windows\\System32\\calc.exe')
    win1.quit()

def xxh():
    user_name='邢信昊'#姓名
    print(user_name)
    user_affilation='军特药'#教研室
    print(user_affilation)
    use_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    row = [user_name, user_affilation, use_time]
    out = open("使用记录.csv", "a", newline="")
    csv_writer = csv.writer(out, dialect="excel")
    csv_writer.writerow(row)
    subprocess.Popen('C:\\Windows\\System32\\calc.exe')
    win1.quit()

def lzy():
    user_name='凌忠毅'#姓名
    print(user_name)
    user_affilation='军特药'#教研室
    print(user_affilation)
    use_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    row = [user_name, user_affilation, use_time]
    out = open("使用记录.csv", "a", newline="")
    csv_writer = csv.writer(out, dialect="excel")
    csv_writer.writerow(row)
    subprocess.Popen('C:\\Windows\\System32\\calc.exe')
    win1.quit()

def main():
    user_name=str(textbox1.get('0.0','end'))#姓名
    print(user_name)
    user_affilation=str(textbox2.get('0.0','end'))#教研室
    print(user_affilation)
    use_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    if len(user_name)>2 and len(user_affilation)>2:#似乎什么都不填，承接下来也有一个字符。所以判断是否大于一个字符串的长度为大于2而不是大于1.
        # 写：追加
        row = [user_name, user_affilation, use_time]
        out = open("使用记录.csv", "a", newline="")
        csv_writer = csv.writer(out, dialect="excel")
        csv_writer.writerow(row)
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')
        win1.quit()
    else:
        #quit()
        label6.configure(font=('Ariel', 60), fg='Red')



button1=Button(win1,text='确定',command=main)
button1.place(width=160, height=30,relx=0.8,rely=0.5,anchor=CENTER)

label3=Label(win1,text='请')
label3.configure(font=('Ariel',30))
label3.place(relx=0.4,rely=0.1,anchor=CENTER)


label4=Label(win1,text='登')
label4.configure(font=('Ariel',30))
label4.place(relx=0.5,rely=0.1,anchor=CENTER)
label4.bind("<Button-1>",lambda e:xxh())

label5=Label(win1,text='记')
label5.configure(font=('Ariel',30))
label5.place(relx=0.6,rely=0.1,anchor=CENTER)
label5.bind("<Button-1>",lambda e:lzy())

win1.mainloop()