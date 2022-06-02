import turtle
def xunhuan(i):#定义函数别往后面冒号
    turtle.up()
    turtle.goto(300, 300)
    turtle.down()
    for i in range(i,300, 20):#循环别忘了后面的冒号
        turtle .seth(240)
        turtle.fd(i)
        turtle.seth(0)
        turtle.fd(i)
        turtle.seth(120)
        turtle.fd(i)
        turtle.color("red")
        turtle.circle(i,180)
        turtle.color("orange")
i=int(input("请输入初始值"))
xunhuan(i)