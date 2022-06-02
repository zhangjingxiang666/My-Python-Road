#Object类是最大的类，是所有类的父类。新建类时如果未指明父类，则默认隶属于Object
'''Object自己就包含了'__class__'以及 '__str__'等方法和属性。
其中运行__str__()方法的结果为这个类它本身。
即【print(实例名.__str__())】等价于【print(实例名)】
可以通过【__str__()】方法可以做修改，修改后依然等价'''
class School:
    def __init__(self,Location,BuildYear):
        self.Location=Location  #注意此处别忘了前面的self.
        self.BuildYear=BuildYear

    def __str__(self):  #__str__(self)方法改的是__str__属性里面的东西
        return ('这是一所位于{0}的于{1}年建成的学校'.format(self.Location,self.BuildYear))

school2=School('上海',1960)
print(dir(school2))
print(school2)  #当打印school2这一实例本身时，打印的其实是school2这一实例运行【school2.__str__()】这一方法的结果
print(school2.__str__())

