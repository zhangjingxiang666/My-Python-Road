import turtle
def drawSnake(changdu, angle, len, neckrad):
    for i in range(len):
        turtle.circle(changdu, angle)
        turtle.circle(-changdu, angle)
    turtle.circle(changdu, angle/4)
    turtle.fd(changdu)
    turtle.circle(neckrad+1, 180)
    turtle.fd(changdu*2/3)

def main() :
    turtle.setup(1300, 1200, 0, 0)
    pythonsize = 30
    turtle.pensize(pythonsize)
    turtle.pencolor("red")
    turtle.seth(-40)
    drawSnake(40, 80, 5, pythonsize/2)
main()