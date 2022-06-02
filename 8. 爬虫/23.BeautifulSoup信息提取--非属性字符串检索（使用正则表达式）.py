from requests import *
from bs4 import BeautifulSoup
import re
r=get("https://www.baidu.com")
r.encoding=r.apparent_encoding
demo=r.text
soup1=BeautifulSoup(demo,"html.parser")
'''
soup.find_all( name, attrs ,recursive ,string,**kwargs)
attrs:按属性进行检索
recursive :  是否对子孙全部检索，默认True
string:  在<>…</>即非属性字符串区域的检索字符串
'''
for tag in soup1.find_all(string=re.compile('百度')):#使用正则表达式寻找非属性字符串包含“百度”的标签（别忘了最开始impore re这一正则表达式库）
    print(tag)#这里把非属性字符串单独处理成标签
    print(tag.parent)