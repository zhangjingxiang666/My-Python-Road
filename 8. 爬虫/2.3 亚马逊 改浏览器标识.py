#亚马逊有保护机制，当没有更改UA爬取时：
from requests import *
def UA_unchanged():
    r=get('https://www.amazon.cn/dp/B07DBZZPQL/ref=sr_1_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&keywords=%E7%99%BE%E5%B9%B4%E5%AD%A4%E7%8B%AC&qid=1588822585&sr=8-1')
    print(r.status_code)
    r.encoding=r.apparent_encoding
    print(r.text)

def UA_changed():
    kv={'user-agent':'Mozilla/5.0'}
    r=get('https://www.amazon.cn/dp/B07DBZZPQL',headers=kv)
    print(r.status_code)
    r.encoding=r.apparent_encoding
    print(r.text)

if __name__ == '__main__':
    a=input("请输入1为未更改标识的，2为更改标识以后的")
    if a=='1':
        UA_unchanged()
    if a == '2':
        UA_changed()