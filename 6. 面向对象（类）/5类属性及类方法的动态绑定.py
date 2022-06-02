class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name,'在吃饭呢' )

stu1=Student('张三','20')
stu2=Student('李四',30)

print(stu1.age)
print(stu2.name)

stu1.gender='男' #可以为类里面的某个实例单独添加一个属性
print(stu1.gender)

#也可以先定义一个函数。然后使用【实例名.方法=函数名】来单独为某一个实例定制一个方法
def drink(a):
    print(a,'在喝水呢')
stu2.drink=drink
stu2.drink(stu2.name)
