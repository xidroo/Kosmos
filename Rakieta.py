import pygame
from random import randint
from random import choice
SZEROKOSC = 1000
WYSOKOSC = 550

class Rakieta:
    x = 0
    y = 0
    dx= 0
    dy = 0
    jest = True
    granicaX = 0
    granicaY = 0
    grafika = pygame.image.load("Grafika\\rakieta1.png")
    grafika.set_colorkey('white')
    szerokosc = grafika.get_width()
    wysokosc = grafika.get_height()
    kat = 0
    czas = 0
    moc = 100

    def __init__(self,x,y,dx,dy,kat,moc,rodzajMisji):
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


    def render(self, window, rodzajMisji):
        if self.kat != 0:
            kopia = pygame.transform.rotate(self.grafika, self.kat)
            kopia.set_colorkey('white')
            window.blit(kopia, (self.x, self.y))
        else:
            window.blit(self.grafika, (self.x, self.y))

    def getRect(self):
        return pygame.Rect((self.x,self.y,self.szerokosc,self.wysokosc))

    def update(self, window, rodzajMisji):
        self.x += self.dx
        self.y += self.dy

        if self.x > SZEROKOSC or self.x + self.szerokosc < 1:
            self.jest = False

        if self.y > self.granicaY or self.y +self.wysokosc < 1:
            self.jest = False

        if self.y > + self.wysokosc > self.granicaY and self.kat == 180:
            self.jest = False

        self.render(window,rodzajMisji)