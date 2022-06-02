from requests import *
from bs4 import BeautifulSoup
r=get("https://www.qq.com")
r.encoding=r.apparent_encoding
demo=r.text
soup1=BeautifulSoup(demo,"html.parser")
'''
soup.find_all( name, attrs ,recursive ,string,**kwargs)
attrs:按属性进行检索
'''
for tag in soup1.find_all(name='a',attrs={"target":"_blank"}):#属性查找时要用字典形式
    print(tag.get('href'))
#查找名称为a且属性里面的target属性为_blank的标签。别忘引号。另外因为属性有多个键值对，所以直接输键值对的名称和对应的值即可，无需再输attrs本身