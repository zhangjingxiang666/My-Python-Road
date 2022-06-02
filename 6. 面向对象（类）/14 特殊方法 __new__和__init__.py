print('总类object的编号为',id(object))
print(dir(object))#列出object这个总的大类所包含的所有属性和方法

class Person(object):
    '''【__new__(cls)】是object类自带的一个类方法，用于从类中创建实例。
    在创建过程中默认自动调用，无需手动写出。也就是生成实例过程中都默认new一下，通常自动就new了。
    此处是为了体现【__new__(cls)】的作用，将这一方法在子类中单独拎了出来'''
    def __new__(cls, *args, **kwargs):  #此处在object的Person子类中重写一下【__new__(cls)】方法
        InstanceObject=super().__new__(cls) #InstanceObject为生成中的对象名
        print('创建中的实例InstanceObject的编号为', id(InstanceObject))
        return InstanceObject

    '''【__init__(self,参数1,参数2,....)】为object类中自带的实例方法，用于实例对象的初始化'''
    def __init__(self,name,age):
        self.name=name
        self.age=age

Stu1=Person('李四',28)


print('Person类的编号为',id(Person))
print('创建完成后的实例Stu1编号为',id(Stu1))
