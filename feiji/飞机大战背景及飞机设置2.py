#coding=utf-8
import pygame
def main():
    #创建游戏窗口
    screen = pygame.display.set_mode((400,500),0,32)
    #把本地文件夹的图片获取到代码中
    background=pygame.image.load("./tupian/background.png")
    hero_plane=pygame.image.load("./tupian/hero1.png")
    #把图片加载到游戏窗口上
    screen.blit(background,(0,0))
    screen.blit(hero_plane,((400-100)/2,350))
    #刷新显示
    pygame.display.update()
    while True:
        pass





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
