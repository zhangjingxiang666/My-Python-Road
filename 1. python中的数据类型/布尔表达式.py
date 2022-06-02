a=bool("")
b=bool("ooo")#对于文本，空的为false,有内容为true
print(a)
print(b)

a=bool(0)
b=bool(1)#对于数字，0为false,非零为true
print(a)
print(b)


m=input("请输入你想要的气味【默认为香味】")
if m:                                           #if 后面所有的内容本质上是一个布尔表达式。因此，if m 等价于 if m!=("")，因为其表达的都是“m有内容”的意思
    print("你喜欢的气味为%s"%m)
else:
    print("你喜欢的气味为香味")