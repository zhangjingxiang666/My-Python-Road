from bs4 import BeautifulSoup
#import的时候用简称bs4！全称会报错！
#BeautifulSoup是一个类，该类可以理解为一个HTML文档的全部内容
from requests import *
r=get("https://www.baidu.com")
r.encoding=r.apparent_encoding
demo=r.text
soup1=BeautifulSoup(demo,'html.parser')  #1.BeautifulSoup是一个类，该类可以理解为一个HTML文档的全部内容 2. html.parser是html解析器
tag1=soup1.p
print(type(tag1))
print(type(tag1.attrs))
print(soup1.title)  #title指的是整个的title标签
print(soup1.p)
#任何存在于HTML语法中的标签都可以用 soup1.<Tag> 获得。例如，soup1.title就是获取soup1的标题；soup1.a就是获取soup1中的超链接（有多个时默认返回第一个）
'''关于HTML（BeautifulSoup）基本元素的简介：
<p class="title">........</p>整个被称为标签，是信息的基本组织单元
在上面一整个标签中：
p为标签的名字。格式：<Tag>.name   例如：soup1.p.name
class="title"为标签的属性。格式：<Tag>.attrs   例如：soup1.p.attrs
中间的......为标签内非属性字符串。格式：<Tag>.string 例如：soup1.p.string

理清几个层次：
BeautifulSoup是bs4库中的一个类
soup1是类里面的一个对象（就是整个HTML文档）
soup1.title、soup1.p、soup1.a等都是HTML里面的一整个一整个标签们
而标签又包括名字（name，文本格式）、属性（attrs，字典格式）、非属性字符串（string）和注释（command）
'''