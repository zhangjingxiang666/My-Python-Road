from bs4 import BeautifulSoup
#import的时候用简称bs4！全称会报错！
#BeautifulSoup是一个类，该类可以理解为一个HTML文档的全部内容
from requests import *
r=get("https://www.baidu.com")
r.encoding=r.apparent_encoding
demo=r.text
soup1=BeautifulSoup(demo,'html.parser')  #1.BeautifulSoup是一个类，该类可以理解为一个HTML文档的全部内容 2. html.parser是html解析器
print(soup1.prettify())  # 使用prettify()格式化显示输出,加上换行符
print(demo)
#直接print出来是一串不分行的代码，但是使用bs4解析出来以后就是整齐的标签树了
