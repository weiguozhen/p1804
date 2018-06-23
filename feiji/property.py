class People(object):
    def __init__(self):
        self.__money=1
    def get_money(self):
        return self.__money
    def set_money(self,a):
        self.__money=a
    money = property(get_money,set_money)
#p=People()
#print(p.money)
#print(p.get_money())
#p.set_money(4444444)



#print(p.money)
#p.money=333333
#print(p.money)


class People(object):
    def __init__(self):
        self.__money=1
        self.__age=15
    @property                                #装饰器property装饰器   第一种 @property @方法名.setter  第二种 私有属性=property(get_,set_)
    def money(self):
        return self.__money
    @money.setter
    def money(self,a):
        self.__money=a
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,a):
        self.__age=a
    #money = property(get_money,set_money)
p=People()
print(p.money)
p.money=333333
print(p.money)
print(p.age)
p.age=18
print(p.age)

