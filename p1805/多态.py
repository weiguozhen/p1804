class Dog(object):
    def game(self):
        return "普通小狗玩泥巴"
class Xiaotianquan(Dog):
    def game(self):
        return "哮天犬玩泥巴"
class Poeple(object):
    def with_(self,a):
        print("人和",a.game())
d= Dog()
r=Poeple()
r.with_(d)
c=Xiaotianquan()
r.with_(c)


