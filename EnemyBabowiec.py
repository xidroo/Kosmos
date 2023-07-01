import pygame
from random import randint
from random import choice
from EnemyBomb import EnemyBomb
from Pasek import pasek

SZEROKOSC = 1000
WYSOKOSC = 550

class EnemyBabowiec:
    x = 0
    y = 0
    dx = 0
    dy = 0
    hp = 0
    maxHp = 0
    granicaX = 0
    granicaY = 0
    grafika = pygame.image.load("Grafika\Enemy\enemy6.png")
    bombaD = pygame.mixer.Sound("Dzwieki\sfx_sounds_falling7.wav")
    grafika.set_colorkey('white')
    szerokosc = grafika.get_width()
    wysokosc = grafika.get_height()
    oslonaD = pygame.mixer.Sound("Dzwieki\sfx_sounds_interaction20.wav")
    kopia = pygame.image.load("Grafika\spr_shield.png")
    oslonaG = pygame.transform.scale(kopia, (szerokosc + 20, wysokosc + 20))
    odpornosc = 0
    czas = 0
    czasZmianyKierunku = 0
    jest = True
    rodzaj = 6
    kat = 0
    stop = False
    czasStop = 0
    czasStrzalu = 0
    zapamietaneDx = 0
    zapamietaneDy = 0
    czasStrzalu = 0
    czasOslony = 0
    czasOdnawianiaOslony = 0
    oslona = False


    def __init__(self, rodzajMisji):
        self.hp = 175
        self.maxHp = 175
        self.odpornosc = 0
        self.czas = pygame.time.get_ticks()
        self.czasZmianyKierunku = pygame.time.get_ticks()
        self.jest = True
        self.czasOslony = pygame.time.get_ticks()
        self.oslona = False
        self.czasOdnawianiaOslony = 6000
        if rodzajMisji in [1,2]:
            self.x = randint(50,SZEROKOSC - 100)
            self.y = randint(1,100)
            self.dx = choice([-1.4,-1.1,1.1,1.4,1.2,-1.2,1.3,-1.3])
            self.dy = choice([0.3,0.5,0.2,0.4])
            self.granicaX = 0
            self.granicaY = 180
            self.kat = 0
            self.stop = False
            self.czasStop = pygame.time.get_ticks()
            self.zapamietaneDx = self.dx
            self.zapamietaneDy = self.dy




    def render(self, window, rodzajMisji):
            window.blit(self.grafika, (self.x, self.y))
            if self.oslona:
                window.blit(self.oslonaG, (self.x - 10, self.y - 10))
            pasek(window, self.x, self.y - 2, 4, self.szerokosc, self.maxHp, self.hp, 'black', 'red')


    def update(self, window, ENEMY,LASERY_ENEMY,RAKIETY_ENEMY, rodzajMisji):

        if not self.oslona and pygame.time.get_ticks() - self.czasOslony > self.czasOdnawianiaOslony:
            self.oslona = True
            self.oslonaD.play()

        if not self.stop:
            self.x += self.dx
            self.y += self.dy


        if randint(1,1000) <= 25 and pygame.time.get_ticks() - self.czasZmianyKierunku > randint(5000,7000) :
             self.czasZmianyKierunku = pygame.time.get_ticks()
             self.dx = - self.dx

        if pygame.time.get_ticks() - self.czas  > randint(5000,12000) and not self.stop:
            self.stop = True
            self.czasStop = pygame.time.get_ticks()


        if pygame.time.get_ticks() - self.czasStop > 1000 and self.stop:
            self.czas = pygame.time.get_ticks()
            self.stop = False
            self.bombaD.play()
            ENEMY.append(EnemyBomb(self.x+self.szerokosc//2,self.y+self.wysokosc//2+10 ))


        if self.x+self.szerokosc > SZEROKOSC-10 or self.x < 10:
            self.dx = - self.dx
            self.czasZmianyKierunku = pygame.time.get_ticks()

        if self.y+self.wysokosc > self.granicaY or self.y < 10:
            self.dy = - self.dy
            self.czasZmianyKierunku = pygame.time.get_ticks()



        self.render(window,rodzajMisji)

    def hit(self,ile):
        self.hp -= ile
        if self.hp <= 0:
            self.jest = False

    def getRect(self):
        return pygame.Rect((self.x,self.y,self.szerokosc,self.wysokosc))






