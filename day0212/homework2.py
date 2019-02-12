#创建类
class Shop():
    '''
     需要使用@classmethod方法声明 第一个参数为cls 可以访问类相关比如 类说明
    '''
    #类属性
    isopen = False

    def __init__(self,shoplist) -> None:
        #实例属性
        self.shoplist=shoplist
    @classmethod
    def classinfo(cls):
        print(cls.__doc__)

    def addShop(self,_name):
        self.name=_name


    @staticmethod
    def shopp():
        print("静态方法的输出")

s=Shop("abc")

#类方法
s.classinfo()
#静态方法
s.shopp()
