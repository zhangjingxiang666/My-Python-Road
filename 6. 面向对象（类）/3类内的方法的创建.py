class Student: #Student为类名，单词首字母需要大写
     native_pace='吉林'       #直接写在类里面的变量（即在所有类方法外的变量），称为类属性
     '''在类中，根据变量定义的位置不同，以及定义的方式不同，类属性又可细分为以下3种类型:
        1.类体中、所有函数之外：此范围定义的变量，称为类属性或类变量；
        2.类体中，所以函数内部：以“self.变量名”的方式定义的变量，称为实例属性或实例变量;
        3.类体中，所有函数内部：以“变量名 = 变量值”的方式定义的变量，称为局部变量。'''

     # 类的初始化：定义方法__init__(self,参数，参数,.....）进行类的初始化
     def __init__(self,name,age):
         self.calling=name #self.calling为实例属性。此处是将局部变量name的值赋给了self.calling这个实例属性
         self.lifetime=age#self.lifetime为实例属性。此处是将局部变量age的值赋给了self.lifetime这个实例属性

     # 类之内的def定义称为方法。也分为实例方法、静态方法和类方法。
     #实例方法
     def eat(self):#括号里一定要有东西，默认是self
         print('学生在吃饭')

     #静态方法--使用@staticmethod进行修饰
     @staticmethod
     def method():#括号内不写
         print('我用了@staticmethod进行修饰的静态方法，括号里面不用self')

     # 类方法--使用@classmethod进行修饰
     @classmethod
     def ClasMetod(cls):
         print('我用了@classmethod进行修饰的类方法，括号里面默认用cls')

#类之外的def定义称为函数，类之内的def定义称为方法
def Distance(v,t):
    L=v*t
    print('总计距离是',L) #print后面不要忘记逗号
Distance(2,5)



