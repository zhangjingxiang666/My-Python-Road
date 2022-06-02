'''类可以继承，类的父类在定义时写在括号中。如果不写括号则默认继承自object'''
class Person(object):
    # 类的初始化：定义方法__init__(self,参数，参数,.....）进行类的初始化
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def ShowInfo(self):
        print('这个人的姓名和年龄分别是',self.name,self.age)

class Student(Person):
    '''父类的方法可以在子类中以相同名称进行重写。例如ShowInfo这一方法。
    在子类基于父类的方法定义新方法的时候，前面写上【super().父类方法名(参数...)】则可以先运行父类的方法。下一行再加上子类新添加的部分。'''
    def ShowInfo(self,gender):  #重新定义子类中的ShowInfo方法
        super().ShowInfo()  #先运行父类的方法，以【super().父类中方法名(参数...)】表示。也就是方法的嵌套。
        self.gender=gender  #这是子类新加的方法
        print('把父类方法以相同名称进行重写。这个人的性别是', self.gender)

    '''当然，子类中也可以基于父类方法新写一个方法。例如下面的ShowStuInfo
    先通过【super().父类方法名(参数...)】运行父类的方法，然后下一行再加上子类新添加的部分。'''
    def ShowStuInfo(self,gender):   #在子类中新定义一个ShowStuInfo方法
        super().ShowInfo()  #先运行父类的方法，以【super().父类中方法名(参数...)】表示。也就是方法的嵌套。
        self.gender=gender  #这是子类新加的方法
        print('在子类中新定义一个方法。这个人姓名、年龄和性别分别是',self.name,self.age,self.gender)

#在Student类中创建实例
stu1=Student('张三',25)

stu1.ShowInfo('女')

stu1.ShowStuInfo('女')
#Student.showinfo(stu1,'女')