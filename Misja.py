import  pygame
import  random
from Enemy import Enemy
from EnemyMysliwiec import EnemyMysliwiec
from Meteor import Meteor
from EnemyKanonierka import EnemyKanonierka
from EnemyScigacz import EnemyScigacz
from EnemyCargo import EnemyCargo
from EnemyKrazownik import EnemyKrazownik
from EnemyBabowiec import EnemyBabowiec
from EnemyPrzewodnik import EnemyPrzewodnik
from EnemyWieza import EnemyWieza
from EnemyPancernik import EnemyPancernik
from Beczka import Beczka
CZARNY = (0,0,0)
BIALY = (255,255,255)
CZERWONY = (255,0,0)
SZARY = (122,122,122)
class Misja:
    rodzaj = 1
    poziom = 1
    przeciwnicy = []
    naroda = 0
    rodzajTekst = ""
    font = 0
    font1 = 0
    powierzchnia = pygame.Surface((200,300))
    powierzchnia.fill(BIALY)
    kolor = SZARY
    hpPlanety = 0 #tylko obrona planety
    aktualnehpPlanety = 0 #tylko obrona planety
    trwaPoscig = True #tylko poscig
    dystansPoscigu = 50 + poziom*25 #tylko poscig
    aktualnyStanPoscigu = 0 #tylko poscig
    czasDoUcieczki = 0 #tylko szwadron
    aktualnyCzasDoUcieczki = 0 #tylko szwadron
    czasUcieczki = 0
    iloscWiez = 0#tylko fabrykator
    beczki = [1,1]#tylko fabrykator
    grafiki = []
    grafiki.append(pygame.image.load("Grafika\Misje\misja1.png"))
    grafiki.append(pygame.image.load("Grafika\Misje\misja2.png"))
    grafiki.append(pygame.image.load("Grafika\Misje\misja3.png"))
    grafiki.append(pygame.image.load("Grafika\Misje\misja4.png"))
    grafika = grafiki[0]


    def __init__(self, rodzajMisji, poziom):
        self.rodzaj = rodzajMisji
        self.poziom = poziom
        self.przeciwnicy = []
        self.naroda = 150 + poziom * 150 + random.choice((0,25,25,25,25,50,50,50,100))
        self.font = pygame.font.SysFont('arial', 30)
        self.font.set_bold(True)
        self.font1 = pygame.font.SysFont('arial', 20)
        self.hpPlanety = 1000
        self.aktualnehpPlanety = 1000
        self.grafika = self.grafiki[self.rodzaj-1]



        if rodzajMisji == 1:
            self.rodzajTekst = "Obrona planety"
            self.kolor = (115,106,255)
        if rodzajMisji == 2:
            self.rodzajTekst = "Fabrykator"
            self.kolor = (115,106,255)
            self.beczki = [1, 1]
        if rodzajMisji == 3:
            self.rodzajTekst = "Pościg"
            self.kolor = (115,106,255)
            self.dystansPoscigu = 15 + poziom * 15
        if rodzajMisji == 4:
            self.rodzajTekst = "Szwadron"
            self.kolor = (115,106,255)
            self.czasDoUcieczki = 2000 * 60 - min(1000,(poziom-1)*500)
            self.aktualnyCzasDoUcieczki = self.czasDoUcieczki


    def inicjujWrogow(self,TRUDNOSC):
        self.przeciwnicy.clear()


        zwyklaki = min(3+TRUDNOSC,2+self.poziom)
        mysliwce = min(2+TRUDNOSC,self.poziom+1)
        kanonierki = min(2+TRUDNOSC,self.poziom-1)
        scigacze = min(1+TRUDNOSC,self.poziom-2)
        babowce = min(1+TRUDNOSC,self.poziom)
        kargo = min(1+TRUDNOSC,self.poziom)
        krazownik = min(1+TRUDNOSC,self.poziom-3)
        pancerniki = min(1+TRUDNOSC,self.poziom-4)
        if self.rodzaj == 4:
            self.przeciwnicy.append(EnemyPrzewodnik())
        if self.rodzaj == 1:  # babowiecd
            for i in range((babowce)):
                self.przeciwnicy.append(EnemyBabowiec(self.rodzaj))
        if self.rodzaj == 3:  # cargo
            for i in range((kargo)):
                self.przeciwnicy.append(EnemyCargo())

        if self.rodzaj == 2: #atak na fabrykator
           zwyklaki -= 2
           mysliwce -= 1
           kanonierki -= 1


           self.przeciwnicy.append(Beczka( 300, 5))
           self.przeciwnicy.append(Beczka( 695, 5))
           if self.poziom in (1,2):
               self.przeciwnicy.append(EnemyWieza(self.rodzaj, 498, 65))
               self.iloscWiez = 1
           if self.poziom in (3,4):
               self.przeciwnicy.append(EnemyWieza(self.rodzaj, 358, 10))
               self.przeciwnicy.append(EnemyWieza(self.rodzaj, 638, 10))
               self.iloscWiez = 2
           if self.poziom > 4:
               self.przeciwnicy.append(EnemyWieza(self.rodzaj, 498, 65))
               self.przeciwnicy.append(EnemyWieza(self.rodzaj, 358, 10))
               self.przeciwnicy.append(EnemyWieza(self.rodzaj, 638, 10))
               self.iloscWiez = 3



        for i in range(zwyklaki):
            self.przeciwnicy.append(Enemy(self.rodzaj))
        for i in range(mysliwce):
            self.przeciwnicy.append(EnemyMysliwiec(self.rodzaj))
        for i in range(kanonierki):
            self.przeciwnicy.append(EnemyKanonierka(self.rodzaj))
        for i in range(scigacze):
            self.przeciwnicy.append(EnemyScigacz(self.rodzaj))
        for i in range(krazownik):
            self.przeciwnicy.append(EnemyKrazownik(self.rodzaj))
        for i in range(pancerniki):
            self.przeciwnicy.append(EnemyPancernik(self.rodzaj))

        if self.rodzaj == 4:
            x = 850
            y1 = 100
            y2 = 150
            y3 = 200
            y4 = 300
            y9 = 250
            y10 = 200
            i1 = i2 = i3 = i4 = i9 = i10 =  0

            for enemy in self.przeciwnicy:
                if enemy.rodzaj == 1:
                    enemy.x = x
                    enemy.y = y1 + i1 * 100
                    i1 += 1
                if enemy.rodzaj == 2:
                    enemy.x = x - 100
                    enemy.y = y2 + i2 * 100
                    i2 += 1
                if enemy.rodzaj == 3:
                    enemy.x = x - 200
                    enemy.y = y3 + i3 * 100
                    i3 += 1
                if enemy.rodzaj == 4:
                    enemy.x = x - 300
                    enemy.y = y4 + i4 * 100
                    i4 += 1
                if enemy.rodzaj == 9:
                    enemy.x = x - 350
                    enemy.y = y9 + i9 * 100
                    i9 += 1
                if enemy.rodzaj == 13:
                    enemy.x = x - 400
                    enemy.y = y10 + i10 * 200
                    i10 += 1




        if self.rodzaj == 3:#meteory
            for i in range(min(1 + self.poziom,4)):
                self.przeciwnicy.append(Meteor(self.rodzaj))

        self.czasUcieczki = pygame.time.get_ticks()
        return self.przeciwnicy

    def wyswietlInfo(self):
        self.powierzchnia.fill(self.kolor)
        self.powierzchnia.blit(self.font.render(self.rodzajTekst, True, 'black'),(10,10))
        self.powierzchnia.blit(self.font1.render("Poziom: " + str(self.poziom), True, 'black'),(10,50))
        self.powierzchnia.blit(self.font1.render("Nagroda: " + str(self.naroda) + "$", True, 'black'),(10,70))
        self.powierzchnia.blit(self.grafika,(15,110))

        return self.powierzchnia

