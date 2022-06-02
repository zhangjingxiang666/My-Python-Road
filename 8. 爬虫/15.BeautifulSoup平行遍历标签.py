from bs4 import BeautifulSoup
from requests import *
r=get("https://python123.io/ws/demo.html")
r.encoding=r.apparent_encoding
demo=r.text
soup1=BeautifulSoup(demo,'html.parser')
tag1=soup1.a.previous_sibling   #上一个标签或非标签字符串（例如and之类的）
print(tag1)
tag2=soup1.a.next_sibling   #下一个标签或非标签字符串
print(tag2)
for i in soup1.a.next_siblings: #next_siblings是下面所有的标签或非标签字符串，为迭代类型，只能用到循环中
    print(i)