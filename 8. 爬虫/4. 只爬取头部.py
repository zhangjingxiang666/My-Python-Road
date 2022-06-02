from requests import *
r=head('http://www.qq.com')
print(r.headers)#因为r是一个类，所以要去print(r.headers)而非r本身