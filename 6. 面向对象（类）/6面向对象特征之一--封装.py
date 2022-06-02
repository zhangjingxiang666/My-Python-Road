#面向对象编程可以把一个类及类里面的方法封装好后，再通过外部调用
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age      #如果希望外界只能通过类里面方法调用某属性，而不希望直接调到属性时，在属性前面加两个下划线
    def show(self):
        print(self.name)
        print(self.__age)

stu1=Student('李四','25')
stu1.show()#这样外界只能通过类里面方法调用age这一属性

print(stu1.name)
print(stu1.__age)#而外界不能直接调用age这一属性

print(stu1._Student__age)#然而，可以通过【实例名._类名__属性】调用。但不建议这么做