from bs4 import BeautifulSoup
from requests import *
r=get('https://www.icourse163.org/')
r.encoding=r.apparent_encoding
demo=r.text
soup1=BeautifulSoup(demo,'html.parser')

#获得标签的属性
tag1=soup1.a #a表示超链接的标签
print(tag1)
print(tag1.attrs)#直接获得标签的属性为一个字典格式
print(tag1.attrs['href'])#可以获得标签的属性这一字典中的某一项

