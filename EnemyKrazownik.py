import pygame
from random import randint
from random import choice
from Rakieta import Rakieta
from Laser import Laser
from Pasek import pasek

SZEROKOSC = 1000
WYSOKOSC = 550

class EnemyKrazownik:
    x = 0
    y = 0
    dx = 0
    dy = 0
    hp = 0
    maxHp = 0
    granicaX = 0
    granicaY = 0
    grafika1 = pygame.image.load("Grafika\Enemy\enemy9_1.png")
    grafika2 = pygame.image.load("Grafika\Enemy\enemy9_2.png")
    grafika = pygame.image.load("Grafika\Enemy\enemy9_1.png")
    rakietaD = pygame.mixer.Sound("Dzwieki\sfx_sounds_falling11.wav")
    laserD = pygame.mixer.Sound("Dzwieki\Laser_09.wav")
    laserD.set_volume(0.1)
    grafika.set_colorkey('white')
    grafika1.set_colorkey('white')
    grafika2.set_colorkey('white')
    szerokosc = grafika.get_width()
    wysokosc = grafika.get_height()
    odpornosc = 1
    czas = 0
    czasZmianyKierunku = 0
    czasPomiedzyLaserami = 5000
    seria = False
    czasStrzalu = 0
    jest = True
    rodzaj = 9
    kat = 0
    stop = False
    czasStop = 0
    czasSerii = 0



    def __init__(self, rodzajMisji):
        self.hp = 200
        self.maxHp = 200
        self.odpornosc = 1
        self.czas = pygame.time.get_ticks()
        self.czasZmianyKierunku = pygame.time.get_ticks()
        self.jest = True
        self.stop = False
        self.czasStop = pygame.time.get_ticks()
        self.czasStrzalu = pygame.time.get_ticks()
        self.czasPomiedzyLaserami = 5000
        self.seria = False
        self.czasSerii = pygame.time.get_ticks()
        if rodzajMisji in [1,2]:
            self.x = randint(50,SZEROKOSC - 200)
            self.y = randint(1,100)
            self.dx = choice([-1.1,1.1,1.2,-1.2,1.3,-1.3])
            self.dy = choice([0.3,0.5,0.2,0.4])
            self.granicaX = 0
            self.granicaY = 150
            self.kat = 0
        if rodzajMisji == 3:
            self.x = randint(SZEROKOSC-300,SZEROKOSC - 300)
            self.y = randint(10,WYSOKOSC - 300)
            self.dx = choice([-0.6,-0.4,0.4,0.6])
            self.dy = choice([0.8,0.9,1,1.1,-0.8,-0.9,-1,-1.1])
            self.aktualnaDx = self.dx
            self.aktualnaDy = self.dy
            self.granicaX = SZEROKOSC//2+200
            self.granicaY = WYSOKOSC - 20
            kopia = pygame.transform.rotate(self.grafika1, -90)
            self.grafika1 = kopia
            self.grafika1.set_colorkey('white')
            self.grafika = self.grafika1
            kopia = pygame.transform.rotate(self.grafika2, -90)
            self.grafika2 = kopia
            self.grafika2.set_colorkey('white')
            self.grafika = self.grafika1
            self.szerokosc = self.grafika.get_width()
            self.wysokosc = self.grafika.get_height()
        if rodzajMisji == 4:
            self.x = 0
            self.y = 0
            self.dx = 1
            self.dy = 0.6
            self.aktualnaDx = self.dx
            self.aktualnaDy = self.dy
            self.granicaX = 400
            self.granicaY = WYSOKOSC
            kopia = pygame.transform.rotate(self.grafika1, -90)
            self.grafika1 = kopia
            self.grafika1.set_colorkey('white')
            self.grafika = self.grafika1
            kopia = pygame.transform.rotate(self.grafika2, -90)
            self.grafika2 = kopia
            self.grafika2.set_colorkey('white')
            self.grafika = self.grafika1
            self.szerokosc = self.grafika.get_width()
            self.wysokosc = self.grafika.get_height()


    def render(self, window, rodzajMisji):
            if self.odpornosc == 1:
                window.blit(self.grafika1, (self.x, self.y))
            elif self.odpornosc == 0:
                window.blit(self.grafika2, (self.x, self.y))

            pasek(window, self.x, self.y - 2, 4, self.szerokosc, self.maxHp, self.hp, 'black', 'red')


    def update(self, window, ENEMY,LASERY_ENEMY,RAKIETY_ENEMY, rodzajMisji):

        if not self.stop:
            self.x += self.dx
            self.y += self.dy

        if rodzajMisji in [1,2]:
            if randint(1,1000) <= 15 and pygame.time.get_ticks() - self.czasZmianyKierunku > randint(5000,7000) :
                 self.czasZmianyKierunku = pygame.time.get_ticks()
                 self.dx = - self.dx

        if rodzajMisji == 3:
            if randint(1,1000) <= 15 and pygame.time.get_ticks() - self.czasZmianyKierunku > randint(5000,7000) :
                 self.czasZmianyKierunku = pygame.time.get_ticks()
                 self.dy = - self.dy

        if randint(1,100) < 15 and pygame.time.get_ticks() - self.czas > randint(5000,12000) and not self.stop:
            self.stop = True
            self.czasStop = pygame.time.get_ticks()


        if pygame.time.get_ticks() - self.czasStop > 750 and self.stop:
            self.czas = pygame.time.get_ticks()
            self.stop = False
            self.rakietaD.play()
            if rodzajMisji in [1, 2]:
                RAKIETY_ENEMY.append(Rakieta(self.x+self.szerokosc//2,self.y+self.wysokosc//2+10,0,3,180,rodzajMisji))
            if rodzajMisji in [3, 4]:
                RAKIETY_ENEMY.append(Rakieta(self.x + 20, self.y + self.wysokosc // 2 , -3, 0, 90, rodzajMisji))

        if rodzajMisji in [1, 2]:
            if self.x+self.szerokosc > SZEROKOSC - 10 or self.x < 10:
                self.dx = - self.dx
                self.czasZmianyKierunku = pygame.time.get_ticks()

        if rodzajMisji  == 3:
            if self.x+self.szerokosc > SZEROKOSC - 10 or self.x < 600:
                self.dx = - self.dx
                self.czasZmianyKierunku = pygame.time.get_ticks()

        if rodzajMisji  == 4:
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
            if not self.seria:
                self.czasSerii = pygame.time.get_ticks()
                self.czasPomiedzyLaserami = 200
                self.seria = True
            self.laserD.play()

            if rodzajMisji in [1,2]:
                LASERY_ENEMY.append(Laser(self.x+10,self.y+self.wysokosc,0,5,0,rodzajMisji,10))
                LASERY_ENEMY.append(Laser(self.x+self.szerokosc - 10,self.y+self.wysokosc,0,5,0,rodzajMisji,10))
            if rodzajMisji in [3,4]:
                LASERY_ENEMY.append(Laser(self.x,self.y+10,-5,0,-90,rodzajMisji,10))
                LASERY_ENEMY.append(Laser(self.x,self.y+self.wysokosc-10,-5,0,-90,rodzajMisji,10))

        if self.seria and pygame.time.get_ticks() - self.czasSerii > 600:
            self.seria = False
            self.czasPomiedzyLaserami = 5000


        self.render(window,rodzajMisji)

    def hit(self,ile):
        self.hp -= ile
        if self.hp <= 0:
            self.jest = False

    def getRect(self):
        return pygame.Rect((self.x,self.y,self.szerokosc,self.wysokosc))






