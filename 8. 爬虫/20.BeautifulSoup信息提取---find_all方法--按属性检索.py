from requests import *
from bs4 import BeautifulSoup
r=get("https://www.qq.com")
r.encoding=r.apparent_encoding
demo=r.text
soup1=BeautifulSoup(demo,"html.parser")
'''
soup.find_all( name, attrs ,recursive ,string,**kwargs)
attrs:按属性进行检索
recursive :  是否对子孙全部检索，默认True
string:  在<>…</>即非属性字符串区域的检索字符串
'''
print(soup1.find_all(name='a',attrs = {"target": "_blank"}))
#查找所有属性里面的target为_blank的标签。别忘引号。属性用字典形式
#可以直接print含有这个属性的列表


for tag in soup1.find_all(target="_blank"):
    print(tag.name)
#也可以在这个列表里进行搜索



