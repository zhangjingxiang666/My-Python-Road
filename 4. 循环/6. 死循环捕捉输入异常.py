while True:#python对大小写敏感的！True的T一定大写
    try:
        a=int(input("请输入一个数字"))
        print(a)
        break   #别忘了跳出循环！否则会一直让你输入
    except ValueError:
        print("你个sb")


while True:
    a=eval(input("请输入一个正数"))
    if a>0:
        break
    else:
        print("输入失败")
print(a)