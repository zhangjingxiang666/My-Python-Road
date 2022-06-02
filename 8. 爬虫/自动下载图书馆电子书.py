#coding=utf-8
from selenium import webdriver
from functools import reduce
import time
import re
from requests import *
from bs4 import BeautifulSoup
import tkinter.messagebox
from tkinter import *
import webbrowser
from tkinter import filedialog
import os

#windows文件名不支持？/等字符。此处定义函数把这些字符都替换成空格。否则后面书的文件名会出问题
def replace_char(s, oldChar, newChar ):
    return reduce(lambda s, char: s.replace(char, newChar), oldChar, s)

#避免同名书籍覆盖。同名pdf文件后面将加上数字编号，避免覆盖
def auto_save_file(path):
    directory, file_name = os.path.split(path)
    while os.path.isfile(path):
        pattern = '(\d+)\)\.'
        if re.search(pattern, file_name) is None:
            file_name = file_name.replace('.', '(0).')
        else:
            current_number = int(re.findall(pattern, file_name)[-1])
            if current_number ==-1:
                current_number=0
            new_number = current_number + 1
            file_name = file_name.replace(f'({current_number}).', f'({new_number}).')
        path = os.path.join(directory + os.sep + file_name)
    return path

#selenium模拟浏览器操作需要下载chromedriver.exe。此处为下载提示
root = Tk()
text = Text(root, width=34, height=10)
text.pack()
text.insert(INSERT, "请提前从此处下载好对应chrome版本的chromedriver.exe（整数版本号对应就行），并解压后放入python.exe所在的的文件夹中，否则程序将无法运行！\n\n弄好后即可关闭本窗口")
text.tag_add("link", "1.4", "1.6")
text.tag_config("link", foreground="blue", underline=True)
def click(event):
    webbrowser.open("http://chromedriver.storage.googleapis.com/index.html")
text.tag_bind("link", "<Button-1>", click)
root.mainloop()

#选择下载到的文件夹
root2 = Tk()
root2.withdraw()
tkinter.messagebox.showwarning("提示","请选择要下载到的文件夹，别选C盘。")
Folderpath = filedialog.askdirectory()   # 获得选择好的文件夹
print('Folderpath:', Folderpath)  # 输出文件夹路径
root2.destroy()

# 创建下载失败的书的名单
txtpath = Folderpath+'\\下载失败书的名单.txt'
if os.path.exists(txtpath):
	print('exist')
else:
    file = open(txtpath, 'w')
    file.write('以下是未下载成功的书的名单。请手动下载\n')
    file.close()

#开始模拟浏览器操作
opt = webdriver.ChromeOptions()   #创建浏览
# opt.set_headless()    #无窗口模式
# driver.minimize_window()   #最小化浏览器窗口
driver = webdriver.Chrome(options=opt)  #创建浏览器对象
driver.get('http://192.168.89.246:9088/front/book/search/page?stype=1&channeltype=100&cls=0A') #打开网页

root = Tk()
root.withdraw()
tkinter.messagebox.showwarning("提示","请在弹出的浏览器左侧选择你想要下载的图书分类。\n\n如果想全部下载，请在上方搜索框输入'<'，并取消勾选“当前分类检索”，然后点“搜索。\n\n推荐下载 文学-各国文学。里面有各种世界名著、小说。\n\n选好分类后请点“确定”")
tkinter.messagebox.showwarning("提示","即将开始，请勿关闭python和chrome窗口。\n\n嫌碍事的话可以先把他俩最小化，下完最后一本书后手动关闭即可\n\n点“确定”继续")

#从网页源码中解析下载链接
while True:
    try:
        time.sleep(2)     #加载等待
        page = driver.page_source  # 获取源码
        soup1 = BeautifulSoup(page, 'html.parser')  # 解析源码
        content1 = soup1.find('ul', class_='recom_list')  # 定位到检索列表标签

        a=""
        content2 = None
        for tag in content1.find_all(name='a'):
            try:
                url=tag.get('href')#print(tag.get('href'))#requests里面的get方法也可以对某一个标签使用（而非只能对整个网页）。另外注意是href，别拼写错了。
                bookname = tag.get('title')#书名
                # 每本书下载链接在网页里有两条，所以得去重。此外，最后两个不是下载链接的javascript也得去掉。
                if (url == a):#如果上一条下载链接和这一条下载链接重复，则跳出本次循环
                    continue
                if(url=='javascript:;'):#如果碰到了javascript，则跳出大循环
                    break
                a=url
                realurl = 'http://192.168.89.246:9088' + url#真正的下载链接要加上前面的ip地址
                print(realurl)
                print('正在下载  '+bookname)
                bookname = replace_char(bookname, '?\/*"<>|¬', '')#替换文件名中的非法字符
                myfile = get(realurl, allow_redirects=True)#允许下载链接自动跳转
                #open('E:/'+bookname+'.pdf','wb').write(myfile.content)
                #open(Folderpath + '\\'+bookname + '.pdf', 'wb').write(myfile.content)
                pathname = Folderpath + '\\' + bookname + '.pdf'
                open(auto_save_file(pathname), 'wb').write(myfile.content)
            except:
                txt_add = open(txtpath, 'a')
                txt_add.write(bookname+'\n')
                txt_add.close()
                continue
        content2 = content1.find('a', class_='layui-laypage-next layui-disabled')
        if content2 != None:
            break
        driver.find_element_by_class_name('layui-laypage-next').click()  # 自动点击翻页按钮

    except:
        continue

root = Tk()
root.withdraw()
tkinter.messagebox.showwarning("提示", "下载完成！")
