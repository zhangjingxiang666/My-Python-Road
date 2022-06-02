a=eval(input("请寻找数字多少以内的质数"))
for i in range (2,a):
    for m in range (2,i):
        if i%m==0:
            print(i,"=", m, "*", int(i/m))
            break
    else:#else和for循环在同一层级使用，只有内层的这个for循环遍历完毕且没有被break打断的情况下才执行else下面的语句（注意是遍历完毕！而不是每遍历一次就执行一次！）
        print(i,"是一个质数")