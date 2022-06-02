from requests import *
from bs4 import BeautifulSoup
import re
para1={'term':'sepsis'}
kv = {'user-agent': 'Mozilla/5.0'}
r=get('https://pubmed.ncbi.nlm.nih.gov/',params=para1,headers=kv)
r.encoding=r.apparent_encoding
print(r.status_code)
print(r.request.url)
print(len(r.text))
demo=r.text
soup1=BeautifulSoup(demo,'html.parser')#1.BeautifulSoup是一个类，该类可以理解为HTML文档的全部内容。soup1是类中的一个对象，表示某一HTML文档的全部内容 2. html.parser是html解析器
for tag in soup1.find_all(name='a',attrs = {"data-ga-category": "result_click"}):#属性查找时要用字典形式
    print(tag)
'''for tag in soup1.find_all('b',string=re.compile('sepsis')):
    print(tag)'''