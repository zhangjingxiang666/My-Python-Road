from bs4 import BeautifulSoup
from requests import *
#r=get('https://python123.io/ws/demo.html')
r=get('https://www.baidu.com')
r.encoding=r.apparent_encoding
demo=r.text
soup1=BeautifulSoup(demo,'html.parser')
tag1=soup1.a
print(tag1)
print(tag1.string)
#tag1.string表示标签内的非属性字符串