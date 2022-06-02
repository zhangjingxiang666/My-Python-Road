'''在python中，无论你属于什么类，只要你有某一个方法，你都可以调用该方法。'''
class Animal:
    def Behave(self):
        print('动物吃东西')

class People:
    def Behave(self):
        print('人会算数')

class Dog(Animal):
    def Behave(self):
        print('狗啃骨头')
class Cat(Animal):
    def Behave(self):
        print('猫吃鱼')

def main(a):
    a.Behave()

main(Dog()) #类名Dog后面加括号Dog()代表类里的一个实例
main(Cat())
main(People())

'''在上面的例子中，People类和Cat类、Dog类不存在隶属关系。
但是既然他们都有Behave这个方法，那他们便都可以调用。
这与java等语言明确类的隶属关系后才可以调用类里面的方法是不同的
这就是python里面的多态性'''