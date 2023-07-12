import pygame
from Button import Button

BIALY = (255,255,255)

class Gwiazda:
    grafika1 = pygame.image.load("Grafika\gwiazda3m.png")
    grafika2 = pygame.image.load("Grafika\gwiazda4m.png")
    grafika3 = pygame.image.load("Grafika\Star_01.png")
    grafika4 = pygame.image.load("Grafika\Star_03.png")
    def __init__(self,numer,zaliczone = 0):
        self.grafika1.set_colorkey(BIALY)
        self.grafika2.set_colorkey(BIALY)
        self.grafika3.set_colorkey(BIALY)
        self.grafika4.set_colorkey(BIALY)
        self.fontMala = pygame.font.SysFont('comicsansms', 20)
        self.zaliczone = zaliczone
        self.numer = numer
        self.kat = 0
        self.czas = pygame.time.get_ticks()
        if numer == 1:
            self.opis = "ŁOWCA ZWYKLAKÓW: Zniszcz 10 zwyklaków"
        if numer == 2:
            self.opis = "ŁOWCA MYŚLIWCÓW: Zniszcz 10 myśliwców"
        if numer == 3:
            self.opis = "ŁOWCA KANONIEREK: Zniszcz 10 kanonierek"
        if numer == 4:
            self.opis = "ŁOWCA ŚCIGACZY: Zniszcz 10 ścigaczy"
        if numer == 5:
            self.opis = "ŁOWCA KRĄŻOWNIKÓW: Zniszcz 10 krążowników"
        if numer == 6:
            self.opis = "ŁOWCA PANCERNIKÓW: Zniszcz 10 pancerników"
        if numer == 7:
            self.opis = "ŁOWCA BOMBOWCÓW: Zniszcz 10 bombowców"
        if numer == 8:
            self.opis = "ŁOWCA CARGO: Zniszcz 10 cargo"
        if numer == 9:
            self.opis = "ŁOWCA PRZEWODNIKÓW: Zniszcz 10 przewodników"
        if numer == 10:
            self.opis = "ŁOWCA WIEŻ: Zniszcz 10 wież"
        if numer == 11:
            self.opis = "ŁOWCA HORDÓW: Zniszcz 50 dowolnych przeciwników"
        if numer == 12:
            self.opis = "NISZCZYCIEL ZWYKLAKÓW: Zniszcz 50 zwyklaków"
        if numer == 13:
            self.opis = "NISZCZYCIEL MYŚLIWCÓW: Zniszcz 50 myśliwców"
        if numer == 14:
            self.opis = "NISZCZYCIEL KANONIEREK: Zniszcz 50 kanonierek"
        if numer == 15:
            self.opis = "NISZCZYCIEL ŚCIGACZY: Zniszcz 50 ścigaczy"
        if numer == 16:
            self.opis = "NISZCZYCIEL KRĄŻOWNIKÓW: Zniszcz 50 krążowników"
        if numer == 17:
            self.opis = "NISZCZYCIEL PANCERNIKÓW: Zniszcz 50 pancerników"
        if numer == 18:
            self.opis = "NISZCZYCIEL BOMBOWCÓW: Zniszcz 50 bombowców"
        if numer == 19:
            self.opis = "NISZCZYCIEL CARGO: Zniszcz 50 cargo"
        if numer == 20:
            self.opis = "NISZCZYCIEL PRZEWODNIKÓW: Zniszcz 50 przewodników"
        if numer == 21:
            self.opis = "NISZCZYCIEL WIEŻ: Zniszcz 50 wież"
        if numer == 22:
            self.opis = "NISZCZYCIEL HORDÓW: Zniszcz 500 dowolnych przeciwników"
        if numer == 23:
            self.opis = "KOLEKCJONER PROCKÓW: Złap 10 procków"
        if numer == 24:
            self.opis = "MISTRZ PROCKÓW: Złap 50 procków"
        if numer == 25:
            self.opis = "KUPA SIANA: Zgarnij w sumie 10000$"
        if numer == 26:
            self.opis = "GRUBA KUPA SIANA: Zgarnij w sumie 75000$"
        if numer == 27:
            self.opis = "KUPKA SIANKA: Zgarnij w trakcie 1 misji ponad 1000$"
        if numer == 28:
            self.opis = "SOKOLE OKO: Uzyskaj procen trafień w misji powyżej 75%"
        if numer == 29:
            self.opis = "SNAJPER: Uzyskaj procen trafień w misji powyżej 90%"
        if numer == 30:
            self.opis = "OBRONA PLANETY - POCZĄTEK: wykonaj 5 misji Obrona Planety"
        if numer == 31:
            self.opis = "POŚCIG - POCZĄTEK: wykonaj 5 misji Pościg"
        if numer == 32:
            self.opis = "SZWADRON - POCZĄTEK: wykonaj 5 misji Szwadron"
        if numer == 33:
            self.opis = "FABRYKATOR - POCZĄTEK: wykonaj 5 misji Fabrykator"
        if numer == 34:
            self.opis = "OBRONA PLANETY - EKSPERT: wykonaj 15 misji Obrona Planety"
        if numer == 35:
            self.opis = "POŚCIG - EKSPERT: wykonaj 15 misji Pościg"
        if numer == 36:
            self.opis = "SZWADRON - EKSPERT: wykonaj 15 misji Szwadron"
        if numer == 37:
            self.opis = "FABRYKATOR - EKSPERT: wykonaj 15 misji Fabrykator"

        if numer > 37:
            self.opis = "NIE OKRESLONO"

    def zalicz(self):
        if self.zaliczone == 0:
            self.zaliczone = 1

    def sprawdzZaliczenie(self, GRACZ):
        if self.numer == 1 and GRACZ.zniszczone[1] > 9:
            self.zaliczone = 1
        if self.numer == 2 and GRACZ.zniszczone[2] > 9:
            self.zaliczone = 1
        if self.numer == 3 and GRACZ.zniszczone[3] > 9:
            self.zaliczone = 1
        if self.numer == 4 and GRACZ.zniszczone[4] > 9:
            self.zaliczone = 1
        if self.numer == 5 and GRACZ.zniszczone[9] > 9:
            self.zaliczone = 1
        if self.numer == 6 and GRACZ.zniszczone[13] > 9:
            self.zaliczone = 1
        if self.numer == 7 and GRACZ.zniszczone[6] > 9:
            self.zaliczone = 1
        if self.numer == 8 and GRACZ.zniszczone[8] > 9:
            self.zaliczone = 1
        if self.numer == 9 and GRACZ.zniszczone[10] > 9:
            self.zaliczone = 1
        if self.numer == 10 and GRACZ.zniszczone[11] > 9:
            self.zaliczone = 1
        if self.numer == 11 and sum(GRACZ.zniszczone) > 50:
            self.zaliczone = 1
        if self.numer == 12 and GRACZ.zniszczone[1] > 49:
            self.zaliczone = 1
        if self.numer == 13 and GRACZ.zniszczone[2] > 49:
            self.zaliczone = 1
        if self.numer == 14 and GRACZ.zniszczone[3] > 49:
            self.zaliczone = 1
        if self.numer == 15 and GRACZ.zniszczone[4] > 49:
            self.zaliczone = 1
        if self.numer == 16 and GRACZ.zniszczone[9] > 49:
            self.zaliczone = 1
        if self.numer == 17 and GRACZ.zniszczone[13] > 49:
            self.zaliczone = 1
        if self.numer == 18 and GRACZ.zniszczone[6] > 49:
            self.zaliczone = 1
        if self.numer == 19 and GRACZ.zniszczone[8] > 49:
            self.zaliczone = 1
        if self.numer == 20 and GRACZ.zniszczone[10] > 49:
            self.zaliczone = 1
        if self.numer == 21 and GRACZ.zniszczone[11] > 49:
            self.zaliczone = 1
        if self.numer == 22 and sum(GRACZ.zniszczone) > 499:
            self.zaliczone = 1
        if self.numer == 23 and GRACZ.prockiAll > 9:
            self.zaliczone = 1
        if self.numer == 24 and GRACZ.prockiAll > 49:
            self.zaliczone = 1
        if self.numer == 25 and GRACZ.kasaAll > 4999:
            self.zaliczone = 1
        if self.numer == 26 and GRACZ.kasaAll > 74999:
            self.zaliczone = 1

    def wyprintur(self):
        print(self.opis, " ", self.zaliczone)

    def render(self,window,x,y,pozycjaMyszy,animus = False):
        if pygame.Rect((x,y,self.grafika1.get_width(),self.grafika1.get_height())).collidepoint(pozycjaMyszy):
            window.blit(self.fontMala.render(self.opis, True, BIALY), (40, 460))
            if self.zaliczone == 0:
                window.blit(self.grafika1, (x, y-6))
            else:
                window.blit(self.grafika2, (x, y-6))
        else:
            if self.zaliczone == 0:
                window.blit(self.grafika1, (x, y))
            else:
                if animus:
                    if pygame.time.get_ticks() - self.czas > 10:
                        self.czas = pygame.time.get_ticks()
                        self.kat += 2
                        if self.kat > 360: self.kat = 0
                        kopia = pygame.transform.rotate(self.grafika2,self.kat)
                        kopia.set_colorkey(BIALY)
                        nx = (x + (self.grafika2.get_width() - kopia.get_width()) / 2)
                        ny = (y + ((self.grafika2.get_height() - kopia.get_height()) / 2))
                        window.blit(kopia, (nx, ny))
                else:
                    window.blit(self.grafika2, (x, y))



