#coding=utf-8
import time
import pygame
def main():
    #创建游戏窗口
    screen = pygame.display.set_mode((400,500),0,32)
    #把本地文件夹的图片获取到代码中
    background=pygame.image.load("./tupian/background.png")
    hero_plane=pygame.image.load("./tupian/hero1.png")
    #定义好位置和尺寸
    rect = pygame.Rect((400-100)/2,350,100,124)
    clock = pygame.time.Clock()#获得游戏时钟控制器
    move_step = 10 #移动的步长值
    while True:
        #把图片加载到游戏窗口上
        screen.blit(background,(0,0))
        screen.blit(hero_plane,rect)
        #移动飞机
        #rect.x += 1
       # if rect.x > 400:
        #    rect.x = 0
        #游戏时间的监听 控制
        for event in pygame.event.get():
            #print("event.type",event.type)
            #print("event=",event)
            if event.type == pygame.QUIT:#退出游戏
                print("游戏退出")
                pygame.quit()
                exit()#退出程序
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    rect.y -= move_step
                if event.key == pygame.K_DOWN:
                    rect.y += move_step
                if event.key == pygame.K_LEFT:
                    rect.x -= move_step
                if event.key == pygame.K_RIGHT:
                    rect.x += move_step
            elif event.type == pygame.KEYUP:
                pass

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
