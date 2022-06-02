# import turtle
from turtle import *
def huashe(banjing, jiaodu, xunhuancishu, bozijiaodu):
    pencolor("purple")
    for i in range (xunhuancishu):
        circle(banjing, jiaodu)
        circle(-banjing, jiaodu)
    circle(banjing, bozijiaodu)
    pencolor("red")
    fd(2*banjing)
    circle(5*banjing, jiaodu)

def zhuyaohanshu():
    setup(600, 600, 0, 0)
    pensize(10)
    seth(-40)
    huashe(20, 50, 9, 120)


zhuyaohanshu()