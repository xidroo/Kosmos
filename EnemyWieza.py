import random

import pygame
import math
from random import randint
from random import choice
from Laser import Laser
from Pasek import pasek
SZEROKOSC = 1000
WYSOKOSC = 550

class EnemyWieza:
    x = 0
    y = 0
    dx= 0
    dy = 0
    hp = 0
    maxHp = 0
    granicaX = 0
    granicaY = 0
    grafika = pygame.image.load("Grafika\Enemy\wieza.png")
    pygame.mixer.init()
    laserD = pygame.mixer.Sound("Dzwieki\Laser_09.wav")
    laserD.set_volume(0.1)
    grafika.set_colorkey('white')
    szerokosc = grafika.get_width()
    wysokosc = grafika.get_height()
    odpornosc = 0
    czas = 0
    jest = True
    rodzaj = 11


    def __init__(self, rodzajMisji,x,y):
        self.hp = 140
        self.maxHp = 140
        self.odpornosc = 0
        self.czas = pygame.time.get_ticks()
        self.jest = True
        self.kat = 0
        if rodzajMisji in [1,2]:
            self.x = x
            self.y = y
            self.dx = 0
            self.dy = 0
            kopia = pygame.transform.rotate(self.grafika, 180)
            self.grafika = kopia
            self.grafika.set_colorkey('white')
            self.granicaX = 0
            self.granicaY = 350
        if rodzajMisji == 3:
            self.x = SZEROKOSC -200
            self.y = WYSOKOSC // 2
            self.dx = 0
            self.dy = 0
            self.granicaX = 300
            self.granicaY = WYSOKOSC
            kopia = pygame.transform.rotate(self.grafika, 180)
            self.grafika = kopia
            self.grafika.set_colorkey('white')
            self.szerokosc = self.grafika.get_width()
            self.wysokosc = self.grafika.get_height()
        if rodzajMisji == 4:
            self.x = 0
            self.y = 0
            self.dx = 0
            self.dy = 0
            self.x = SZEROKOSC -200
            self.y = WYSOKOSC // 2
            kopia = pygame.transform.rotate(self.grafika, 180)
            self.grafika = kopia
            self.grafika.set_colorkey('white')
            self.szerokosc = self.grafika.get_width()
            self.wysokosc = self.grafika.get_height()

    def obliczKat(self,GRACZ):
        srodekX = self.x + self.grafika.get_width() // 2
        srodekY = self.y + self.grafika.get_height() // 2
        cwiartka = 1

        namiarX = GRACZ.x + 40
        namiarY = GRACZ.y + 40

        if namiarX > srodekX and namiarY < srodekY:
            cwiartka = 1
        if namiarX > srodekX and namiarY >= srodekY:
            cwiartka = 2
        if namiarX <= srodekX and namiarY >= srodekY:
            cwiartka = 3
        if namiarX <= srodekX and namiarY < srodekY:
            cwiartka = 4

        odleglosc = math.sqrt((namiarX - srodekX) ** 2 + (namiarY - srodekY) ** 2)
        if cwiartka == 1:
            a = namiarX - srodekX
        if cwiartka == 2:
            a = namiarY - srodekY
        if cwiartka == 3:
            a = srodekX - namiarX
        if cwiartka == 4:
            a = srodekY - namiarY

        kat = math.asin(a / odleglosc)
        kat = (kat * 180) / math.pi

        if cwiartka == 2: kat += 90
        if cwiartka == 3: kat += 180
        if cwiartka == 4: kat += 270

        self.kat =  -int(kat)

    def render(self, window, rodzajMisji):
        kopia = pygame.transform.rotate(self.grafika, self.kat)

        rect = kopia.get_rect()
        kopia.set_colorkey('white')
        nx = (self.x + (self.grafika.get_width() - rect.width) / 2)
        ny = (self.y + ((self.grafika.get_height() - rect.height) / 2))

        window.blit(kopia, (nx, ny))
        pasek(window, self.x-3, self.y - 2, 4, self.szerokosc, self.maxHp, self.hp, 'black', 'red')


    def update(self, window, ENEMY,LASERY_ENEMY,RAKIETY_ENEMY, rodzajMisji):
        self.render(window, rodzajMisji)

        """self.x += self.dx
        self.y += self.dy

        """
        if pygame.time.get_ticks() - self.czas > 1000:
            self.czas = pygame.time.get_ticks()
            self.laserD.play()

            LASERY_ENEMY.append(Laser(self.x + self.grafika.get_width() // 2 - self.grafika.get_width() // 2 * math.sin(self.kat * math.pi / 180), self.y + self.grafika.get_height() // 2 - self.grafika.get_height() // 2 * math.cos(self.kat * math.pi / 180), -5 * math.sin(self.kat * math.pi / 180), -5 * math.cos(self.kat * math.pi / 180), self.kat, rodzajMisji, 10))



    def hit(self,ile):
        self.hp -= ile
        if self.hp <= 0:
            self.jest = False

    def getRect(self):
        return pygame.Rect((self.x,self.y,self.szerokosc,self.wysokosc))






