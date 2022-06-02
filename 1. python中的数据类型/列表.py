list=[1,2,3,4,5,6,7,8,9]
print(list)
for i in list[0:]:
    print(i)
shuru=int(input("请输入一个元素，我们将判断其是否在列表中"))#列表默认用数值表示，所以要用int转一下
if(shuru in list):
    print("在的呢~")
else:
    print("不在，哼~~")

#字符串拆分为列表
str1="我 是 最 牛 逼 的 ！"
list2=str1.split( )#split后面括号里写的是拆分标记，此处为空格
print(list2)