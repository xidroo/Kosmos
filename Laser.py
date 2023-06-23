import pygame
import math
from random import randint
from random import choice
SZEROKOSC = 1000
WYSOKOSC = 550

class Laser:
    x = 0
    y = 0
    dx = 0
    dy = 0
    jest = True
    granicaX = 0
    granicaY = 0
    grafika = pygame.image.load("Grafika\laser.png")
    grafika1 = pygame.image.load("Grafika\laser1.png")
    grafika2 = pygame.image.load("Grafika\laser2.png")
    grafika.set_colorkey('white')
    grafika1.set_colorkey('white')
    grafika2.set_colorkey('white')
    szerokosc = grafika.get_width()
    wysokosc = grafika.get_height()
    kat = 0
    czas = 0
    moc = 1

    def __init__(self,x,y,dx,dy,kat,rodzajMisji,moc):
            self.x = x
            self.y = y
            self.dx = dx
            self.dy = dy
            self.kat = kat
            self.granicaX = 0
            self.granicaY = WYSOKOSC
            self.odpornosc = 0
            self.czas = pygame.time.get_ticks()
            self.jest = True
            self.moc = moc
            if self.moc == 15:
                self.grafika = self.grafika1
            if self.moc == 20:
                self.grafika = self.grafika2

            '''self.x = Gracz.x + Gracz.grafika.get_width() // 2 - Gracz.grafika.get_width() // 2 * math.sin(kat * math.pi / 180)
            self.y = Gracz.y + Gracz.get_height() // 2 - Gracz.get_height() // 2 * math.cos(kat * math.pi / 180)
            self.dx = 5 * math.sin(self.kat * math.pi / 180)
            self.dy = 5 * math.cos(self.kat * math.pi / 180)'''


    def render(self, window, rodzajMisji):
        if self.kat != 0:
            kopia = pygame.transform.rotate(self.grafika,self.kat)
            kopia.set_colorkey('white')
            window.blit(kopia, (self.x, self.y))
        else:
            window.blit(self.grafika,(self.x,self.y))

    def getRect(self):
        return pygame.Rect((self.x,self.y,self.szerokosc,self.wysokosc))

    def update(self, window, rodzajMisji):
        self.x += self.dx
        self.y += self.dy

        if self.x > SZEROKOSC or self.x + self.szerokosc < 1:
            self.jest = False

        if self.y + self.wysokosc > self.granicaY or self.y + self.wysokosc < 1:
            self.jest = False

        self.render(window,rodzajMisji)