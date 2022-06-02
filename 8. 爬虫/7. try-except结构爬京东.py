from requests import *
def main(url):
    try:
        hd={'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Mobile Safari/537.36'}
        r=get(url)
        print(r.status_code)
        r.raise_for_status()  # 如果状态不是200，则引发HTTPError异常
        print(r.encoding)
        return(r.text[0:1000])#只获取前1000个字符
    except:
        return('网络异常')
print(main('https://item.jd.com/100004538398.html'))