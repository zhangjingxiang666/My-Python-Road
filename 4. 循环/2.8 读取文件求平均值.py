filename=(r"D:\a.txt")#前面加一个r表示强制将后面引号里的读为文本。否则里面的/a会被理解为其他意思
content=open(filename,'r')
sum=0
i=0
line = content.readline()#1.由于eval不能处理包括空值在内的文本型字符串，所以在这里不能加eval. readline默认最开始读第一行，后面读下一行
print(line)
while line!="":
    for shuzi in line.split(','):#一串字符串经过split以后就是一个可以遍历的列表，类似于i in range(1,10)这样
        sum=sum+eval(shuzi)
        i=i+1
    line = content.readline()#readline是最开始读第一行，后面是读下一行，就类似于i=i+1
print("平均数为",sum/i)

liebiao=[]
liebiao=i in range (1,10,1)
print(str(liebiao))