def main():
    i=0
    sum=0
    xstr=input("请输入下一个数字，或者按回车直接结束")#循环之前就要有一个这个，否则i就会多加一遍
    while xstr!="":
        x = eval(xstr) #eval处理不了非数字型字符串！
        sum=sum+x
        i=i+1
        xstr=input("请输入下一个数字，或者按回车直接结束")
    print("平均值为", sum / i)
main()