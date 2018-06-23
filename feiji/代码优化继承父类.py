#coding=utf-8
import pygame
import time,random
class Base(object):
    def __init__(self,screen,x,y,image_name):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_name)

class BasePlane(Base):
    '''飞机爸爸'''
    def __init__(self,screen,x,y,image_name):
        Base.__init__(self,screen,x,y,image_name)
        self.rect=pygame.Rect(self.x,self.y,102,126)
        self.bullet_list=[]#保存子弹引用
        self.bullet_remove=[]#保存待删除的子弹
        self.hit=False #表示没有击中不爆炸
        self.bomb_list = []#保存爆炸效果图
        self.__create_image()#添加图片
        self.image_num=0#while true 增加次数效果延迟
        self.image_index=0#爆炸图片
    def __create_image(self):
        self.bomb_list.append(pygame.image.load("./tupian/hero_blowup_n1.png"))
        self.bomb_list.append(pygame.image.load("./tupian/hero_blowup_n2.png"))
        self.bomb_list.append(pygame.image.load("./tupian/hero_blowup_n3.png"))
        self.bomb_list.append(pygame.image.load("./tupian/hero_blowup_n4.png"))
    def display(self):
        if self.hit==True:
            self.screen.blit(self.bomb_list[self.image_index],self.rect)
            self.image_num+=1
            if self.image_num==7:
                self.image_index+=1
                self.image_num = 0
            if self.image_index > 3:
                time.sleep(1)
                exit()
        else:
            self.screen.blit(self.image,self.rect)
        if len(self.bullet_list)>0:
            for bullet in self.bullet_list:
                bullet.display()
                bullet.move()
                if bullet.judge():
                    self.bullet_remove.append(bullet)
            if len(self.bullet_remove)>0:
                for i in self.bullet_remove:
                    self.bullet_list.remove(i)
                del self.bullet_remove[:]
    def bomb(self):
        self.hit = True







class HeroPlane(BasePlane):
    '''飞机抽象类'''
    def __init__(self,screen):
        super(HeroPlane,self).__init__(screen,150,500,"./tupian/hero1.png")
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.rect.x-20,self.rect.y+100))
        self.bullet_list.append(Bullet(self.screen,self.rect.x+40,self.rect.y))
        self.bullet_list.append(Bullet(self.screen,self.rect.x+100,self.rect.y+100))
class EnemyPlane(BasePlane):
    '''敌机抽象类'''
    def __init__(self,screen):
        super(EnemyPlane,self).__init__(screen,0,0,"./tupian/enemy0.png")
        self.flag = "right"
    def move(self):
        if self.flag == "right":
            self.rect.x += 2
        elif self.flag == "left":
            self.rect.x -= 2
        if self.rect.x > 400 - self.rect.width:
            self.flag ="left"
        elif self.rect.x <= 0:
            self.flag = "right"
    def fire(self):
        if random.randint(1,100)==78:
            self.bullet_list.append(EnemyBullet(self.screen,self.rect.x,self.rect.y))



class BaseBullet(Base):
    def __init__(self,screen,x,y,image_name):
        Base.__init__(self,screen,x,y,image_name)
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))



class EnemyBullet(BaseBullet):
    '''敌机子弹的抽象类'''
    def __init__(self,screen,x,y):
        BaseBullet.__init__(self,screen,x+25,y+20,"./tupian/bullet1.png")
    def move(self):
        self.y += 2
    def judge(self):
        """判断子弹是否飞出了屏幕"""
        if self.y > 500:
            return True#表示子弹飞出了屏幕
        else:
            return False
class Bullet(BaseBullet):
    '''子弹的抽象类'''
    def __init__(self,screen,x,y):
        BaseBullet.__init__(self,screen,x+40,y+20,"./tupian/bullet.png")
    def move(self):
        self.y -= 2
    def judge(self):
        """判断子弹是否飞出了屏幕"""
        if self.y < 0:
            return True#表示子弹飞出了屏幕
        else:
            return False



def key_control(hero):

    move_step = 5
    move_x,move_y=0,0
    for event in pygame.event.get():#游戏时间的监听控制
        if event.type == pygame.QUIT:#退出游戏
            print("游戏退出")
            pygame.quit()
            exit()#退出程序
        elif event.type == pygame.KEYDOWN:
          #  if event.key == pygame.K_LEFT:
           #     move_x = -move_step
           # elif event.key==pygame.K_RIGHT:
           #     move_x = move_step
           # elif event.key==pygame.K_UP:
           #     move_y = -move_step
           # elif event.key==pygame.K_DOWN:
           #     move_y = move_step
           if event.key == pygame.K_SPACE:
                hero.fire()
           elif event.key == pygame.K_b:
                hero.bomb()
        #elif event.type == pygame.KEYUP:
        #    move_X=0
         #   move_y=0

        #hero.rect.x += move_x
       # hero.rect.y += move_y

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        if hero.rect.x < 400-hero.rect.width:
            hero.rect.x +=move_step
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        if hero.rect.x > 100:
            hero.rect.x -=move_step
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        if hero.rect.y > 100:
            hero.rect.y -=move_step
    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        if hero.rect.y < 500-hero.rect.height:
            hero.rect.y +=move_step
    #if event.key == pygame.K_b:
     #       hero.bomb()






def main():
    #创建游戏窗口
    screen = pygame.display.set_mode((400,500),0,32)
    #把本地文件夹的图片获取到代码中
    background=pygame.image.load("./tupian/background.png")
    #初始化飞机
    hero = HeroPlane(screen)
    enemy = EnemyPlane(screen)
    clock = pygame.time.Clock()#获得游戏时钟控制器
    move_step = 10 #移动的步长值
    while True:
        #把图片加载到游戏窗口上
        screen.blit(background,(0,0))
        hero.display()
        enemy.move()
        enemy.display()
        enemy.fire()
        clock.tick(60)
        if hero.rect.y <= 0:
            hero.rect.y = 500
        key_control(hero)
        #刷新显示
        pygame.display.update()

if __name__=="__main__":
    main()
