import turtle
def xunhuandengbian(x):
    for x in range(x, 200, 50):
        for i in range(-120, 121, 120):#注意range是左闭右开区间！
            turtle.seth(i)
            turtle.forward(x)
        turtle.circle(x, 360)

x=int(input("请输入初始边长的值"))
xunhuandengbian(x)