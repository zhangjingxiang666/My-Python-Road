from requests import *
url='http://img0.dili360.com/pic/2020/04/16/5e9817e9973c35i20842721_t.jpg'
path='D:/abc.jpg'
r=get(url)
with open(path,'wb') as f:      #with open(路径,'读写状态') as 赋值对象:
    f.write(r.content)          #对象.write(需要写入的属性)
f.close()