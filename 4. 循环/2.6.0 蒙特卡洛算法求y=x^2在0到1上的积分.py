from math import *
from random import *
m=0
for i in range (1,10000000,1):
    x,y=random(),random()
    if y<x*x:
        m=m+1
print(m/10000000)