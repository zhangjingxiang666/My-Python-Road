class Student: #Student为类名，单词首字母需要大写
     # 类之内的def定义称为方法。也分为实例方法、静态方法和类方法。
     def __init__(self,name,age):#括号内第一个指它自己；后面的分别为局部变量。后续可以为变量进行赋值
         self.calling=name #self.calling为实例属性。此处是将局部变量name的值赋给了self.calling这个实例属性
         self.lifetime=age#self.lifetime为实例属性。此处是将局部变量age的值赋给了self.lifetime这个实例属性

     #类之内的def定义称为方法，分为实例方法、静态方法和类方法。（另：类之外的def定义称为函数）
     #实例方法（只有实例可以调用）
     def Eat(self,a,b):#括号里一定要有东西，括号内默认主体是self，后面的都是参数（类似函数内的参数）
         print(a*b,'个学生在吃饭')

     #静态方法--使用@staticmethod进行修饰（类和实例可以调用）
     @staticmethod
     def SticMetod(x,y):#类和类内实例都可以调用。括号内无默认主体，后面的都是参数（类似函数内的参数）
         m=x*y
         print('我用了@staticmethod进行修饰的静态方法',m)

     # 类方法--使用@classmethod进行修饰（只有类可以调用）
     @classmethod
     def ClasMetod(cls):        #括号里面默认用cls
         print('我用了@classmethod进行修饰的类方法')

#在Student类里面创建一个实例对象stu1
stu1=Student('张三','20') #根据上面 def __init__()括号里面除了self后面跟的变量来定义Student的属性
print('stu1的编号是',id(stu1),'stu1的类型是',type(stu1),'stu1在内存中的位置是', stu1)

'''实例方法只有实例可以调用'''
#上面对Student类里面的实例定义了实例方法Eat，下面可以在stu1这一实例中直接调用该方法。下面两种方式都可以调用
print('----------实例方法的调用---------')
stu1.Eat(5,6)      #实例名.方法名()
Student.Eat(stu1,5,6)       #类名.方法名(实例名)
#上述两行代码相同，都是调用Student类里面的eat方法

'''类方法只有类可以的调用'''
print('----------类方法的调用---------')
Student.ClasMetod()

'''静态方法类和对象都可以调用'''
print('----------静态方法的调用---------')
Student.SticMetod(5,6)
stu1.SticMetod(5,6)






