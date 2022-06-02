from requests import *
from bs4 import BeautifulSoup #bs4为小写
r=get("https://www.baidu.com")
r.encoding=r.apparent_encoding
demo=r.text
soup1=BeautifulSoup(demo,"html.parser")#用demo实例做一锅汤
print(soup1.find_all('a'))
for tag in soup1.find_all('a'):# find_all方法为查找某一个标签类型，find_all('a')为查找所有的a标签，别忘双引号
    print(tag.get('href'))#requests里面的get方法也可以对某一个标签使用（而非只能对整个网页）.