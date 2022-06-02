'''类可以继承，类的父类在定义时写在括号中。如果不写括号则默认继承自object【注意o是小写】'''
class Person(object):
    # 类的初始化：定义方法__init__(self,参数，参数,.....）进行类的初始化
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def showinfo(self):
        print('这个人的姓名和年龄分别是',self.name,self.age)

class Student(Person):  #Student类继承自Person类
    '''父类的方法可以在子类中重写。例如初始化方法  __init__(self,参数，参数,.....）
    在子类基于父类的方法定义新方法的时候，前面写上【super().父类方法名(参数...)】则可以先运行父类的方法。下一行再加上子类新添加的部分。'''
    def __init__(self,name,age,StuID):  #重新定义子类中的__init__方法
        super().__init__(name,age)  #先运行父类的方法，以【super().父类中方法名(参数...)】表示。也就是方法的嵌套。
        self.StuID=StuID    #这是子类新加的方法

class Teacher(Person):
    def __init__(self,name,age,year_of_teach):
        super().__init__(name,age)
        self.year_of_teach=year_of_teach

stu1=Student('张三',25,'20192012')
teach1=Teacher('李四',34,10)

stu1.showinfo()
teach1.showinfo()



