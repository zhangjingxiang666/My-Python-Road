from requests import *
r=get('http://www.baidu.com')#r=get('URL'),别忘了URL前面的http://
print(r.status_code)#status_code为200表示成功
r.encoding=('utf-8')#r.encoding从页面头部的charset获取到的编码方式,如果没有，则默认用ISO ‐8859‐1输出。
print(r.apparent_encoding)#r.apparent_encoding分析页面内容里面猜测编码方式，如果页面头部没有编码方式，则用r.apparent_encoding分析以后再赋值给r.encoding以替换ISO ‐8859‐1
print(r.text)#r.text指的是url对应的页面内容
print(type(r))#r属于一个类，这个类的名字是Response<class 'requests.models.Response'>
print(r.headers)#获得页面的头部信息'''