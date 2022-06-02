def main():
    sum=0
    i=0
    moredata="yes"
    while moredata[0]=="y":#0为第一位！！
        a = eval(input("下个运算值是什么？"))
        sum=sum+a
        i=i+1
        moredata=input("是否还要进行下一次运算？yes or no")
        print("平均值为", sum / i)

main()