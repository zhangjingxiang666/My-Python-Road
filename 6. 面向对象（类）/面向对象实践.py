#程序中的数据和操作数据的函数是一个逻辑上的整体，称之为“对象”。
#类是对象的蓝图和模板，而对象是类的实例。类是抽象的概念，而对象是具体的东西。

#现在创建一个类。类名首字母大写
class Student:
    def __init__(self,property1,property2, property3):##注意：_init_是一个特殊的函数，用于根据类的定义创建实例对象，其最开始的形式参数必须是self。property123就是普通形式参数
        self.name=property1
        self.score=property2
        self.call_parents_or_not=property3

    def showresults(self):#可以给类创建函数，后面调用时直接以 对象名.3. 函数()  调用即可
        print('%s这名同学成绩为%s，%s.' % (self.name, self.score,self.call_parents_or_not))


def main():
    #在Student这个类底下创建对象
    stu1=Student('张三','67','不叫家长')
    stu1.showresults()#调用类里面的函数
    stu2=Student('李四','52','叫家长')
    stu2.showresults()

if __name__ == '__main__':#if __name__ == '__main__':的意思是，如果这个python文件被其他脚本通过import调用的话，就不运行。如果运行的是它本身的话，就运行
    main()
