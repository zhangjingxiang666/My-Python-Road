'''print输出两个变量时用逗号隔开'''
a=2
b=5
print(a,b)

'''print在想输出的变量之前可以加上字符串。用逗号隔开'''
print('我即将输出的是',a,b)

'''print可以在字符串中混入变量一起输出。
具体格式为 【‘字符串内部向混入的变量用{0}和{1}等编号代替’.format({0}指代的变量,{1}指代的变量)'''
print('这里有{0}队，每队有{1}人'.format(a,b))

'''return也可以在字符串中混入变量一起输出。
具体格式同上'''
def School():
    return('这个学校有{0}个班，每班有{1}人'.format(a,b))

print(School())
