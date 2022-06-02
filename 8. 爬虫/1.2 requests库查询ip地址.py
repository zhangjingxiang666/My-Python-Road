from requests import *
kv={'user-agent':'Mozilla/5.0'}
url='http://ip.tool.chinaz.com/'
r=get(url+'202.108.22.5',params=kv)
print(r.status_code)
print(r.text)