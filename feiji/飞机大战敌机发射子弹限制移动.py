#coding=utf-8
import pygame
import random
class Heroplane(object):
    '''飞机抽象类'''
    def __init__(self,img_path,screen):
        self.screen = screen#创建窗口对象
        self.x = (400-100)/2
        self.y = 350
        self.w = 100
        self.h = 124
        self.img_path = img_path
        self.hero_plane=pygame.image.load(self.img_path)#飞机图片
        #定义好的位置和尺寸
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.bullet_list=[]#列表保存发射的子弹
    def display(self):
        self.screen.blit(self.hero_plane,self.rect)#设置飞机
        #显示子弹
        for i in self.bullet_list:
            if i.judge():
                self.bullet_list.remove(i)
            i.display()#子弹的对象.display()
            i.move()
    def fire(self):
        self.bullet_list.append(Bullet("./tupian/bullet.png",self.screen,self.rect.x-20,self.rect.y+100))
        self.bullet_list.append(Bullet("./tupian/bullet.png",self.screen,self.rect.x+40,self.rect.y))
        self.bullet_list.append(Bullet("./tupian/bullet.png",self.screen,self.rect.x+100,self.rect.y+100))
class EnemyPlane(object):
    '''敌机抽象类'''
    def __init__(self,img_path,screen):
        self.screen = screen#创建窗口对象
        self.x = 0
        self.y = 0
        self.w = 100
        self.h = 124
        self.img_path = img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
        #定义好的位置和尺寸
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.bullet_list=[]#列表保存发射的子弹
        self.flag = "right"
    def display(self):
        self.screen.blit(self.plane,self.rect)
        self.move()
        num=random.randint(1,60)
        if num==5:
            self.fire()
        for i in self.bullet_list:
            if i.judge():
                self.bullet_list.remove(i)
            i.display()
            i.move()
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



class EnemyBullet(object):
    '''敌机子弹的抽象类'''
    def __init__(self,img_path,screen,x,y):
        self.screen = screen
        self.x = x+40
        self.y = y+20
        self.img_path = img_path
        self.bullet=pygame.image.load(self.img_path)#子弹图片
    def display(self):
        self.screen.blit(self.bullet,(self.x,self.y))#设置子弹
    def move(self):
        self.y += 2
    def judge(self):
        """判断子弹是否飞出了屏幕"""
        if self.y > 500:
            return True#表示子弹飞出了屏幕
        else:
            return False



class Bullet(object):
    '''子弹的抽象类'''
    def __init__(self,img_path,screen,x,y):
        self.screen = screen
        self.x = x
        self.y = y
        self.img_path = img_path
        self.bullet=pygame.image.load(self.img_path)#子弹图片
    def display(self):
        self.screen.blit(self.bullet,(self.x,self.y))#设置子弹
    def move(self):
        self.y -= 2
    def judge(self):
        """判断子弹是否飞出了屏幕"""
        if self.y < 0:
            return True#表示子弹飞出了屏幕
        else:
            return False



def key_control(hero,move_step):
     for event in pygame.event.get():#游戏时间的监听控制
         if event.type == pygame.QUIT:#退出游戏
             print("游戏退出")
             pygame.quit()
             exit()#退出程序
         elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE:
                 hero.fire()
     keys_pressed = pygame.key.get_pressed()
     if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
         if hero.rect.x < 400-hero.rect.width:
            hero.rect.x +=move_step
     if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
         if hero.rect.x > 0:
             hero.rect.x -=move_step
     if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
         if hero.rect.y > 0:
            hero.rect.y -=move_step
     if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
         if hero.rect.y < 500-hero.rect.height:
            hero.rect.y +=move_step




def main():
    #创建游戏窗口
    screen = pygame.display.set_mode((400,500),0,32)
    #把本地文件夹的图片获取到代码中
    background=pygame.image.load("./tupian/background.png")
    #初始化飞机
    hero = Heroplane("./tupian/hero1.png",screen)
    enemy_hero = EnemyPlane("./tupian/enemy1.png",screen)
    clock = pygame.time.Clock()#获得游戏时钟控制器
    move_step = 10 #移动的步长值
    while True:
        #把图片加载到游戏窗口上
        screen.blit(background,(0,0))
        hero.display()
        enemy_hero.display()
        key_control(hero,move_step)
        #刷新显示
        pygame.display.update()
        clock.tick(60)#让游戏时钟，1/60秒运行一次

if __name__=="__main__":
    main()
