def jiecheng(n,*b):#给出可变参数，就是后面想输入几个就输入几个
    s=1
    for i in range(1,n+1):
        s=s*i
    for item in b:
        s=s*item
    return s
y=jiecheng(10,3)
print(y)
z=jiecheng(10,1,2,3)
print(z)