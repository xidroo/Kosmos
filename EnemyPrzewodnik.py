import pygame
from random import randint
from random import choice
from Laser import Laser
from Pasek import pasek
SZEROKOSC = 1000
WYSOKOSC = 550

class EnemyPrzewodnik:
    x = 0
    y = 0
    dx = 0
    dy = 0
    hp = 0
    maxHp = 0
    granicaX = 0
    granicaY = 0
    grafika = pygame.image.load("Grafika\Enemy\enemy10.png")
    oslonaD = pygame.mixer.Sound("Dzwieki\sfx_sounds_interaction20.wav")
    grafika.set_colorkey('white')
    szerokosc = grafika.get_width()
    wysokosc = grafika.get_height()
    kopia = pygame.image.load("Grafika\spr_shield.png")
    oslonaG = pygame.transform.scale(kopia, (szerokosc + 25, wysokosc + 25))
    pygame.mixer.init()
    laserD = pygame.mixer.Sound("Dzwieki\Laser_09.wav")
    laserD.set_volume(0.1)
    odpornosc = 0
    czas = 0
    jest = True
    rodzaj = 10
    kat = 0
    czasOslony = 0
    czasOdnawianiaOslony = 0
    oslona = False


    def __init__(self):
        self.hp = 175
        self.maxHp = 175
        self.odpornosc = 0
        self.czas = pygame.time.get_ticks()
        self.jest = True
        self.x = randint(800,850)
        self.y = randint(240,260)
        self.dx = choice([1.8, 1.7, 1.6, -1.8, -1.7, -1.6])
        self.dy = choice([1.8, 1.7, 1.6, -1.8, -1.7, -1.6])
        self.granicaX = 980
        self.granicaY = WYSOKOSC - 50
        self.czasOslony = pygame.time.get_ticks()
        self.oslona = False
        self.czasOdnawianiaOslony = 3000


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
            LASERY_ENEMY.append(Laser(self.x, self.y + self.wysokosc // 2, -5, 0, -90, rodzajMisji,15))
            if randint(1,100) < 50:
                self.dy = - self.dy

        self.render(window,rodzajMisji)

    def hit(self,ile):
        self.hp -= ile
        if self.hp <= 0:
            self.jest = False

    def getRect(self):
        return pygame.Rect((self.x,self.y,self.szerokosc,self.wysokosc))






