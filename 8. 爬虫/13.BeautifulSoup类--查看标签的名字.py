from bs4 import BeautifulSoup
from requests import *
r=get('https://www.icourse163.org/')
r.encoding=r.apparent_encoding
demo=r.text
soup1=BeautifulSoup(demo,'html.parser')

#获得标签中超链接的名字信息
print(soup1.a.name)

#看看a的上一级标签是什么
print(soup1.a.parent.name)

#看看a的上上级标签是什么
print(soup1.a.parent.parent.name)
