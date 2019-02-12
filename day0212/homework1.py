class person(object):
    #类属性
    name = "abc"

    def __init__(self,_hp) -> None:
        #实例属性
        self.hp=_hp

s = person(10)
print(s.name,s.hp)

print(person.name)
#print(person.hp)       #类属性不能操作实例属性