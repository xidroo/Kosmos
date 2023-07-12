import pygame
import random
import math
from random import randint
from random import choice
from Rakieta import Rakieta
from Laser import Laser
from Pasek import pasek

SZEROKOSC = 1000
WYSOKOSC = 550

class EnemyWspieracz:
    x = 0
    y = 0
    dx = 0
    dy = 0
    hp = 0
    maxHp = 0
    granicaX = 0
    granicaY = 0
    grafika = pygame.image.load("Grafika\Enemy\enemy15.png")
    grafika.set_colorkey('white')
    szerokosc = grafika.get_width()
    wysokosc = grafika.get_height()
    oslonaD = pygame.mixer.Sound("Dzwieki\sfx_sounds_interaction20.wav")
    wsparcieD = pygame.mixer.Sound("Dzwieki\\sfx_menu_select3.wav")
    kopia = pygame.image.load("Grafika\spr_shield.png")
    oslonaG = pygame.transform.scale(kopia, (szerokosc + 20, wysokosc + 20))
    odpornosc = 0
    czas = 0
    czasZmianyKierunku = 0
    jest = True
    rodzaj = 15
    kat = 0
    stop = False
    czasOslony = 0
    czasOdnawianiaOslony = 0
    oslona = False
    czasWsparcia = 0




    def __init__(self, rodzajMisji):
        self.hp = 250
        self.maxHp = 250
        self.odpornosc = 0
        self.czas = pygame.time.get_ticks()
        self.czasZmianyKierunku = pygame.time.get_ticks()
        self.czasWsparcia = pygame.time.get_ticks()
        self.jest = True
        self.stop = False
        self.trwaWsparcie = False
        if rodzajMisji in [1,2]:
            self.x = randint(100,SZEROKOSC - 100)
            self.y = randint(10,20)
            self.dx = choice([0.3,0.2,0.35,-0.3,-0.2,-0.35])
            self.dy = choice([0.25,0.2,0.1,0.08])
            self.granicaX = 0
            self.granicaY = 100
            self.kat = 0
        if rodzajMisji in [3,4]:
            self.x = randint(SZEROKOSC-80,SZEROKOSC - 60)
            self.y = randint(10,WYSOKOSC - 350)
            self.dx = choice([0.25,0.2,0.1,0.08])
            self.dy = choice([0.3,0.2,0.35,-0.3,-0.2,-0.35])
            self.granicaX = SZEROKOSC-200
            self.granicaY = WYSOKOSC - 20
            kopia = pygame.transform.rotate(self.grafika, -90)
            self.grafika = kopia
            self.grafika.set_colorkey('white')
            self.szerokosc = self.grafika.get_width()
            self.wysokosc = self.grafika.get_height()


        self.czasOslony = pygame.time.get_ticks()
        self.oslona = False
        self.czasOdnawianiaOslony = 5500
    def obliczOdleglosc(self, x1,y1,x2,y2):
        return math.sqrt((x2-x1)**2+(y2-y1)**2)

    def render(self, window, rodzajMisji):

            window.blit(self.grafika, (self.x, self.y))
            if self.oslona:
                window.blit(self.oslonaG, (self.x - 10, self.y - 10))
            pasek(window, self.x, self.y - 2, 4, self.szerokosc, self.maxHp, self.hp, 'black', 'red')


    def update(self, window, ENEMY,LASERY_ENEMY,RAKIETY_ENEMY, rodzajMisji):
        self.x += self.dx
        self.y += self.dy

        if not self.oslona and pygame.time.get_ticks() - self.czasOslony > self.czasOdnawianiaOslony:
            self.oslona = True
            self.oslonaD.play()

        if rodzajMisji in [1,2]:
            if randint(1,1000) <= 15 and pygame.time.get_ticks() - self.czasZmianyKierunku > randint(5000,7000) :
                 self.czasZmianyKierunku = pygame.time.get_ticks()
                 self.dx = - self.dx

        if rodzajMisji == 3:
            if randint(1,1000) <= 15 and pygame.time.get_ticks() - self.czasZmianyKierunku > randint(5000,7000) :
                 self.czasZmianyKierunku = pygame.time.get_ticks()
                 self.dy = - self.dy

        if rodzajMisji in [1, 2]:
            if self.x+self.szerokosc > SZEROKOSC - 10 or self.x < 10:
                self.dx = - self.dx
                self.czasZmianyKierunku = pygame.time.get_ticks()

        if rodzajMisji  == 3:
            if self.x+self.szerokosc > SZEROKOSC - 10 or self.x < 600:
                self.dx = - self.dx
                self.czasZmianyKierunku = pygame.time.get_ticks()

        if rodzajMisji == 4:
            if self.x+self.szerokosc > SZEROKOSC - 10 or self.x < self.granicaX:
                self.dx = - self.dx
                self.czasZmianyKierunku = pygame.time.get_ticks()

        if rodzajMisji in [1, 2]:
            if self.y+self.wysokosc > WYSOKOSC//2 - 100 or self.y < 10:
                self.dy = - self.dy
                self.czasZmianyKierunku = pygame.time.get_ticks()

        if rodzajMisji in [3, 4]:
            if self.y+self.wysokosc > WYSOKOSC - 10 or self.y < 10:
                self.dy = - self.dy
                self.czasZmianyKierunku = pygame.time.get_ticks()

        if pygame.time.get_ticks() - self.czasWsparcia > 5000:
            self.trwaWsparcie = True
            self.czas = pygame.time.get_ticks()
            self.czasWsparcia = pygame.time.get_ticks()
            self.wsparcieD.play()
            for enemy in ENEMY:
                if enemy.rodzaj not in [7,5]:
                    """if enemy.dx > 0:
                        enemy.dx += 0.1
                    else:
                        enemy.dx -= 0.1
                    if enemy.dy > 0:
                        enemy.dy += 0.1
                    else:
                        enemy.dy -= 0.1"""
                    enemy.hp += 25
                    if enemy.hp > enemy.maxHp:
                        enemy.hp = enemy.maxHp

        if self.trwaWsparcie:
            #pygame.draw.circle(window,"red",(self.x,self.y),200,1)
            for enemy in ENEMY:
                if enemy.rodzaj not in [7, 5 , 15]:
                    pygame.draw.line(window,"orange",(self.x+25,self.y+25),(enemy.x+enemy.szerokosc//2,enemy.y+enemy.wysokosc//2),2)

        if pygame.time.get_ticks() - self.czas > 500:
            self.trwaWsparcie = False










        self.render(window,rodzajMisji)

    def hit(self,ile):
        self.hp -= ile
        if self.hp <= 0:
            self.jest = False


    def getRect(self):
        return pygame.Rect((self.x,self.y,self.szerokosc,self.wysokosc))






