import pygame
from random import randint
from random import choice
SZEROKOSC = 1000
WYSOKOSC = 550

class Wybuch:
    x = 0
    y = 0
    klatka = 0
    jest = True
    czas = 0
    grafikiDuze = []
    grafikiMale = []
    grafikiDuze1 = []
    grafiki = []
    kierunek = 1
    jaki = 0
    sciezka = "Grafika\Wybuchy\expl_09_00"
    for i in range(32):
        if i < 10:
            sciezka = "Grafika\Wybuchy\expl_09_000"
        else:
            sciezka = "Grafika\Wybuchy\expl_09_00"
        sciezka += str(i)
        sciezka += ".png"
        grafikiDuze.append(pygame.image.load(sciezka))

    sciezka = "Grafika\Wybuchy\expl_10_00"
    for i in range(32):
        if i < 10:
            sciezka = "Grafika\Wybuchy\expl_10_000"
        else:
            sciezka = "Grafika\Wybuchy\expl_10_00"
        sciezka += str(i)
        sciezka += ".png"
        grafikiDuze1.append(pygame.image.load(sciezka))

    sciezka = "Grafika\Wybuchy\expl_02_00"
    for i in range(23):
        if i < 10:
            sciezka = "Grafika\Wybuchy\expl_05000"
        else:
            sciezka = "Grafika\Wybuchy\expl_0500"
        sciezka += str(i)
        sciezka += ".png"
        grafikiMale.append(pygame.image.load(sciezka))

        kopie = []
        for g in grafikiMale:
            kopia = pygame.transform.scale(g,(70,70))
            kopia.set_colorkey('white')
            kopie.append(kopia)
        grafikiMale.clear()
        grafikiMale = kopie

    def __init__(self,x,y,jaki):
        self.x = x
        self.y = y
        self.jest = True
        self.klatka = 0
        self.czas = pygame.time.get_ticks()
        self.kierunek = 1
        self.jaki = jaki
        if self.jaki == 1:
            self.grafiki  = self.grafikiDuze
        if self.jaki == 2:
            self.grafiki  = self.grafikiMale
        if self.jaki == 3:
            self.grafiki  = self.grafikiDuze1

    def render(self,window):
            window.blit(self.grafiki[self.klatka],(self.x,self.y))


    def update(self,window):
        if pygame.time.get_ticks() - self.czas > 30:
            self.czas = pygame.time.get_ticks()
            self.klatka += self.kierunek
            if self.klatka >= len(self.grafiki)-1:
                self.kierunek = -1
                self.klatka = 4
            if self.kierunek == -1 and self.klatka == 0:
                self.jest = False

        self.render(window)
