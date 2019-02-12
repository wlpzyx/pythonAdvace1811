#创建类
class Person(object):

    def __init__(self,_name) -> None:
        self.name=_name

s=Person("abc")

print(s.name)

Person.age=20  #通过类名动态的添加类属性
print(Person.age)

s.stature=1.7  #通过实例动态的添加实例属性
print(s.stature)

'''
类方法和类属性属于类  不属于某个实例
'''