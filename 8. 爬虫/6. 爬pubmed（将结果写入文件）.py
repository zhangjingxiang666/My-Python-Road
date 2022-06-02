from requests import *
para1={'term':'sepsis'}
kv = {'user-agent': 'Mozilla/5.0'}
r=get('https://pubmed.ncbi.nlm.nih.gov/',params=para1,headers=kv)
r.encoding=r.apparent_encoding
print(r.status_code)
print(r.request.url)
print(len(r.text))
path='D:/sepsis.txt'
with open(path,'w',encoding="utf-8") as f:      #with open(路径,'读写状态') as 赋值对象:   别忘了转化编码方式
    f.write(r.content.decode("utf-8"))          #对象.write(需要写入的属性)   别忘了转化编码方式