from requests import *
from bs4 import BeautifulSoup
r=get("https://www.baidu.com")
r.encoding=r.apparent_encoding
demo=r.text
soup1=BeautifulSoup(demo,"html.parser")
'''
soup.find_all( name, attrs ,recursive ,string,**kwargs)
name:按名称进行检索
'''
for tag in soup1.find_all(name='a'):
    print(tag)
    print(tag.get('href'))#requests里面的get方法也可以对某一个标签使用（而非只能对整个网页）。另外注意是href，别拼写错了。
for tag in soup1.find_all(name=True):#如果是name=True,则返回所有有名字的标签
    print(tag.name)



