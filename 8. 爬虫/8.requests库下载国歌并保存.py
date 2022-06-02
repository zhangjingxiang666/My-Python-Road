import requests
for i in range (1,205):
    j=str(i)
    url = 'https://guo.ge/mp3/map_'+j+'.mp3' # 目标下载链接
    r = requests.get(url) # 发送请求
    # 保存
    with open('D:/map_'+j+'.mp3', 'wb') as f:
     f.write(r.content)
     f.close

