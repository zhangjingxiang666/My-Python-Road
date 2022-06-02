#没有with的情况
reader=open('a.txt','r')#创建阅读器,以读取的方式打开
content=reader.read()#阅读器阅读文件内容作为content
print(content)#打印content
reader.close()#关闭reader

'''有with的情况'''
with open('a.txt','r') as reader:
    reader.read()
    print(content)
'''有with的话就不用后续关闭文件了'''

'''为什么呢？因为上下文管理器。下面解释原因：'''
class Filemanager():
    def __init__(self,name,mode):
        print('调用__init__方法啦~')
        self.name=name
        self.mode=mode
        self.file=None
    def __enter__(self):
        print('调用__enter__方法啦~')
        self.file=open(self.name,self.mode)
        return self.file
    def __exit__(self,exc_type,exc_val,exc_tb):
        print('__exit__方法被调用啦')
        if self.file:
            self.file.close()

with Filemanager('a.txt','r') as FM:
    print('准备读取文件')
    content=FM.read()
    print(content)

'''也就是，当一个函数被with方法调用时，
        会先运行其内置的__init__()特殊方法
        会先运行其内置的__enter__()特殊方法
        再运行后面的代码
        最后运行其内置的__exit__()特殊方法'''

