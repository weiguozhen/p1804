#coding=utf-8
import time
import pygame
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
    def display(self):
        self.screen.blit(self.hero_plane,self.rect)



def main():
    #创建游戏窗口
    screen = pygame.display.set_mode((400,500),0,32)
    #把本地文件夹的图片获取到代码中
    background=pygame.image.load("./tupian/background.png")
    #初始化飞机
    hero = Heroplane("./tupian/hero1.png",screen)
    clock = pygame.time.Clock()#获得游戏时钟控制器
    move_step = 10 #移动的步长值
    while True:
        #把图片加载到游戏窗口上
        screen.blit(background,(0,0))
        hero.display()
            #print("event.type",event.type)
            #print("event=",event)
            if event.type == pygame.QUIT:#退出游戏
                print("游戏退出")
                pygame.quit()
                exit()#退出程序

            #elif event.type == pygame.KEYDOWN:
             #   if event.key == pygame.K_UP:
              #      rect.y -= move_step
               # if event.key == pygame.K_DOWN:
                #    rect.y += move_step
                #if event.key == pygame.K_LEFT:
                 #   rect.x -= move_step
               # if event.key == pygame.K_RIGHT:
                #    rect.x += move_step
          #  elif event.type == pygame.KEYUP:
           #     pass
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            hero.rect.x += move_step
        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            hero.rect.x -= move_step
        if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
            hero.rect.y -= move_step
        if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
            hero.rect.y += move_step

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
