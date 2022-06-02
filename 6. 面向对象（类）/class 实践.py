class Qianqiu:
    def __init__(self,v0,t):
        self.x=v0*t
        self.y=-0.5*9.8*t*t

def getinputs():
    a=eval(input('请输入水平初速度'))
    b=eval(input('请输入抛出时间'))
    return a,b
def main():
    v0,t=getinputs()
    Object1 = Qianqiu(v0,t)
    print('在%s秒后铅球的位置为%s,%s' %(t,Object1.x, Object1.y))
main()
