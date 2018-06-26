class People(object):
    def __init__(self):

        self.__money=1
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self,a):
        self.__money=a
   # money=property(get_money,set_money)
   #通过property吧get_money和set_money方法属性化，可直接使用
c=People()    #property 的两种用法
print(c.money)
c.money=99999
print(c.money)
