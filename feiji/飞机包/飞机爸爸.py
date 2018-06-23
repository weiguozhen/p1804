import pygame

class plane(object):
    '''飞机爸爸'''
    def __init__(self,img_path,screen,x,y):
        self.screen=screen
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane = pygame.image.load(self.img_path)
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.bullet_list=[]
    def display(self):
        self.screen.blit(self.plane,self.rect)
        for i in self.bullet_list:
            if i.judge():
                self.bullet_list.remove(i)
            i.display()
            i.move()


