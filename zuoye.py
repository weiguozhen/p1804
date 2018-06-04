class Jiangshi:
    def __init__(self,name,color,xue,sudu):
        self.name=name
        self.color=color
        self.xue=xue
        self.sudu=sudu
        #print("僵尸名字:%s,僵尸的颜色:%s，僵尸的血量:%s，僵尸的速度:%s"%(self.name,self.color,self.xue,self.sudo))
    def rudong(self):
        print("%s:开始蠕动了"%self.name)
    def cgt(self):
        print("%s:开始撑杆跳了"%self.name)
    def eat(self):
        print("%s:开始搞破坏了"%self.name)
    def sd(self):
        print("%s:开始加速跑了"%self.name)
    def sw(self):
        print("%s:被打致死"%self.name)
    def __str__(self):
        s="僵尸名字:"+self.name+"\n僵尸的颜色:"+self.color+"\n僵尸的血量:"+self.xue+"\n僵尸的速度:"+self.sudu
        return s
ptjs=Jiangshi("普通僵尸",'红色','500','慢')
print(ptjs)
ptjs.rudong()
ptjs.eat()
ptjs.sw()
print("*"*30)

cgtjs=Jiangshi("撑杆跳僵尸","白色","300","非常快")
print(cgtjs)
cgtjs.cgt()
cgtjs.eat()
cgtjs.sw()
print("*"*30)

pdkjs=Jiangshi("跑得快僵尸","紫色","400","飞快")
print(pdkjs)
pdkjs.sd()
pdkjs.eat()
pdkjs.sw()
print("*"*30)








import random
a=random.randint(1,5)


class xrk():
    def __init__(self,name,color,xue,kz):
        self.name=name
        self.color=color
        self.xue=xue
        self.kz=kz
    def fg(self):
        print('%s开始生产阳光%d个'%(self.name,a))
    def fy(self):
        print("%s进行自我防御"%self.name)
    def bc(self):
        print("%s被吃掉"%self.name)

    def __str__(self):
        s="名字是:"+self.name+"\n颜色是:"+self.color+"\n血量是:"+self.xue+"\n是否坚硬:"+self.kz
        return s

xiangrikui=xrk('向日葵',"黄色","血量50","脆弱")
print(xiangrikui)
print(id(xiangrikui))
xiangrikui.fg()
xiangrikui.fy()
xiangrikui.bc()

print("*"*30)


class wandou():
    def __init__(self,name,color,xue,kz):
        self.name=name
        self.color=color
        self.xue=xue
        self.kz=kz
    def gj(self):
        print('%s开始攻击'%self.name)
    def yt(self):
        print("%s开始摇头"%self.name)
    def fy(self):
        print("%s进行自我防御"%self.name)
    def bc(self):
        print("%s被吃掉"%self.name)
    def __str__(self):
        s="名字是:"+self.name+"\n发型是:"+self.color+"\n血量是:"+self.xue+"\n是否坚硬"+self.kz
        return s

print("*"*30)
wd=wandou('豌豆豆',"卷毛","血量100","坚韧")
print(wd)
wd.gj()
wd.yt()
wd.fy()
wd.bc()





print("*"*30)


class jg():
    def __init__(self,name,color,xue,jy):
        self.name=name
        self.color=color
        self.xue=xue
        self.jy=jy

    def zz(self):
        print("%s目视前方"%self.name)
    def fy(self):
        print("%s准备被吃"%self.name)
    def bc(self):
        print("%s被吃了也要抗住"%self.name)
    def __str__(self):
        s="名字是："+self.name+"\n颜色是："+self.color+"\n血量是："+self.xue+'\n是否坚硬:'+self.jy
        return s
jianguo=jg("坚果","棕色",'血量1000',"超级坚硬")
print(jianguo)
jianguo.zz()
jianguo.fy()
jianguo.bc()









