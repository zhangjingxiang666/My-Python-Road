a=eval(input("请输入整数"))
sum=0
i=1#while循环别忘了设置自变量初始值
while i<=a:
    sum=sum+i
    i=i+1#千万别忘了让i累加！！！
print("平均值为",sum/a)


b=1
sum=0
while b<=3:
    sum=sum+b
    b=b+1
    if sum>2:
        break    #break代表满足上面这个条件则立马跳出整个循环,在if下面的一层而非同层
print(sum)

c=0
summ=0
while c<=3:
    c = c + 1
    if c==2:
        print("发现2！")
        continue
    summ=summ+c
print(summ)