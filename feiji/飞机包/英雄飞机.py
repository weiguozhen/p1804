from 飞机爸爸 import *
class Heroplane(plane):
    '''飞机抽象类'''
    def __init__(self,img_path,screen):
        plane.__init__(self,img_path,screen,(400-100)/2,350)

    def fire(self):
        self.bullet_list.append(Bullet("./tupian/bullet.png",self.screen,self.rect.x-20,self.rect.y+100))
        self.bullet_list.append(Bullet("./tupian/bullet.png",self.screen,self.rect.x+40,self.rect.y))
        self.bullet_list.append(Bullet("./tupian/bullet.png",self.screen,self.rect.x+100,self.rect.y+100))

