from requests import *
#import的时候用简称bs4！全称会报错！
from bs4 import BeautifulSoup
#BeautifulSoup是一个类，该类可以理解为一个HTML文档的全部内容
#B要和S都要大写
r=get("https://www.baidu.com")
r.encoding =r.apparent_encoding
demo=r.text
soup1=BeautifulSoup(demo,'html.parser')#1.BeautifulSoup是一个类，该类可以理解为HTML文档的全部内容。soup1是类中的一个对象，表示某一HTML文档的全部内容 2. html.parser是html解析器
for everylink in soup1.find_all('a'):#<a>.....</a>表示含有超链接的标签
    print(everylink.get('href'))

