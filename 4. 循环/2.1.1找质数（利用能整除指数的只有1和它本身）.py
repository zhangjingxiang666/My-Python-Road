num=eval(input("请输入你想在多少以内找质数"))
zhishuliebao=[]
for i in range(1,num):
    feiyinziliebiao = []
    for j in range (1,i):
        if i%j!=0:
            feiyinziliebiao.append(j)
    if len(feiyinziliebiao)==i-2:       #别忘了,比较是否等于时用的是==
        zhishuliebao.append(i)
        print(i,"是个质数")
print("在",num,"以内所有的质数为",zhishuliebao)