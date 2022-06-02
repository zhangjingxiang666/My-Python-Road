a=int(input("请输入您要求平均值的数字个数"))
sum=0 #循环前因变量有一个初始值
for i in range(a):
    b=int(input("请输入数字"))
    sum=sum+b
print('平均值为',sum/a)#print不同类型数值之间不能相加，但可以用逗号直接连接
