'''前后各带两个下划线的为特殊属性和方法
下面是特殊方法'''
class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):   #只有定义了【__add__(self, other)】特殊函数，才能后续对特殊对象使用加法
        return self.name+other.name

stu1=Student('张三')
stu2=Student('李四')
s=stu1+stu2   #只有定义了【__add__(self, other)】特殊函数，才能后续对特殊对象使用加法
print(s)


class School:
    def __init__(self,calling):
        self.calling=calling
    def __len__(self):      #只有定义了【__len__(self)】特殊函数，才能后续对特殊对象计算长度
        return len(self.calling)
school2=School('张憋三学校')

print(len(school2)) #只有定义了【__len__(self)】特殊函数，才能后续对特殊对象计算长度

