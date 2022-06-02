#类：代表具体的一类东西
#实例：类里面的具体的某一样东西
class Student: #Student为类名，单词首字母需要大写
    pass #当这个类里面具体需要什么还不确定时，可以使用pass进行占位，保证不报错

#python中一切皆对象。里面包含了类对象和实例对象。即使之前创建的这个Student类也是对象。需要占用内存空间，有id号，也有值
print(id(Student))
print(type(Student))
print(Student)