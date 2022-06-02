from requests import *
def getHTMLText(url):
    try:
        r=get(url,timeout=30)
        r.raise_for_status()#如果状态不是200，则引发HTTPError异常
        r.encoding=r.apparent_encoding
        return(r.text)
    except:
        return('出现异常')
if __name__ == '__main__':#表示当 .py 文件被直接运行时，if __name__ == '__main__' 之下的代码块将被运行； 当 .py 文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
    url=input('输入网址,别忘自己加前面的http://')
    print(getHTMLText(url))
