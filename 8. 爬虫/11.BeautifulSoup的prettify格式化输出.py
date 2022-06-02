from bs4 import BeautifulSoup
#import的时候用简称bs4！全称会报错！
#BeautifulSoup是一个类，该类可以理解为一个HTML文档的全部内容
from requests import *
r=get("https://www.baidu.com")
r.encoding=r.apparent_encoding
demo=r.text
soup1=BeautifulSoup(demo,'html.parser')  #1.BeautifulSoup是一个类，该类可以理解为一个HTML文档的全部内容 2. html.parser是html解析器
print(soup1.prettify())  # 使用prettify()格式化显示输出。prettify()可以加换行符，使更加友好
tag1=soup1.a
print(tag1)
print(tag1.prettify())