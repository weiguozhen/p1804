from 代码优化继承父类 import *

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
        screen.blit(background,(0,0))
        hero.display()
        enemy_hero.move()
        enemy_hero.display()
        if random.randint(1,60)==5:
            enemy_hero.fire()
        key_control(hero,move_step)
        #刷新显示
        pygame.display.update()
        clock.tick(60)#让游戏时钟，1/60秒运行一次

if __name__=="__main__":
    main()
