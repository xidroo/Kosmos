import pygame
import random
from random import randint
from random import choice
from Rakieta import Rakieta
from Laser import Laser
from Pasek import pasek

SZEROKOSC = 1000
WYSOKOSC = 550

class EnemyHybryd:
    x = 0
    y = 0
    dx = 0
    dy = 0
    hp = 0
    maxHp = 0
    granicaX = 0
    granicaY = 0
    grafika = pygame.image.load("Grafika\Enemy\enemy14.png")
    rakietaD = pygame.mixer.Sound("Dzwieki\sfx_sounds_falling11.wav")
    laserD = pygame.mixer.Sound("Dzwieki\Laser_09.wav")
    laserD.set_volume(0.1)
    grafika.set_colorkey('white')
    szerokosc = grafika.get_width()
    wysokosc = grafika.get_height()
    oslonaD = pygame.mixer.Sound("Dzwieki\sfx_sounds_interaction20.wav")
    kopia = pygame.image.load("Grafika\spr_shield.png")
    oslonaG = pygame.transform.scale(kopia, (szerokosc + 20, wysokosc + 20))
    odpornosc = 0
    czas = 0
    czasZmianyKierunku = 0
    czasPomiedzyLaserami = 1500
    jest = True
    rodzaj = 14
    kat = 0
    stop = False
    czasOslony = 0
    czasOdnawianiaOslony = 0
    oslona = False




    def __init__(self, rodzajMisji):
        self.hp = 420
        self.maxHp = 420
        self.odpornosc = 0
        self.czas = pygame.time.get_ticks()
        self.czasZmianyKierunku = pygame.time.get_ticks()
        self.czasStrzalu = pygame.time.get_ticks()
        self.jest = True
        self.stop = False
        self.czasPomiedzyLaserami = 1500
        if rodzajMisji in [1,2]:
            self.x = randint(100,SZEROKOSC - 100)
            self.y = randint(10,50)
            if rodzajMisji == 2:
                if random.choice((1,2)) == 1:
                    self.x = 388
                    self.y = 90
                else:
                    self.x = 588
                    self.y = 90
            self.dx = choice([0.3,0.2,0.35,-0.3,-0.2,-0.35])
            self.dy = choice([0.3,0.2,0.1,0.08])
            self.granicaX = 0
            self.granicaY = 150
            self.kat = 0
        if rodzajMisji == 3:
            self.x = randint(SZEROKOSC-300,SZEROKOSC - 150)
            self.y = randint(10,WYSOKOSC - 300)
            self.dx = choice([0.3,0.2,0.1,0.08])
            self.dy = choice([0.3,0.2,0.35,-0.3,-0.2,-0.35])
            self.granicaX = SZEROKOSC//2+200
            self.granicaY = WYSOKOSC - 20
            kopia = pygame.transform.rotate(self.grafika, -90)
            self.grafika = kopia
            self.grafika.set_colorkey('white')
            self.szerokosc = self.grafika.get_width()
            self.wysokosc = self.grafika.get_height()
        if rodzajMisji == 4:
            self.x = SZEROKOSC - 300
            self.y = WYSOKOSC//2
            self.dx = 0.7
            self.dy = 0.35
            self.granicaX = SZEROKOSC//2+200
            self.granicaY = WYSOKOSC - 20
            kopia = pygame.transform.rotate(self.grafika, -90)
            self.grafika = kopia
            self.grafika.set_colorkey('white')
            self.szerokosc = self.grafika.get_width()
            self.wysokosc = self.grafika.get_height()

        self.czasOslony = pygame.time.get_ticks()
        self.oslona = False
        self.czasOdnawianiaOslony = 8000


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
            if randint(1,1000) <= 8 and pygame.time.get_ticks() - self.czasZmianyKierunku > randint(5000,7000) :
                 self.czasZmianyKierunku = pygame.time.get_ticks()
                 self.dx = - self.dx

        if rodzajMisji == 3:
            if randint(1,1000) <= 8 and pygame.time.get_ticks() - self.czasZmianyKierunku > randint(5000,7000) :
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

        if pygame.time.get_ticks() - self.czasStrzalu > self.czasPomiedzyLaserami:
            self.czasStrzalu = pygame.time.get_ticks()
            self.laserD.play()

            if rodzajMisji in [1,2]:
                LASERY_ENEMY.append(Laser(self.x+10,self.y+self.wysokosc,0,5,0,rodzajMisji,15))
                LASERY_ENEMY.append(Laser(self.x+self.szerokosc - 10,self.y+self.wysokosc,0,5,0,rodzajMisji,15))
                LASERY_ENEMY.append(Laser(self.x+self.szerokosc//2,self.y+self.wysokosc+20,0,5,0,rodzajMisji,10))
            if rodzajMisji in [3,4]:
                LASERY_ENEMY.append(Laser(self.x,self.y+10,-5,0,-90,rodzajMisji,15))
                LASERY_ENEMY.append(Laser(self.x,self.y+self.wysokosc-10,-5,0,-90,rodzajMisji,15))
                LASERY_ENEMY.append(Laser(self.x + 20,self.y+self.wysokosc//2,-5,0,-90,rodzajMisji,10))


        self.render(window,rodzajMisji)

    def hit(self,ile):
        self.hp -= ile
        if self.hp <= 0:
            self.jest = False

    def getRect(self):
        return pygame.Rect((self.x,self.y,self.szerokosc,self.wysokosc))






