from math import sqrt
from random import random
number_of_times=0
zongcishu=int(input("要算多少次呢？"))
for i in range(1,zongcishu):#注意：在前面插入for函数，千万别忘了1.缩进 2.把后面不需要循环的拿到前头去！
    x,y=random(),random()
    distance=sqrt(x**2+y**2)
    if(distance<=1.0):
        number_of_times=number_of_times+1
    pai=4*(number_of_times/zongcishu)
    print(pai)
print(pai)