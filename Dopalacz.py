import pygame
import Gracz
from Pasek import pasek
class Dopalacz:
    name = "nazwa"
    opis = "opis"
    grafika = "grafika"
    grafikaAktywna = "grafika"
    czasDzialania = 0
    czasOdnawiania = 0
    czas = pygame.time.get_ticks()
    czyDziala = False
    czyOdnawiaSie = False
    gdzieJest = 0 # 0 - sklep, 1,2,3 - u gracza w slocie, 5 - u gracza w magazynie

    def __init__(self,nr):
        self.nr = nr
        self.gdzieJest = 0
        self.font = pygame.font.SysFont('comicsansms', 20)
        if nr == 0:
            self.grafika = pygame.image.load("Grafika\Info_BTN.png")
            self.grafikaAktywna = pygame.image.load("Grafika\dopalaczAktywny.png")
            self.czasDzialania = 5000
            self.czasOdnawiania = 10000

        self.grafika.set_colorkey('white')
        self.grafikaAktywna.set_colorkey('white')


    def dzialanie(self, GRACZ):
        pass

    def render(self,window, myszPozycja, klawiatura):
        if self.gdzieJest == 1:
            window.blit(self.grafika, (300, 590))
            if self.czyOdnawiaSie:
                pasek(window, 355, 590, 25, 100, self.czasOdnawiania, max(0,pygame.time.get_ticks() - self.czas) , (255, 255, 255),'grey')
                window.blit(self.font.render(str(self.czasOdnawiania//1000) + "/" + str(round((pygame.time.get_ticks() - self.czas)//1000,1)), True, (0,0,0)),(360, 585))
                if pygame.time.get_ticks() - self.czas >= self.czasOdnawiania:
                    self.czyOdnawiaSie = False
            if self.czyDziala:
                pasek(window, 355, 590, 25, 100, self.czasDzialania, pygame.time.get_ticks() - self.czas , (255, 255, 255),'mediumseagreen')
                window.blit(self.font.render(str(self.czasDzialania//1000) + "/" + str(round((pygame.time.get_ticks() - self.czas)//1000,1)), True, (0,0,0)),(360, 585))
                if pygame.time.get_ticks() - self.czas >= self.czasDzialania:
                    self.czyDziala = False
                    self.czyOdnawiaSie = True
                    self.czas = pygame.time.get_ticks()
            #else:
                #pasek(window, 355, 590, 25, 100, self.czasDzialania, self.czasDzialania, (255, 255, 255),'mediumseagreen')
            if klawiatura[pygame.K_1] and not self.czyDziala:
                self.czyDziala = True
                self.czas = pygame.time.get_ticks()
            if self.getRect().collidepoint(myszPozycja):
                pygame.draw.rect(window, 'red',(299, 589,51, 51), 2,5)
        if self.gdzieJest == 2:
            window.blit(self.grafika, (480, 590))
            pasek(window, 535, 590, 25, 100, self.czasDzialania, self.czasDzialania, (255, 255, 255), 'mediumseagreen')
            if self.getRect().collidepoint(myszPozycja):
                pygame.draw.rect(window, 'red',(479, 589,51, 51), 2,5)
        if self.gdzieJest == 3:
            window.blit(self.grafika, (660, 590))
            pasek(window, 715, 590, 25, 100, self.czasDzialania, self.czasDzialania, (255, 255, 255), 'mediumseagreen')
            if self.getRect().collidepoint(myszPozycja):
                pygame.draw.rect(window, 'red',(659, 589,51, 51), 2,5)




    def wkladanieDoSlotu(self,numerSlotu):
        self.gdzieJest = numerSlotu


    def getRect(self):
        if self.gdzieJest == 1:
            return pygame.Rect((300,590,50,50))
        if self.gdzieJest == 2:
            return pygame.Rect((480,590,50,50))
        if self.gdzieJest == 3:
            return pygame.Rect((660,590,50,50))





