from requests import *
url="http://www.baidu.com/s?wd="
r=get(url+'Python')
print(r.status_code)
print(r.request.url)
print(len(r.text))