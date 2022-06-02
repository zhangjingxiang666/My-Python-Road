import requests

urls=[
    f'https://www.cnblogs.com/#p{page}'
    for page in range(1, 50+1)#for循环是前闭后开区间
]
#print(urls)

def Web_Crawler(site_address):
    r=requests.get(site_address)
    print(site_address,len(r.text))

if __name__=='__main__':
    Web_Crawler(urls[0])

