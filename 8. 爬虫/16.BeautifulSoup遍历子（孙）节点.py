from bs4 import BeautifulSoup
from requests import *
r=get('https://www.qq.com/')
r.encoding=r.apparent_encoding
demo=r.text
soup1=BeautifulSoup(demo,'html.parser')#把获取的页面熬成一锅由标签树组成的汤
content0=soup1.body.contents    #.contents为列表类型，指的是下一层（儿子）标签
print(content0)
def main1():
    content1=soup1.body.children    #children指的只有body标签的下一层（儿子）标签，为迭代类型，只能用到循环中
    for child in content1:
        print(child)
        print("下一个标签是")

def main2():
    content2=soup1.body.descendants     #descendants指的是子子孙孙标签，为迭代类型，只能用到循环中
    for child in content2:
        print(child)
        print("下一个标签是")

a=eval(input("想只遍历子标签就输入1，想子子孙孙都遍历就输入2"))
if a==1:
    main1()
if a == 2:
    main2()

