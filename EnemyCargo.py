import pygame
from random import randint
from random import choice
from Laser import Laser
from Pasek import pasek
SZEROKOSC = 1000
WYSOKOSC = 550

class EnemyCargo:
    x = 0
    y = 0
    dx = 0
    dy = 0
    hp = 0
    maxHp = 0
    granicaX = 0
    granicaY = 0
    grafika = pygame.image.load("Grafika\Enemy\enemy8.png")
    oslonaD = pygame.mixer.Sound("Dzwieki\sfx_sounds_interaction20.wav")
    grafika.set_colorkey('white')
    szerokosc = grafika.get_width()
    wysokosc = grafika.get_height()
    kopia = pygame.image.load("Grafika\spr_shield.png")
    oslonaG = pygame.transform.scale(kopia, (szerokosc + 20, wysokosc + 20))
    pygame.mixer.init()
    laserD = pygame.mixer.Sound("Dzwieki\Laser_09.wav")
    laserD.set_volume(0.1)
    odpornosc = 0
    czas = 0
    jest = True
    rodzaj = 8
    kat = 0
    czasOslony = 0
    czasOdnawianiaOslony = 0
    oslona = False


    def __init__(self):
        self.hp = 220
        self.maxHp = 220
        self.odpornosc = 0
        self.czas = pygame.time.get_ticks()
        self.jest = True
        self.x = randint(SZEROKOSC-200, SZEROKOSC - 100)
        self.y = randint(100, WYSOKOSC-200)
        self.dx = choice([0.8, 0.7, 0.6, -0.8, -0.7, -0.6])
        self.dy = choice([0.8, 0.7, 0.6, -0.8, -0.7, -0.6])
        self.granicaX = SZEROKOSC//2 + 150
        self.granicaY = WYSOKOSC - 50
        self.czasOslony = pygame.time.get_ticks()
        self.oslona = False
        self.czasOdnawianiaOslony = 6000


    def render(self, window, rodzajMisji):
            window.blit(self.grafika, (self.x, self.y))
            if self.oslona:
                window.blit(self.oslonaG, (self.x - 10, self.y - 10))
            pasek(window, self.x, self.y - 2, 4, self.szerokosc, self.maxHp, self.hp, 'black', 'red')

    def update(self, window, ENEMY,LASERY_ENEMY,RAKIETY_ENEMY, rodzajMisji):
        if not self.oslona and pygame.time.get_ticks() - self.czasOslony > self.czasOdnawianiaOslony:
            self.oslona = True
            self.oslonaD.play()

        self.x += self.dx
        self.y += self.dy

        if self.x+self.szerokosc > SZEROKOSC -5 or self.x < self.granicaX:
            self.dx = - self.dx

        if self.y+self.wysokosc > self.granicaY or self.y < 1:
            self.dy = - self.dy

        if pygame.time.get_ticks() - self.czas > randint(3500, 5000):
            self.czas = pygame.time.get_ticks()
            self.laserD.play()
            LASERY_ENEMY.append(Laser(self.x, self.y + self.wysokosc // 2, -5, 0, -90, rodzajMisji,10))

        self.render(window,rodzajMisji)

    def hit(self,ile):
        self.hp -= ile
        if self.hp <= 0:
            self.jest = False

    def getRect(self):
        return pygame.Rect((self.x,self.y,self.szerokosc,self.wysokosc))






