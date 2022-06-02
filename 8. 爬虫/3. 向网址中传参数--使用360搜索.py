from requests import *
para1={'q':'sepsis'}
kv = {'user-agent': 'Mozilla/5.0'}
r=get('https://www.so.com/s',params=para1,headers=kv)
r.encoding=r.apparent_encoding
print(r.status_code)
print(r.request.url)
print(len(r.text))