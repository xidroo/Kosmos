import pygame
from random import randint
from random import choice
SZEROKOSC = 1000
WYSOKOSC = 550

class Zlom:
    x = 0
    y = 0
    dx= 0
    dy = 0
    jest = True
    grafiki = []
    for i in range(9):
        sciezka = "Grafika\Zlom\zlom"
        sciezka += str(i)
        sciezka += ".png"
        grafiki.append(pygame.image.load(sciezka))
    for grafika in grafiki:
        grafika.set_colorkey('white')
    grafika = grafiki[0]
    szerokosc = 0
    wysokosc = 0
    kat = 0
    dKat = 45
    czas = 0

    def __init__(self,x,y):
            self.x = x
            self.y = y
            self.dx = choice([1.8,1.7,1.6,1.5,1.4,1.3,1.2,1.1,1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0,-1.8,-1.7,-1.6,-1.5,-1.4,-1.3,-1.2,-1.1,-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1])
            self.dy = choice([1.5,1,0,-2,-1.9,-1.8,-1.7,-1.6,-1.5,-1.4,-1.3,-1.2,-1.1,-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1])
            self.kat = 0
            self.dKat = 90
            self.granicaX = SZEROKOSC
            self.granicaY = WYSOKOSC
            self.czas = pygame.time.get_ticks()
            self.grafika = choice(self.grafiki)
            self.szerokosc = self.grafika.get_width()
            self.wysokosc = self.grafika.get_height()
            self.jest = True

    def getRect(self):
        return pygame.Rect((self.x,self.y,self.szerokosc,self.wysokosc))

    def render(self, window):
        kopia = pygame.transform.rotate(self.grafika,self.kat)
        kopia.set_colorkey('white')
        window.blit(kopia,(self.x,self.y))

    def update(self, window):
        self.x += self.dx
        self.y += self.dy


        if self.y + self.wysokosc > WYSOKOSC:
            self.jest = False

        if pygame.time.get_ticks() - self.czas > 100:
            self.czas = pygame.time.get_ticks()
            if self.dx > 0:
                self.dx -= 0.1
            else:
                self.dx += 0.1

            self.dy += 0.1
            self.kat += self.dKat

            if self.dKat > 10:
                self.dKat -= 5

            if self.kat > 360:
                self.kat = 0


        self.render(window)
