import pygame



class zidan(object):
    def __init__(self,img_path,screen,x,y):
        self.screen = screen
        self.x = x
        self.y = y
        self.img_path = img_path
        self.bullet=pygame.image.load(self.img_path)
    def display(self):
        self.screen.blit(self.bullet,(self.x,self.y))



