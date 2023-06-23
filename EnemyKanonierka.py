import pygame
import math
from random import randint
from random import choice
from Laser import Laser
from Pasek import pasek
SZEROKOSC = 1000
WYSOKOSC = 550

class EnemyKanonierka:
    x = 0
    y = 0
    dx = 0
    dy = 0
    hp = 0
    maxHp = 0
    aktualnaDx = 0
    aktualnaDy = 0
    granicaX = 0
    granicaY = 0
    grafika = pygame.image.load("Grafika\Enemy\enemy3.png")
    pygame.mixer.init()
    laserD = pygame.mixer.Sound("Dzwieki\Laser_09.wav")
    laserD.set_volume(0.1)
    grafika.set_colorkey('white')
    szerokosc = grafika.get_width()
    wysokosc = grafika.get_height()
    odpornosc = 0
    czasStrzalu = 0
    czasZmianyKierunku = 0
    zwrot = True
    jest = True
    rodzaj = 3


    def __init__(self, rodzajMisji):
        self.hp = 140
        self.maxHp = 140
        self.odpornosc = 0
        self.czasStrzalu = pygame.time.get_ticks()
        self.czasZmianyKierunku = pygame.time.get_ticks()
        self.jest = True
        self.zwrot = False
        if rodzajMisji in [1,2]:
            self.x = randint(100,SZEROKOSC - 120)
            self.y = randint(1,50)
            self.dx = choice([-1.9,-1.8,-1.6,-1.7,-2,2,1.6,1.8,1.7,1.9])
            self.dy = choice([0.5,0.4,0.3,0.2,0.1])
            self.aktualnaDx = self.dx
            self.aktualnaDy = self.dy
            self.granicaX = 0
            self.granicaY = 300
        if rodzajMisji == 3:
            self.x = randint(SZEROKOSC-300,SZEROKOSC - 200)
            self.y = randint(100,WYSOKOSC - 200)
            self.dx = choice([-0.8,-0.6,-0.7,-0.4,0.4,0.6,0.8,0.7])
            self.dy = choice([0.8,0.9,1,1.1,-0.8,-0.9,-1,-1.1])
            self.aktualnaDx = self.dx
            self.aktualnaDy = self.dy
            self.granicaX = SZEROKOSC//2
            self.granicaY = WYSOKOSC - 20
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
            self.aktualnaDx = self.dx
            self.aktualnaDy = self.dy
            self.granicaX = 400
            self.granicaY = WYSOKOSC
            kopia = pygame.transform.rotate(self.grafika, -90)
            self.grafika = kopia
            self.grafika.set_colorkey('white')
            self.szerokosc = self.grafika.get_width()
            self.wysokosc = self.grafika.get_height()


    def render(self, window, rodzajMisji):
        window.blit(self.grafika,(self.x,self.y))
        pasek(window, self.x, self.y - 2, 4, self.szerokosc, self.maxHp, self.hp, 'black', 'red')

    def update(self, window, ENEMY,LASERY_ENEMY,RAKIETY_ENEMY, rodzajMisji):
        self.x += self.aktualnaDx
        self.y += self.aktualnaDy

        if rodzajMisji in [1,2]:
            if self.x+self.szerokosc > SZEROKOSC or self.x < 1:
                self.aktualnaDx = - self.aktualnaDx


            if self.y+self.wysokosc > self.granicaY or self.y < 1:
                self.aktualnaDy = - self.aktualnaDy


            if pygame.time.get_ticks() - self.czasZmianyKierunku > randint(5000,7000):
                self.czasZmianyKierunku = pygame.time.get_ticks()
                self.aktualnaDx = - self.aktualnaDx


        if rodzajMisji in [3, 4]:
            if self.x + self.szerokosc > SZEROKOSC - 20 or self.x < self.granicaX:
                self.aktualnaDx = - self.aktualnaDx

            if self.y + self.wysokosc > self.granicaY or self.y < 10:
                self.aktualnaDy = - self.aktualnaDy

            if pygame.time.get_ticks() - self.czasZmianyKierunku > randint(5000,7000):
                self.czasZmianyKierunku = pygame.time.get_ticks()
                self.aktualnaDy = - self.aktualnaDy


        if pygame.time.get_ticks() - self.czasStrzalu > randint(2500, 4000):
            self.czasStrzalu = pygame.time.get_ticks()
            self.laserD.play()
            if rodzajMisji in [1,2]:
                LASERY_ENEMY.append(Laser(self.x+10,self.y+self.wysokosc,0,5,0,rodzajMisji,10))
                LASERY_ENEMY.append(Laser(self.x+self.szerokosc - 10,self.y+self.wysokosc,0,5,0,rodzajMisji,10))
            if rodzajMisji in [3,4]:
                LASERY_ENEMY.append(Laser(self.x,self.y+10,-5,0,-90,rodzajMisji,10))
                LASERY_ENEMY.append(Laser(self.x,self.y+self.wysokosc-10,-5,0,-90,rodzajMisji,10))

        self.render(window,rodzajMisji)

    def hit(self,ile):
        self.hp -= ile
        if self.hp <= 0:
            self.jest = False

    def getRect(self):
        return pygame.Rect((self.x,self.y,self.szerokosc,self.wysokosc))






