class GirlFriend(object):
    __girl=None
    __only_you=False
    def __init__(self,name):
        if self.__only_you==False:
            self.name = name
            self.__only_you=True
    def __new__(cls,*args):
        if cls.__girl == None:
            cls.__girl = object.__new__(cls)
        return cls.__girl

girl01 = GirlFriend("dd")
print(girl01.name)
girl02=GirlFriend("gg")
print(girl02.name)
