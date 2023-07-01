import pygame
import random
from random import randint
from random import choice
from Laser import Laser
from Pasek import pasek
SZEROKOSC = 1000
WYSOKOSC = 550

class EnemyScigacz:
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
    grafika = pygame.image.load("Grafika\Enemy\enemy4.png")
    pygame.mixer.init()
    laserD = pygame.mixer.Sound("Dzwieki\Laser_09.wav")
    laserD.set_volume(0.1)
    grafika.set_colorkey('white')
    szerokosc = grafika.get_width()
    wysokosc = grafika.get_height()
    odpornosc = 0
    czasStrzalu = 0
    czasSzarzy = 0
    odstepMiedzyLaserami = 0
    szarza = True
    jest = True
    rodzaj = 4



    def __init__(self, rodzajMisji,x=0,y=0):
        self.hp = 120
        self.maxHp = 120
        self.odpornosc = 0
        self.czasStrzalu = pygame.time.get_ticks()
        self.czasSzarzy = pygame.time.get_ticks()
        self.jest = True
        self.szarza = False
        self.odstepMiedzyLaserami = 3000
        if rodzajMisji in [1,2]:
            self.x = randint(100,SZEROKOSC - 100)
            self.y = randint(20,50)
            if x != 0:
                self.x = x
                self.y = y
            if rodzajMisji == 2:
                if random.choice((1,2)) == 1:
                    self.x = 388
                    self.y = 90
                else:
                    self.x = 588
                    self.y = 90
            if x != 0:
                self.x = x
                self.y = y
            self.dx = choice([-1.9,-1.8,-1.6,-1.7,-2,2,1.6,1.8,1.7,1.9])
            self.dy = choice([0.9,0.8,0.7,0.6,0.5])
            self.aktualnaDx = self.dx
            self.aktualnaDy = self.dy
            self.granicaX = 0
            self.granicaY = 300
        if rodzajMisji ==3:
            self.x = randint(SZEROKOSC - 300,SZEROKOSC - 200)
            self.y = randint(100,WYSOKOSC - 100)
            if x != 0:
                self.x = x
                self.y = y
            self.dx = 1.7
            self.dy = 0.8
            self.aktualnaDx = self.dx
            self.aktualnaDy = self.dy
            self.granicaX = 400
            self.granicaY = WYSOKOSC-10
            kopia = pygame.transform.rotate(self.grafika, -90)
            self.grafika = kopia
            self.grafika.set_colorkey('white')
            self.szerokosc = self.grafika.get_width()
            self.wysokosc = self.grafika.get_height()
        if rodzajMisji == 4:
            self.x = 0
            self.y = 0
            self.dx = 1.8
            self.dy = 0.8
            self.aktualnaDx = self.dx
            self.aktualnaDy = self.dy
            self.granicaX = 400
            self.granicaY = WYSOKOSC
            kopia = pygame.transform.rotate(self.grafika, -90)
            self.grafika = kopia
            self.grafika.set_colorkey('white')
            self.szerokosc = self.grafika.get_width()
            self.wysokosc = self.grafika.get_height()
            if x != 0:
                self.x = x
                self.y = y


    def render(self, window, rodzajMisji):
        window.blit(self.grafika,(self.x,self.y))
        pasek(window, self.x, self.y - 2, 4, self.szerokosc, self.maxHp, self.hp, 'black', 'red')

    def update(self, window, ENEMY,LASERY_ENEMY,RAKIETY_ENEMY, rodzajMisji):
        self.x += self.aktualnaDx
        self.y += self.aktualnaDy

        if rodzajMisji in [1,2]:
            if self.x + self.szerokosc > SZEROKOSC or self.x < 1:
                self.aktualnaDx = - self.aktualnaDx

            if self.y + self.wysokosc > self.granicaY:
                self.aktualnaDy = -self.aktualnaDy

            if self.y < 10 and self.szarza:
                self.aktualnaDy = choice([0.9,0.8,0.7,0.6,0.5])
                self.aktualnaDx = choice([-1.9,-1.8,-1.6,-1.7,-2,2,1.6,1.8,1.7,1.9])
                self.szarza = False
                self.odstepMiedzyLaserami = 3000

            if self.y < 1:
                self.aktualnaDy = - self.aktualnaDy

            if not self.szarza and self.y+self.wysokosc > self.granicaY-10 and pygame.time.get_ticks() - self.czasSzarzy > 5000:
                self.czasSzarzy = pygame.time.get_ticks()
                self.szarza = True
                self.aktualnaDy = 4
                self.aktualnaDx = 0
                self.odstepMiedzyLaserami = 100

        if rodzajMisji in [3,4]:

            if self.x + self.szerokosc > SZEROKOSC-5 or self.x < 200 :
                self.aktualnaDx = - self.aktualnaDx

            if self.y + self.wysokosc > self.granicaY-10 or self.y <10:
                self.aktualnaDy = -self.aktualnaDy

            if not self.szarza and self.x < self.granicaX and pygame.time.get_ticks() - self.czasSzarzy > 5000:
                self.czasSzarzy = pygame.time.get_ticks()
                self.szarza = True
                self.aktualnaDx = 4
                self.aktualnaDy = 0
                self.odstepMiedzyLaserami = 100

            if self.szarza and self.x+self.szerokosc > SZEROKOSC-150 :
                self.aktualnaDx = choice([-1.8, -1.6, -1.7, 1.6, 1.8, 1.7, 1.5, -1.5])
                self.aktualnaDy = choice([0.9, 0.8, 1, 1.1, 1.2, 1.3, -0.9, -0.8, -1, -1.1, -1.2, -1.3])
                self.szarza = False
                self.odstepMiedzyLaserami = 3000


            if self.x+self.szerokosc < 10:
                self.aktualnaDx = - self.aktualnaDx




        if pygame.time.get_ticks() - self.czasStrzalu > self.odstepMiedzyLaserami:
            self.czasStrzalu = pygame.time.get_ticks()
            self.laserD.play()
            if rodzajMisji in [1, 2]:
                LASERY_ENEMY.append(Laser(self.x + self.szerokosc // 2, self.y + self.wysokosc, 0, 5, 0, rodzajMisji,10))
            if rodzajMisji in [3, 4]:
                LASERY_ENEMY.append(Laser(self.x, self.y + self.wysokosc//2, -5, 0, -90, rodzajMisji,10))

        self.render(window, rodzajMisji)

    def hit(self,ile):
        self.hp -= ile
        if self.hp <= 0:
            self.jest = False

    def getRect(self):
        return pygame.Rect((self.x,self.y,self.szerokosc,self.wysokosc))






