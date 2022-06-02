from math import *
from random import random

def qiujifen(m):
    total_area = 0
    x=0
    for i in range(0,m,1):
        microarea=(1/m)*(x**2)
        x=x+1/m
        total_area=total_area+microarea
    print(total_area)

m=int(input("请输入分成多少份"))
qiujifen(m)
