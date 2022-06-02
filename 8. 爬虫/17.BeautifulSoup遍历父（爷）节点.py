from bs4 import BeautifulSoup
from requests import *
r=get("https://www.baidu.com")
r.encoding=r.apparent_encoding
demo=r.text
soup1=BeautifulSoup(demo,'html.parser')
print(soup1.title.parent.name)  #打印soup1中title标签的父标签的名字
parentSets=soup1.a.parents
#若parents为迭代形式显示所有长辈（父、爷....)标签。若只有parent则只有父标签
for i in parentSets:
    if i==None: #因为最后上行遍历会遍历到soup1本身，而soup1是没有父标签的，所以需要有一个判断
        print(i)
    else:
        print(i.name)