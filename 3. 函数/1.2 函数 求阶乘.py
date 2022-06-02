def jiecheng(n,m=1):#可选参数m放在必选参数后面。如果不给的话就默认为括号中的
    s=1
    for i in range(1,n+1):
        s=s*i
        i=i+1
    return s//m#//号为整除的意思

y=jiecheng(6)
print(y)
z=jiecheng(6,2)
print(z)
k=jiecheng(m=2,n=6)#在括号中表明谁等于谁，就是按照名称传递
print(k)