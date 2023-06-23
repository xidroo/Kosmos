import random

import pygame
from random import randint
from random import choice

SZEROKOSC = 1000
WYSOKOSC = 550

class Meteor:
    x = 0
    y = 0
    dx= 0
    dy = 0
    hp = 0
    granicaX = 0
    granicaY = 0
    grafiki = []
    grafikiMale = []
    grafikiDuze = []
    klatka = 0
    szybkoscKlatkowania = 100

    sciezka = "Grafika\Meteor\\c1000"
    for i in range(16):
        if i < 10:
            sciezka = "Grafika\Meteor\\c1000"
        else:
            sciezka = "Grafika\Meteor\\c100"
        sciezka += str(i)
        sciezka += ".png"
        grafikiDuze.append(pygame.image.load(sciezka))

    for grafika in grafikiDuze:
        grafika.set_colorkey('white')

    sciezka = "Grafika\Meteor\\b1000"
    for i in range(16):
        if i < 10:
            sciezka = "Grafika\Meteor\\b1000"
        else:
            sciezka = "Grafika\Meteor\\b100"
        sciezka += str(i)
        sciezka += ".png"
        grafikiMale.append(pygame.image.load(sciezka))

    for grafika in grafikiMale:
        grafika.set_colorkey('white')


    odpornosc = 0
    czas = 0
    jest = True
    rodzaj = 5
    kat = 0


    def __init__(self, rodzajMisji):
        self.hp = 300
        self.odpornosc = 0
        self.czas = pygame.time.get_ticks()
        self.jest = True
        if random.randint(1,100) > 50:
            self.grafiki = self.grafikiMale
            self.hp = 100
            self.szybkoscKlatkowania = 75
        else:
            self.grafiki = self.grafikiDuze
            self.szybkoscKlatkowania = 100


            self.szybkoscKlatkowania = 100
        self.szerokosc = self.grafiki[0].get_width()
        self.wysokosc = self.grafiki[0].get_height()
        self.klatka = random.choice((0,1,2,3,4,5,6,7,8,9))
        if rodzajMisji in [3,4]:
            self.x = randint(SZEROKOSC+100, SZEROKOSC + 200)
            self.y = randint(5, WYSOKOSC-100)
            self.dx = choice([-5, -5.5,-5.6,-5.7, -4.8,-4.9,-5.8 ])
            self.dy = 0
            self.granicaX = 0
            self.granicaY = WYSOKOSC




    def render(self, window, rodzajMisji):
            window.blit(self.grafiki[self.klatka], (self.x, self.y))

    def update(self, window, ENEMY,LASERY_ENEMY,RAKIETY_ENEMY, rodzajMisji):
        self.x += self.dx


        if pygame.time.get_ticks() - self.czas > 100:
            self.czas = pygame.time.get_ticks()
            self.klatka += 1
            if self.klatka >= len(self.grafiki) - 1:
                self.klatka = 0

        if rodzajMisji in [3,4]:
            if self.x < -60:
                self.x = randint(SZEROKOSC,SZEROKOSC + 300)
                self.y = randint(5, WYSOKOSC-100)

        self.render(window,rodzajMisji)

    def hit(self,ile):
        self.hp -= ile
        if self.hp <= 0:
            self.jest = False

    def getRect(self):
        return pygame.Rect((self.x+30,self.y+30,self.szerokosc-30,self.wysokosc-30))






