a=eval(input("请输入几个数字，用逗号隔开"))
print(a)
length=len(a)
print(length)
print(max(a))#pytho自带

#下面是循环比较最大值
max=a[0]#最大比较循环，给它一个初始值
for i in range(0,length-1,1):
    if a[i+1]>max:
        max=a[i+1]
print(max)
