def main():

    try:#try后面别忘冒号
        number_1, number_2 = eval(input("请输入两个数字，用逗号隔开"))
        m=number_1/number_2
    except ZeroDivisionError:#1. except和try是同一级别的 2. except后面别忘冒号
        print("请不要用0当做除数")
    except NameError:
        print("输入错误！")
    except:
        print("其他错误！")
    else:
        print(m)
    finally:
        print("运算完成")

main()