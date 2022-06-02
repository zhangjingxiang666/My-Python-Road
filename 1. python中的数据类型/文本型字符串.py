a="putonggaodengxuexiao"
b="hello\nworld"#表示换行时为右斜杠！！
print(a)
print(a[2])
print(a[2:-2])#注意区间是冒号！！！冒号！！！不是逗号！！
print(a+"666999999")
print(6*a)
print(len(a))#字符串长度
print(a.upper())#大写
print(a.capitalize())#首字母大写
print(a.split("u",1))#以u为分隔符，分隔一次
print(b)
print(b.split("\n"))


#输入几就是星期几
str1="星期一星期二星期三星期四星期五星期六星期日"
shuru=input("请输入星期所对应的数字")
if int(shuru)<8:#像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束
    m=3*(int(shuru)-1)
    print(str1[m:m+3])#注意区间中间是冒号！！！冒号！！！不是逗号！！
elif int(shuru)<10:
    print("数据错误！")
else:
    print("你个大傻逼")

