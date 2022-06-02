class Student: #Student为类名，单词首字母需要大写
    '''在类中，根据变量定义的位置不同，以及定义的方式不同，类属性又可细分为以下3种类型:
           1.类体中、所有函数之外：此范围定义的变量，称为类属性或类变量；
           2.类体中，所以函数内部：以“self.变量名”的方式定义的变量，称为实例属性或实例变量;
           3.类体中，所有函数内部：以“变量名 = 变量值”的方式定义的变量，称为局部变量。'''
    native_pace = '吉林'  # 这个就是类属性

    #类的初始化：定义方法__init__(self,参数，参数,.....）进行类的初始化
    def __init__(self,name,age):#括号内第一个指它自己；后面跟的都是变量。后续可以将变量的值赋给实例对象的属性
         self.calling=name #self.calling为实例属性。此处是将局部变量name的值赋给了self.calling这个实例属性
         self.lifetime=age#self.lifetime为实例属性。此处是将局部变量age的值赋给了self.lifetime这个实例属性

#在Student类里面创建一个实例对象
stu1=Student('张三','20') #根据上面 def __init__()括号里面self后面跟的变量来定义stu1的属性
print('stu1的编号是',id(stu1),'stu1的类型是',type(stu1),'stu1在内存中的位置是', stu1)

print(stu1.calling)#显示stu1这一实例的calling属性
print(stu1.lifetime)#显示stu1这一实例的lifetime属性

#Student这个类本身也是一个对象（类对象）
print('Student类对象的编号是',id(Student))
print('Student类对象的类型是',type(Student))
print(Student)





