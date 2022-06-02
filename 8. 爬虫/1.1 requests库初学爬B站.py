from requests import *
r=get('http://www.bilibili.com')
print(r.encoding)
print(r.text)