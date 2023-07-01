import pygame
from Button import Button
CZARNY = (0,0,0)
CZERWONY = ('red')
FIOLETOWY = (128, 0, 128)
BIALY = ("crimson")


class Technologia:
    numer = 0
    nazwa = ""
    opis = ""
    cenaBadania = 0
    stopien = 0
    cena1 = 0
    cena2 = 0
    nazwaStopien1 = ""
    nazwaStopien2 = ""
    powierzchniaDuza = ""
    powierzchniaMala1 = pygame.Surface((200,50))
    powierzchniaMala2 = pygame.Surface((200,50))
    powierzchniaMala3 = pygame.Surface((200,50))

    fontNaglowek = ""
    fontOpis = ""
    buttonZbadaj = ""





    def __init__(self,numer,stopien = -1):
        self.fontNaglowek = pygame.font.SysFont('comicsansms', 15)
        self.fontNaglowek.set_bold(True)
        self.fontOpis = pygame.font.SysFont('comicsansms', 10)
        self.powierzchniaDuza = pygame.Surface((235, 285))
        self.powierzchniaDuza.fill((115, 106, 255))
        self.numer = numer
        self.stopien = stopien

        if numer == 0:
            self.nazwa = "SILNIK DRONA"
            self.opis = "Wzmocnij silnik, zwiększ szybkość i manewrowość drona"
            self.cenaBadania = 1
            self.cena1 = 800
            self.cena2 = 1500
            self.nazwaStopien1 = "Szybkość dorona + 1"
            self.nazwaStopien2 = "Szybkość dorona + 1"


        if numer == 1:
            self.nazwa = "DODATKOWE LASERY"
            self.opis = "Dodaj dronowi kolejne lasery, ale kosztem  zwiększenia temperatury"
            self.cenaBadania = 4
            self.cena1 = 1500
            self.cena2 = 2500
            self.nazwaStopien1 = "Ilość laserów + 1"
            self.nazwaStopien2 = "Ilość laserów + 1"

        if numer == 2:
            self.nazwa = "WIĘCEJ RAKIET"
            self.opis = "Zwiększ ilość rakiet w jakie uzbrojony jest dron"
            self.cenaBadania = 2
            self.cena1 = 1000
            self.cena2 = 2000
            self.nazwaStpien1 = "Ilość rakiet + 2"
            self.nazwaStopien2 = "Ilość rakiet + 3"

        if numer == 3:
            self.nazwa = "WIĘKSZY MAGAZYN ZŁOMU"
            self.opis = "Zwiększ pojemność magazynu złomu"
            self.cenaBadania = 1
            self.cena1 = 1000
            self.cena2 = 2000
            self.nazwaStopien1 = "Ilość złomu + 10"
            self.nazwaStopien2 = "Ilość złomu + 15"

        if numer == 4:
            self.nazwa = "LEPSZE CHŁODZENIE"
            self.opis = "Zwiększ maksymalną temperaturę laserów"
            self.cenaBadania = 2
            self.cena1 = 1000
            self.cena2 = 2000
            self.nazwaStopien1 = "Max. temperatura + 50"
            self.nazwaStopien2 = "Max. temperatura + 100"

        if numer == 5:
            self.nazwa = "SZYBSZE RAKIETY"
            self.opis = "Zwiększ szybkość rakiet"
            self.cenaBadania = 3
            self.cena1 = 1000
            self.cena2 = 1800
            self.nazwaStopien1 = "Szybkość rakiet +2"
            self.nazwaStopien2 = "Szybkość rakiet +2"

        if numer == 6:
            self.nazwa = "WIĘCEJ HP DRONA"
            self.opis = "Zwiększ HP drona"
            self.cenaBadania = 3
            self.cena1 = 1000
            self.cena2 = 2000
            self.nazwaStopien1 = "HP +50"
            self.nazwaStopien2 = "HP +100"

        if numer == 7:
            self.nazwa = "SZYBSZA OSŁONA"
            self.opis = "Zmniejsz czas odnawiania osłony"
            self.cenaBadania = 2
            self.cena1 = 1000
            self.cena2 = 2000
            self.nazwaStopien1 = "Czas odnawiania osłony -2s"
            self.nazwaStopien2 = "Czas odnawiania osłony -3s"

        if numer == 8:
            self.nazwa = "WIĘKSZY ZASIĘG MAGNESU"
            self.opis = "Zwiększ promień przyciągania magnesu przyciągającego złom"
            self.cenaBadania = 1
            self.cena1 = 800
            self.cena2 = 1500
            self.nazwaStopien1 = "Zasięg zmagnesu +50"
            self.nazwaStopien2 = "Zasięg zmagnesu +50"

        if numer == 9:
            self.nazwa = "WIĘKSZA MOC LASERU"
            self.opis = "Zwiększ obrażenia zadawane przez lasery, ale i generowaną temperaturę"
            self.cenaBadania = 4
            self.cena1 = 1500
            self.cena2 = 3000
            self.nazwaStopien1 = "Moc laseru +5"
            self.nazwaStopien2 = "Moc laseru +5"

        if numer == 10:
            self.nazwa = "ZAWIRUSOWANE RAKIETY"
            self.opis = "Po trafieniu taką rakietą, przeciwnik odporny na lasery, traci odporność"
            self.cenaBadania = 3
            self.cena1 = 1000
            self.cena2 = 1500
            self.nazwaStopien1 = "Wyłączają odporność na laser"
            self.nazwaStopien2 = "Wirus?"

        if numer == 11:
            self.nazwa = "WIĘKSZA CENA ZŁOMU"
            self.opis = "Koszt sprzedaży złomu wzrasta"
            self.cenaBadania = 1
            self.cena1 = 1000
            self.cena2 = 1600
            self.nazwaStopien1 = "Koszt złomu +5$"
            self.nazwaStopien2 = "Koszt złomu +10$"

        if numer == 12:
            self.nazwa = "TAŃSZA NAPRAWA DRONA"
            self.opis = "Koszt naprawy drona maleje"
            self.cenaBadania = 4
            self.cena1 = 1000
            self.cena2 = 1800
            self.nazwaStopien1 = "Koszt naprawy 1HP/2$"
            self.nazwaStopien2 = "Koszt naprawy 1HP/1$"

        if numer == 13:
            self.nazwa = "WIĘKSZA SIŁA RAKIET"
            self.opis = "Rakiety zadają więcej obrażeń"
            self.cenaBadania = 4
            self.cena1 = 1200
            self.cena2 = 2500
            self.nazwaStopien1 = "Moc rakiety + 50"
            self.nazwaStopien2 = "Moc rakiety + 50"

        if numer == 14:
            self.nazwa = "RAKIETY OBSZAROWE"
            self.opis = "Eksplozja rakiety razi okoliczne cele"
            self.cenaBadania = 3
            self.cena1 = 1500
            self.cena2 = 2500
            self.nazwaStopien1 = "Zasięg eksplozji = 50"
            self.nazwaStopien2 = "Zasięg eksplozji = 100"

    def odswiezObraz(self,GRACZ):
        kolor1 = ('lightgreen')
        kolor2 = ('lightsalmon')


        if self.stopien>-1:
            pygame.draw.rect(self.powierzchniaDuza,kolor1,(5,5,230,90),0,10)
        else:
            pygame.draw.rect(self.powierzchniaDuza,kolor2,(5,5,230,90),0,10)

        if self.stopien == -1:
            pygame.draw.rect(self.powierzchniaDuza, kolor2, (5, 100, 230, 90), 0, 10)
            pygame.draw.rect(self.powierzchniaDuza, kolor2, (5, 192, 230, 90), 0, 10)
        elif self.stopien == 1:
            pygame.draw.rect(self.powierzchniaDuza, kolor1, (5, 100, 230, 90), 0, 10)
            pygame.draw.rect(self.powierzchniaDuza, kolor2, (5, 192, 230, 90), 0, 10)
        elif self.stopien == 2:
            pygame.draw.rect(self.powierzchniaDuza, kolor1, (5, 100, 230, 90), 0, 10)
            pygame.draw.rect(self.powierzchniaDuza, kolor1, (5, 192, 230, 90), 0, 10)

        self.powierzchniaDuza.blit(self.fontNaglowek.render(self.nazwa, True, BIALY),(15,5))
        if self.stopien>-1:
            self.powierzchniaDuza.blit(self.fontNaglowek.render("Zbadane!", True, CZARNY),(15,25))
        else:
            if self.cenaBadania <= GRACZ.procki or GRACZ.procki == 0:
                if self.cenaBadania == 1:
                    self.powierzchniaDuza.blit(self.fontNaglowek.render("Koszt: " + str(self.cenaBadania) + " procek", True, CZARNY),(15,25))
                elif self.cenaBadania >= 2 and self.cenaBadania <= 4:
                    self.powierzchniaDuza.blit(self.fontNaglowek.render("Koszt: " + str(self.cenaBadania) + " procki", True, CZARNY),(15,25))
                else:
                    self.powierzchniaDuza.blit(self.fontNaglowek.render("Koszt: " + str(self.cenaBadania) + " procków", True, CZARNY),(15,25))
            else:
                if self.cenaBadania == 1:
                    self.powierzchniaDuza.blit(self.fontNaglowek.render("Koszt: " + str(self.cenaBadania) + " procek", True, CZERWONY), (15, 25))
                elif self.cenaBadania >= 2 and self.cenaBadania <= 4:
                    self.powierzchniaDuza.blit(self.fontNaglowek.render("Koszt: " + str(self.cenaBadania) + " procki", True, CZERWONY), (15, 25))
                else:
                    self.powierzchniaDuza.blit(self.fontNaglowek.render("Koszt: " + str(self.cenaBadania) + " procków", True, CZERWONY),(15, 25))

        self.powierzchniaDuza.blit(self.fontNaglowek.render(self.nazwaStopien1, True, CZARNY), (15, 105))
        if self.stopien >= 1:
            self.powierzchniaDuza.blit(self.fontNaglowek.render("Kupione", True, CZARNY), (15, 125))
        else:
            if self.cena1 <= GRACZ.kasa:
                self.powierzchniaDuza.blit(self.fontNaglowek.render("Cena: " + str(self.cena1) + "$", True, CZARNY),(15, 125))
            else:
                self.powierzchniaDuza.blit(self.fontNaglowek.render("Cena: " + str(self.cena1) + "$", True, CZERWONY),(15, 125))

        self.powierzchniaDuza.blit(self.fontNaglowek.render(self.nazwaStopien2, True, CZARNY), (15, 197))
        if self.stopien == 2:
            self.powierzchniaDuza.blit(self.fontNaglowek.render("Kupione", True, CZARNY), (15, 217))
        else:
            if self.cena2 <= GRACZ.kasa:
                self.powierzchniaDuza.blit(self.fontNaglowek.render("Cena: " + str(self.cena2) + "$", True, CZARNY),(15, 217))
            else:
                self.powierzchniaDuza.blit(self.fontNaglowek.render("Cena: " + str(self.cena2) + "$", True, CZERWONY),(15, 217))


    def pokazObrazek(self):
        return self.powierzchniaDuza


    def zbadaj(self, GRACZ):
        self.stopien = 0
        self.odswiezObraz(GRACZ)
        GRACZ.procki -= self.cenaBadania

    def kup(self, GRACZ):
        self.stopien += 1
        self.odswiezObraz(GRACZ)
        if self.stopien == 1:
            GRACZ.kasa -= self.cena1
        if self.stopien == 2:
            GRACZ.kasa -= self.cena2


        if self.numer == 0 and self.stopien == 1:
            GRACZ.dx += 1
            GRACZ.dy += 1

        if self.numer == 0 and self.stopien == 2:
            GRACZ.dx += 1
            GRACZ.dy += 1


        if self.numer == 2 and self.stopien == 1:
            GRACZ.maxRakiety += 2

        if self.numer == 2 and self.stopien == 2:
            GRACZ.maxRakiety += 3

        if self.numer == 1 and self.stopien == 1:
            GRACZ.iloscLaserow += 1

        if self.numer == 1 and self.stopien == 2:
            GRACZ.iloscLaserow += 1

        if self.numer == 3 and self.stopien == 1:
            GRACZ.maxZlom += 10

        if self.numer == 3 and self.stopien == 2:
            GRACZ.maxZlom += 15


        if self.numer == 4 and self.stopien == 1:
            GRACZ.maxTemperatura += 50

        if self.numer == 4 and self.stopien == 2:
            GRACZ.maxTemperatura += 100

        if self.numer == 5 and self.stopien == 1:
            GRACZ.szybkoscRakiet += 2

        if self.numer == 5 and self.stopien == 2:
            GRACZ.szybkoscRakiet += 2

        if self.numer == 6 and self.stopien == 1:
            GRACZ.maxHP += 50
            GRACZ.hp = GRACZ.maxHP

        if self.numer == 6 and self.stopien == 2:
            GRACZ.maxHP += 100
            GRACZ.hp = GRACZ.maxHP

        if self.numer == 7 and self.stopien == 1:
            GRACZ.czasOdnawianiaOslony -= 2000

        if self.numer == 7 and self.stopien == 2:
            GRACZ.czasOdnawianiaOslony -= 3000

        if self.numer == 8 and self.stopien == 1:
            GRACZ.zasiegMagnesu += 50

        if self.numer == 8 and self.stopien == 2:
            GRACZ.zasiegMagnesu += 50

        if self.numer == 9 and self.stopien == 1:
            GRACZ.mocLaseru += 5

        if self.numer == 9 and self.stopien == 2:
            GRACZ.mocLaseru += 5

        if self.numer == 10 and self.stopien == 1:
            GRACZ.wirus = 1

        if self.numer == 10 and self.stopien == 2:
            GRACZ.wirus = 2

        if self.numer == 11 and self.stopien == 1:
            GRACZ.cenaZlomu += 5

        if self.numer == 11 and self.stopien == 2:
            GRACZ.cenaZlomu += 10

        if self.numer == 12 and self.stopien == 1:
            GRACZ.kosztNaprawy = 2

        if self.numer == 12 and self.stopien == 2:
            GRACZ.kosztNaprawy = 1

        if self.numer == 13 and self.stopien == 1:
            GRACZ.mocRakiet += 50

        if self.numer == 13 and self.stopien == 2:
            GRACZ.mocRakiet += 50

        if self.numer == 14 and self.stopien == 1:
            GRACZ.glowica = 50

        if self.numer == 14 and self.stopien == 2:
            GRACZ.glowica = 100