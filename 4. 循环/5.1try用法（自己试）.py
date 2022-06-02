from math import *
from random import *
def main():
    try:
        x = eval(input("请输入数字"))
        y=sqrt(x)
    except NameError:
        print("请输入阿拉伯数字！")
    except ValueError:
        print("请输入正值，傻X")
    else:
        print(y)
    finally:
        print("运算完成啦~")


main()