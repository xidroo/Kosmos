import pygame
import Gracz
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
        if nr == 0:
            self.grafika = pygame.image.load("Grafika\Info_BTN.png")
            self.grafikaAktywna = pygame.image.load("Grafika\dopalaczAktywny.png")

        self.grafika.set_colorkey('white')
        self.grafikaAktywna.set_colorkey('white')


    def dzialanie(self, GRACZ):
        pass

    def render(self,window, myszPozycja):
        if self.gdzieJest == 0:
            window.blit(self.grafika, (300, 590))
            if self.getRect().collidepoint(myszPozycja):
                #window.blit(self.grafikaAktywna, (300,590))
                pygame.draw.rect(window, 'red',(299, 589,51, 51), 2,5)





    def getRect(self):
        return pygame.Rect((300,590,50,50))





