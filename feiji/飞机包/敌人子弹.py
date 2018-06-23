from 英雄子弹爸爸 import *



class EnemyBullet(zidan):
    '''敌机子弹的抽象类'''
    def __init__(self,img_path,screen,x,y):
        zidan.__init__(self,img_path,screen,x+40,y+20)
    def move(self):
        self.y += 2
    def judge(self):
        """判断子弹是否飞出了屏幕"""
        if self.y > 500:
            return True#表示子弹飞出了屏幕
        else:
            return False
c
