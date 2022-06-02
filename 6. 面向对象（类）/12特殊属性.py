'''凡是前后带两个下划线的都是特殊属性或方法
首先介绍特殊属性'''
class Aa:
    pass
class Bb:
    pass
class Cc(Aa,Bb):
    def __init__(self,name,age):
        self.name=name
        self.age=age

obj1=Cc('张三',20)
print(obj1.__dict__)    #返回实例的属性【以字典的形式】
print(obj1.__class__)   #返回实例所属的类

print(Cc.__bases__)    #返回类的父类
print(Cc.__mro__)   #返回类的层次结构（父类、祖先类等等）
print(Aa.__subclasses__()) #返回一个类的子类都有哪些
