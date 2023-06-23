import random

import pygame
from random import randint
from random import choice
from Pasek import pasek

SZEROKOSC = 1000
WYSOKOSC = 550

class Beczka:
    x = 0
    y = 0
    dx= 0
    dy = 0
    maxHp = 0
    hp = 0
    granicaX = 0
    granicaY = 0
    grafikaL = pygame.image.load("Grafika\Enemy\\beczkaL.png")
    grafikaP = pygame.image.load("Grafika\Enemy\\beczkaP.png")
    grafikaL.set_colorkey('white')
    grafikaP.set_colorkey('white')
    szerokosc = grafikaL.get_width()
    wysokosc = grafikaL.get_height()
    grafika = 0
    odpornosc = 0
    czas = 0
    jest = True
    rodzaj = 12
    kat = 0


    def __init__(self,x,y):
        self.hp = 220
        self.maxHp = 220
        self.odpornosc = 0
        self.czas = pygame.time.get_ticks()
        self.jest = True
        self.x = x
        self.y = y
        if x == 300:
            self.grafika = self.grafikaL
        else:
            self.grafika = self.grafikaP


        self.szerokosc = self.grafika.get_width()
        self.wysokosc = self.grafika.get_height()



    def render(self, window, rodzajMisji):
            window.blit(self.grafika, (self.x, self.y))
            pasek(window,self.x,self.y-2,4,self.szerokosc,self.maxHp,self.hp,'black','red')

    def update(self, window, ENEMY,LASERY_ENEMY,RAKIETY_ENEMY, rodzajMisji):

        self.render(window,rodzajMisji)

    def hit(self,ile):
        self.hp -= ile
        if self.hp <= 0:
            self.jest = False

    def getRect(self):
        return pygame.Rect((self.x,self.y,self.szerokosc,self.wysokosc))






