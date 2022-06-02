from requests import *
hd={'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Mobile Safari/537.36'}
#注意中间是冒号！！冒号！！
#具体UA可以在浏览器里右上角三个点-更多工具- 控制台-三个点--更多工具--网络状态-然后看到有个 user agent 去掉 自动选择，复制其中的代码即可
r=request('get','http://www.baidu.com',headers=hd)#headers=hd代表用hd这个UA
r.encoding=r.apparent_encoding
print(r.text)