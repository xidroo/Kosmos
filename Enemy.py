import random

import pygame
from random import randint
from random import choice
from Pasek import pasek

SZEROKOSC = 1000
WYSOKOSC = 550

class Enemy:
    x = 0
    y = 0
    dx= 0
    dy = 0
    maxHp = 0
    hp = 0
    granicaX = 0
    granicaY = 0
    grafika = pygame.image.load("Grafika\Enemy\enemy1.png")
    grafika.set_colorkey('white')
    szerokosc = grafika.get_width()
    wysokosc = grafika.get_height()
    odpornosc = 0
    czas = 0
    jest = True
    rodzaj = 1
    kat = 0


    def __init__(self, rodzajMisji):
        self.hp = 50
        self.maxHp = 50
        self.odpornosc = 0
        self.czas = pygame.time.get_ticks()
        self.jest = True
        if rodzajMisji in [1,2]:
            self.x = randint(50,SZEROKOSC - 100)
            self.y = randint(1,100)
            if rodzajMisji == 2:
                if random.choice((1,2)) == 1:
                    self.x = 388
                    self.y = 90
                else:
                    self.x = 588
                    self.y = 90
            self.dx = choice([-1,-1.5,-2,0,1,2,1.5])
            self.dy = choice([0.5,0.4,0.3,0.2,0.1])
            self.granicaX = 0
            self.granicaY = 500
            self.kat = 0
        if rodzajMisji == 3:
            self.x = randint(SZEROKOSC-200, SZEROKOSC - 100)
            self.y = randint(100, WYSOKOSC-300)
            self.dx = choice([-1, -1.5, -2, 1, 2, 1.5])
            self.dy = choice([0.5, 0.4, 0.3, 0, -0.5, -0.4, -0.3])
            self.granicaX = 20
            self.granicaY = WYSOKOSC
            kopia = pygame.transform.rotate(self.grafika, -90)
            self.grafika = kopia
            self.grafika.set_colorkey('white')
            self.szerokosc = self.grafika.get_width()
            self.wysokosc = self.grafika.get_height()
        if rodzajMisji == 4:
            self.x = 0
            self.y = 0
            self.dx = 1.5
            self.dy = 0.6
            self.granicaX = SZEROKOSC//2
            self.granicaY = WYSOKOSC
            kopia = pygame.transform.rotate(self.grafika, -90)
            self.grafika = kopia
            self.grafika.set_colorkey('white')
            self.szerokosc = self.grafika.get_width()
            self.wysokosc = self.grafika.get_height()



    def render(self, window, rodzajMisji):
            window.blit(self.grafika, (self.x, self.y))
            pasek(window,self.x,self.y-2,4,self.szerokosc,self.maxHp,self.hp,'black','red')

    def update(self, window, ENEMY,LASERY_ENEMY,RAKIETY_ENEMY, rodzajMisji):
        self.x += self.dx
        self.y += self.dy

        if rodzajMisji in [1,2]:
            if self.x+self.szerokosc > SZEROKOSC or self.x < 1:
                self.dx = - self.dx

            if self.y+self.wysokosc > self.granicaY or self.y < 1:
                self.dy = - self.dy

        if rodzajMisji in [3,4]:
            if self.x+self.szerokosc > SZEROKOSC -5 or self.x < self.granicaX:
                self.dx = - self.dx

            if self.y+self.wysokosc > self.granicaY or self.y < 1:
                self.dy = - self.dy

        self.render(window,rodzajMisji)

    def hit(self,ile):
        self.hp -= ile
        if self.hp <= 0:
            self.jest = False

    def getRect(self):
        return pygame.Rect((self.x,self.y,self.szerokosc,self.wysokosc))






