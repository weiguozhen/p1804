#coding=utf-8
#import time
import pygame
import random
class Heroplane(object):
    def __init__(self,img_path,screen):
        self.screen = screen
        self.x = (400-100)/2
        self.y = 350
        self.w = 100
        self.h = 124
        self.img_path = img_path
        self.hero_plane=pygame.image.load(self.img_path)#飞机图片
        #定义好的位置和尺寸
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.bullet_list=[]
    def display(self):
        self.screen.blit(self.hero_plane,self.rect)
        for i in self.bullet_list:
            i.display()
            i.move()
           # i.move1()
    def fire(self):
        self.bullet_list.append(Bullet("./tupian/bullet.png",self.screen,self.rect.x-20,self.rect.y+100))
        self.bullet_list.append(Bullet("./tupian/bullet.png",self.screen,self.rect.x+40,self.rect.y))
        self.bullet_list.append(Bullet("./tupian/bullet.png",self.screen,self.rect.x+100,self.rect.y+100))
class Diji(object):
    def __init__(self,img_path,screen):
        self.screen = screen
        self.x = (400-100)/2
        self.y = 50
        self.w = 100
        self.h = 124
        self.img_path = img_path
        self.dj = pygame.image.load(self.img_path)#敌机
        #位置尺寸
        self.chicun = pygame.Rect(self.x,self.y,self.w,self.h)
        self.zidan = [] #列表储存子弹
    def xianshi(self):
        a=random.randint(1,7)
        self.screen.blit(self.dj,(self.x,self.y)) #显示敌机
        for i in self.zidan:
            if a==2:
                i.zidanxianshi()

                i.move()
    def tianjiazidan(self):
        self.zidan.append(Dijizidan("./tupian/bullet2.png",self.screen,self.x,self.y))#将子弹添加到列表中

class Bullet(object):
    def __init__(self,img_path,screen,x,y):
        self.screen = screen
        self.x = x
        self.y = y
        self.img_path = img_path
        self.bullet=pygame.image.load(self.img_path)

    def display(self):
        self.screen.blit(self.bullet,(self.x,self.y))
    def move(self):
        self.y -= 2
    #def move1(self):
     #   self.x -= 20
class Dijizidan(object):
    def __init__(self,img_path,screen,x,y):
        self.screen = screen
        self.x=x
        self.y=y
        self.img_path=img_path
        self.zd=pygame.image.load(self.img_path)
        self.flag="right"
    def zidanxianshi(self):
        self.screen.blit(self.zd,(self.x,self.y))
        self.screen.blit(self.zd,(self.x-10,self.y-10))
    def move(self):
        if self.flag == "right":
            self.x +=2
        else:
            self.x -=2
        if self.x > 300:
            self.flag = "reft"
        elif self.x<=0:
            self.flag = "right"




def key_control(hero,move_step):

     for event in pygame.event.get():
         if event.type == pygame.QUIT:#退出游戏
             print("游戏退出")
             pygame.quit()
             exit()#退出程序
         elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE:
                 hero.fire()
             #elif event.key == pygame.K_n:
             #    diji.chucun()




     keys_pressed = pygame.key.get_pressed()
     if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
         hero.rect.x += move_step
     if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
         hero.rect.x -= move_step
     if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
         hero.rect.y -= move_step
     if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
         hero.rect.y += move_step
     if hero.rect.bottom<=50:
         hero.rect.y=50
     if hero.rect.y>=400:
         hero.rect.y=400
     if hero.rect.x+hero.rect.width<=50:
         hero.rect.x=50
     if hero.rect.x>=300:
         hero.rect.x=300




def main():
    #创建游戏窗口
    screen = pygame.display.set_mode((400,500),0,32)
    #把本地文件夹的图片获取到代码中
    background=pygame.image.load("./tupian/background.png")
    #初始化飞机
    hero = Heroplane("./tupian/hero1.png",screen)
    #初始化敌机
    diji=Diji("./tupian/enemy-1.gif",screen)

    clock = pygame.time.Clock()#获得游戏时钟控制器
    move_step = 10 #移动的步长值
    while True:
        #把图片加载到游戏窗口上
        a=random.randint(1,40)
        screen.blit(background,(0,0))
        hero.display()
        diji.xianshi()
        key_control(hero,move_step)
        #diji.x = a
        diji.x += 1
        if diji.x > 350:
            diji.x = 0
        if a==3:
            diji.tianjiazidan()
       # diji.chicun.x=a
       # if diji.chicun.x > 40:
        #    diji.chicun.x=0



        #刷新显示
        pygame.display.update()
        clock.tick(60)#让游戏时钟，1/60秒运行一次






    '''

    #1.x 2.y 3.宽 4.高
    feiji=pygame.Rect(100,500,50,50)
    print("x=",feiji.x)
    print("y=",feiji.y)
    print("width",feiji.width)
    print("height",feiji.height)
    '''
if __name__=="__main__":
    main()
