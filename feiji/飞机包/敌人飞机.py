from 飞机爸爸 import *




class EnemyPlane(plane):
    '''敌机抽象类'''
    def __init__(self,img_path,screen):
        plane.__init__(self,img_path,screen,0,0)
        self.flag = "right"
    def move(self):
        if self.flag == "right":
            self.rect.x += 2
        else:
            self.rect.x -= 2
        if self.rect.x > 400 - self.rect.width:
            self.flag ="left"
        elif self.rect.x <= 0:
            self.flag = "right"
    def fire(self):
        self.bullet_list.append(EnemyBullet("./tupian/bullet1.png",self.screen,self.rect.x,self.rect.y))
    def bbaozha(self):
        baozha=EnemyPlane("./tupian/enemy0_down2.png",screen)
        self.display()


