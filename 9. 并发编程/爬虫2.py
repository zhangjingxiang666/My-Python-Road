import requests
from bs4 import BeautifulSoup

urls=[
    f'https://www.cnblogs.com/#p{page}'
    for page in range(1, 50+1)#for循环是前闭后开区间
]
#print(urls)

def Web_Crawler(site_address):
    r=requests.get(site_address)
    #print(site_address,len(r.text))
    return r.text

def Parser(html):
    soup1=BeautifulSoup(html,'html.parser')
    links=soup1.find_all(name="a",class_='post-item-title')#查找所有类为post-item-title的a标签（即超链接标签）
    '''注意是class_，不是class，因为class是python的关键字，所以后面要加个尾巴，防止冲突'''
    return[
        (link['href'],link.get_text())
        for link in links#如果要一股脑全部输出的话，for循环要写在后面
    ]


if __name__=='__main__':
    for result in (Parser(Web_Crawler(urls[0]))):
        print(result)

