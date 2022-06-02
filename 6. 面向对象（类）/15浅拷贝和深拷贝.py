class CPU:
    pass
class Disk:
    pass
class Computer():
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

Intel2=CPU()#如果类不带参数，那么定义实例时也可以不带参数
Seagate2=Disk()

Lenovo2=Computer(Intel2,Seagate2)#在定义一个实例时，另一个实例可以作为属性放在括号中

'''浅拷贝的意思是，拷贝者和被拷贝者的id（内存中的位置）不同，但是里面所含的内容的id都是相同的
例如下面的Dell2与Lenovo2的id不同。但它们cpu和硬盘的id都是相同的，不用重新拷贝一份'''
'''而深拷贝的意思是，拷贝者和被拷贝者的id（内存中的位置）不同，里面所含的内容的id都是不同的。也就是把里面所有的层次都复制一份
例如下面的Huawei2与Lenovo2的id不同。它们cpu和硬盘的id也是不同的，都重新拷贝了一份'''
import copy
Dell2=copy.copy(Lenovo2)#浅拷贝
Huawei2=copy.deepcopy(Lenovo2)#深拷贝

print(id(Lenovo2),id(Lenovo2.cpu),id(Lenovo2.disk))#联想是被拷贝者
print(id(Dell2),id(Dell2.cpu),id(Dell2.disk))
print(id(Huawei2),id(Huawei2.cpu),id(Huawei2.disk))