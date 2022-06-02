#amazon有反爬虫机制
from requests import *
kv={'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Mobile Safari/537.36'}
url='https://www.amazon.cn/dp/B07Y8C8THQ'
r=get(url,headers=kv)
print(r.status_code)
r.encoding = r.apparent_encoding
print(r.text)