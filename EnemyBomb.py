import pygame
from random import randint
from random import choice

SZEROKOSC = 1000
WYSOKOSC = 550

class EnemyBomb:
    x = 0
    y = 0
    dx= 0
    dy = 0
    hp = 0
    granicaX = 0
    granicaY = 0
    grafika = pygame.image.load("Grafika\Enemy\enemy7.png")
    grafika.set_colorkey('white')
    szerokosc = grafika.get_width()
    wysokosc = grafika.get_height()
    odpornosc = 0
    czas = 0
    jest = True
    rodzaj = 7
    kat = 0


    def __init__(self,x,y):
        self.hp = 20
        self.odpornosc = 0
        self.czas = pygame.time.get_ticks()
        self.jest = True
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 2
        self.granicaX = 0
        self.granicaY = WYSOKOSC
        self.kat = 0

    def render(self, window, rodzajMisji):
            window.blit(self.grafika, (self.x, self.y))

    def update(self, window, ENEMY,LASERY_ENEMY,RAKIETY_ENEMY, rodzajMisji):
        self.y += self.dy

        if self.y+self.wysokosc > self.granicaY:
                self.jest = False

        self.render(window,rodzajMisji)

    def hit(self,ile):
        self.hp -= ile
        if self.hp <= 0:
            self.jest = False

    def getRect(self):
        return pygame.Rect((self.x,self.y,self.szerokosc,self.wysokosc))






