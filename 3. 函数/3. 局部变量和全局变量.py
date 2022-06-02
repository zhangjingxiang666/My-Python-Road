n,m=100,1000
def main():
    global n #声明使用的为全局变量
    a=n+1
    print(a)
main()

q=0
def main2():
    q=1
main2()#函数运行结束后，局部变量q就被释放
print(q)#此时print出来的依然是全局变量的那个q