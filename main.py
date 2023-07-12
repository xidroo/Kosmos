import math
import random
import sqlite3

import pygame
from Enemy import Enemy
from Misja import Misja
from Technologia import Technologia
from EnemyMysliwiec import EnemyMysliwiec
from EnemyKanonierka import EnemyKanonierka
from EnemyScigacz import EnemyScigacz
from EnemyPancernik import EnemyPancernik
from Gracz import Gracz
from Button import Button
from Wybuch import Wybuch
from Zlom import Zlom
from Pasek import pasek
from Rakieta import Rakieta
from Procek import Procek
from Laser import Laser
from Dopalacz import Dopalacz

pygame.init()
dopalacz1 = Dopalacz(0)
grafikaEnemy = pygame.image.load("Grafika\Enemy\enemy1.png")
grafikaFabryka = pygame.image.load("Grafika\Enemy\\fabryka.png")
grafikaFabrykaLewa = pygame.image.load("Grafika\Enemy\\fabryka_lewa.png")
grafikaFabrykaPrawa = pygame.image.load("Grafika\Enemy\\fabryka_prawa.png")
grafikaScreen = pygame.image.load("Grafika\screen.png")
grafikaEnemyMysliwiec = pygame.image.load("Grafika\Enemy\enemy2.png")
grafikaEnemyKanonierka = pygame.image.load("Grafika\Enemy\enemy3.png")
grafikaEnemyScigacz = pygame.image.load("Grafika\Enemy\enemy4.png")
grafikaEnemyBabowiec = pygame.image.load("Grafika\Enemy\enemy6.png")
grafikaEnemyCargo = pygame.image.load("Grafika\Enemy\enemy8.png")
grafikaEnemyKrazownik = pygame.image.load("Grafika\Enemy\enemy9_1.png")
grafikaEnemyPrzewodnik = pygame.image.load("Grafika\Enemy\enemy10.png")
grafikaEnemyPancernik = pygame.image.load("Grafika\Enemy\enemy13_1.png")
grafikaEnemyWieza = pygame.image.load("Grafika\Enemy\wieza.png")
grafikaEnemyBeczka = pygame.image.load("Grafika\Enemy\\beczkaL.png")
grafikaEnemyHybryda = pygame.image.load("Grafika\Enemy\\enemy14.png")
grafikaEnemyWsparcie = pygame.image.load("Grafika\Enemy\\enemy15.png")
grafikaGwiazda1 = pygame.image.load("Grafika\gwiazda1m.png")
grafikaGwiazda2 = pygame.image.load("Grafika\gwiazda2m.png")
grafikaGwiazda3 = pygame.image.load("Grafika\gwiazda3m.png")
grafikaGwiazda4 = pygame.image.load("Grafika\gwiazda4m.png")
grafikaZnak = pygame.image.load("Grafika\znak.png")
kopia = pygame.transform.rotate(grafikaEnemyPrzewodnik,90)
grafikaEnemyPrzewodnik = kopia
kopia = pygame.transform.rotate(grafikaEnemyCargo,90)
grafikaEnemyCargo = kopia
grafikaFabryka.set_colorkey('white')
grafikaFabrykaLewa.set_colorkey('white')
grafikaFabrykaPrawa.set_colorkey('white')
grafikaEnemy.set_colorkey('white')
grafikaEnemyMysliwiec.set_colorkey('white')
grafikaEnemyKanonierka.set_colorkey('white')
grafikaEnemyScigacz.set_colorkey('white')
grafikaEnemyBabowiec.set_colorkey('white')
grafikaEnemyCargo.set_colorkey('white')
grafikaEnemyKrazownik.set_colorkey('white')
grafikaEnemyPrzewodnik.set_colorkey('white')
grafikaEnemyWieza.set_colorkey('white')
grafikaEnemyBeczka.set_colorkey('white')
grafikaEnemyPancernik.set_colorkey('white')
grafikaEnemyHybryda.set_colorkey('white')
grafikaEnemyWsparcie.set_colorkey('white')
grafikaGwiazda1.set_colorkey('white')
grafikaGwiazda2.set_colorkey('white')
grafikaGwiazda3.set_colorkey('white')
grafikaGwiazda4.set_colorkey('white')
grafikaZnak.set_colorkey('white')

name = ""
db = sqlite3.connect("baza.db")
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS gracze(id integer PRIMARY KEY AUTOINCREMENT, name text,aktualneHP integer, maxHP integer, maxZlomu integer, zasiegMagnezu integer, rakietyMax integer,szybkoscRakiet integer,maxTemperatura integer,iloscLaserow integer,kosztNaprawy integer,cenaZlomu integer,mocLaseru integer,czasOdnawianiaOslony integer,kasa integer,procki integer,liczbaWykonanychMisji integer,trudnosc integer,strzalyAll integer,trafioneAll integer,kasaAll integer,prockiAll integer,wirus integer,mocRakiet integer,glowica integer,zlomAll integer, wykonaneObrony integer, wykonanePoscigi integer, wykonaneSzwadrony integer, wykonaneFabrykatory integer )")
cursor.execute("CREATE TABLE IF NOT EXISTS technologie(id integer PRIMARY KEY AUTOINCREMENT,gracz text,t0 integer,t1 integer,t2 integer,t3 integer,t4 integer,t5 integer,t6 integer,t7 integer,t8 integer,t9 integer,t10 integer,t11 integer,t12 integer,t13 integer,t14 integer)")
cursor.execute("CREATE TABLE IF NOT EXISTS zniszczone(id integer PRIMARY KEY AUTOINCREMENT,gracz text,w0 integer,w1 integer,w2 integer,w3 integer,w4 integer,w5 integer,w6 integer,w7 integer,w8 integer,w9 integer,w10 integer,w11 integer,w12 integer,w13 integer,w14 integer,w15 integer,w16 integer,w17 integer,w18 integer,w19 integer)")
cursor.execute("CREATE TABLE IF NOT EXISTS gwiazdy(id integer PRIMARY KEY AUTOINCREMENT,gracz text,g0 integer,g1 integer,g2 integer,g3 integer,g4 integer,g5 integer,g6 integer,g7 integer,g8 integer,g9 integer,g10 integer,g11 integer,g12 integer,g13 integer,g14 integer,g15 integer,g16 integer,g17 integer,g18 integer,g19 integer,g20 integer,g21 integer,g22 integer,g23 integer,g24 integer,g25 integer,g26 integer,g27 integer,g28 integer,g29 integer,g30 integer,g31 integer,g32 integer,g33 integer,g34 integer,g35 integer,g36 integer,g37 integer,g38 integer,g39 integer,g40 integer)")
cursor.execute("SELECT COUNT(*) FROM gracze")
iloscZapisow = cursor.fetchone()[0]
if iloscZapisow == 0:
    for i in range(5):
        cursor.execute("INSERT INTO gracze VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",["WOLNE",200,200,15,200,5,3,100,1,3,10,10,10000,5000,3,0,1,0,0,0,0,0,100,0,0,0,0,0,0])
        cursor.execute("INSERT INTO technologie VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", ["WOLNE",-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])
        cursor.execute("INSERT INTO zniszczone VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", ["WOLNE",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        cursor.execute("INSERT INTO gwiazdy VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", ["WOLNE",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

zapisy = []
iloscZapisow = 0
buttonsZapisy = []
buttonsUsunZapisy = []
def przygotujPrzyciskiOdczyt():
    global iloscZapisow, zapisy, buttonsZapisy, buttonsUsunZapisy
    cursor.execute("SELECT COUNT(*) FROM gracze WHERE name NOT LIKE ?",["WOLNE"])
    iloscZapisow = cursor.fetchone()[0]
    buttonsZapisy.clear()
    buttonsUsunZapisy.clear()
    if iloscZapisow > 0:
        cursor.execute("SELECT name,liczbaWykonanychMisji,TRUDNOSC FROM gracze WHERE name NOT LIKE ?",["WOLNE"])
        zapisy = cursor.fetchall()
        for zapis in zapisy:
            text = "Gracz: " + zapis[0] + "   Wykonane misje: " + str(zapis[1]) + "   Poziom: "
            if zapis[2] == 1:
                text += " normalny"
            if zapis[2] == 2:
                text += " trudny"
            if zapis[2] == 3:
                text += " hardcore"

            buttonsZapisy.append(Button('lightslateblue', 'cadetblue1', 'black', text))
            buttonsUsunZapisy.append(Button('lightslateblue', 'cadetblue1', 'black','Usuń zapis'))


przygotujPrzyciskiOdczyt()
def obliczOdleglosc(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def losujNoweMisje(wykonaneMisje):
    misje = []
    if wykonaneMisje < 3:
        misje.append(Misja(random.choice((1,2)),1))
        misje.append(Misja(random.choice((1,2,3,4)),1))
        misje.append(Misja(random.choice((1,2,3,4)),1))
    if wykonaneMisje >= 3 and wykonaneMisje < 6:
        misje.append(Misja(random.choice((1,2,3,4)),random.randint(1,2)))
        misje.append(Misja(random.choice((1,2,3,4)),2))
        misje.append(Misja(random.choice((1,2,3,4)),1))
    if wykonaneMisje >= 6 and wykonaneMisje < 9:
        misje.append(Misja(random.choice((1,2,3,4)),random.randint(1,3)))
        misje.append(Misja(random.choice((1,2,3,4)),3))
        misje.append(Misja(random.choice((1,2,3,4)),random.randint(2,3)))
    if wykonaneMisje >= 9 and wykonaneMisje < 12:
        misje.append(Misja(random.choice((1,2,3,4)),random.randint(1,4)))
        misje.append(Misja(random.choice((1,2,3,4)),4))
        misje.append(Misja(random.choice((1,2,3,4)),random.randint(2,4)))
    if wykonaneMisje >= 12 and wykonaneMisje < 15:
        misje.append(Misja(random.choice((1,2,3,4)),random.randint(1,5)))
        misje.append(Misja(random.choice((1,2,3,4)),5))
        misje.append(Misja(random.choice((1,2,3,4)),random.randint(3,5)))
    if wykonaneMisje >= 15 and wykonaneMisje < 17:
        misje.append(Misja(random.choice((1,2,3,4)),random.randint(1,7)))
        misje.append(Misja(random.choice((1,2,3,4)),7))
        misje.append(Misja(random.choice((1,2,3,4)),random.randint(3,7)))
    if wykonaneMisje >= 17 and wykonaneMisje < 19:
        misje.append(Misja(random.choice((1,2,3,4)),random.randint(1,8)))
        misje.append(Misja(random.choice((1,2,3,4)),8))
        misje.append(Misja(random.choice((1,2,3,4)),random.randint(4,8)))
    if wykonaneMisje >= 19 and wykonaneMisje < 21:
        misje.append(Misja(random.choice((1,2,3,4)),random.randint(1,9)))
        misje.append(Misja(random.choice((1,2,3,4)),9))
        misje.append(Misja(random.choice((1,2,3,4)),random.randint(5,9)))
    if wykonaneMisje >= 21:
        misje.append(Misja(random.choice((1,2,3,4)),random.randint(1,10)))
        misje.append(Misja(random.choice((1,2,3,4)),10))
        misje.append(Misja(random.choice((1,2,3,4)),random.randint(6,10)))

    random.shuffle(misje)
    return misje
def wyswietlStatystykeZniszczonych(listaZniszczonychAll = [],listaZniszczonychMisja = [] ,misia = False):

    if not misia:
        okno.blit(fontMala.render("ZNISZCZENI PRZECIWNICY", True, 'white'), (570, 55))


    if listaZniszczonychAll[1] == 0:
        okno.blit(grafikaZnak, (400, 100))
        okno.blit(fontMala.render(" ?????????", True, 'white'), (470, 100))
    else:
        okno.blit(grafikaEnemy, (400, 100))
        if  misia:
            okno.blit(fontMala.render(" Zwyklak: " + str(listaZniszczonychMisja[1]), True, 'white'), (470, 100))
        else:
            okno.blit(fontMala.render(" Zwyklak: " + str(listaZniszczonychAll[1]), True, 'white'), (470, 100))

    if listaZniszczonychAll[2] == 0:
        okno.blit(grafikaZnak, (400, 150))
        okno.blit(fontMala.render(" ?????????", True, 'white'), (470, 150))
    else:
        okno.blit(grafikaEnemyMysliwiec, (395, 150))
        if  misia:
            okno.blit(fontMala.render(" Myśliwiac: " + str(listaZniszczonychMisja[2]), True, 'white'), (470, 150))
        else:
            okno.blit(fontMala.render(" Myśliwiac: " + str(listaZniszczonychAll[2]), True, 'white'), (470, 150))

    if listaZniszczonychAll[3] == 0:
        okno.blit(grafikaZnak, (400, 200))
        okno.blit(fontMala.render(" ?????????", True, 'white'), (470, 205))
    else:
        okno.blit(grafikaEnemyKanonierka, (395, 200))
        if  misia:
            okno.blit(fontMala.render(" Kanonierka: " + str(listaZniszczonychMisja[3]), True, 'white'), (470, 205))
        else:
            okno.blit(fontMala.render(" Kanonierka: " + str(listaZniszczonychAll[3]), True, 'white'), (470, 205))

    if listaZniszczonychAll[4] == 0:
        okno.blit(grafikaZnak, (400, 255))
        okno.blit(fontMala.render(" ?????????", True, 'white'), (470, 260))
    else:
        okno.blit(grafikaEnemyScigacz, (395, 255))
        if  misia:
            okno.blit(fontMala.render(" Ścigacz: " + str(listaZniszczonychMisja[4]), True, 'white'), (470, 260))
        else:
            okno.blit(fontMala.render(" Ścigacz: " + str(listaZniszczonychAll[4]), True, 'white'), (470, 260))

    if listaZniszczonychAll[6] == 0:
        okno.blit(grafikaZnak, (400, 320))
        okno.blit(fontMala.render(" ?????????", True, 'white'), (470, 325))
    else:
        okno.blit(grafikaEnemyBabowiec, (395, 320))
        if  misia:
            okno.blit(fontMala.render(" Bombowiec: " + str(listaZniszczonychMisja[6]), True, 'white'), (470, 325))
        else:
            okno.blit(fontMala.render(" Bombowiec: " + str(listaZniszczonychAll[6]), True, 'white'), (470, 325))

    if listaZniszczonychAll[8] == 0:
        okno.blit(grafikaZnak, (400, 380))
        okno.blit(fontMala.render(" ?????????", True, 'white'), (470, 385))
    else:
        okno.blit(grafikaEnemyCargo, (395, 380))
        if  misia:
            okno.blit(fontMala.render(" Cargo: " + str(listaZniszczonychMisja[8]), True, 'white'), (470, 385))
        else:
            okno.blit(fontMala.render(" Cargo: " + str(listaZniszczonychAll[8]), True, 'white'), (470, 385))

    if listaZniszczonychAll[10] == 0:
        okno.blit(grafikaZnak, (400, 440))
        okno.blit(fontMala.render(" ?????????", True, 'white'), (470, 445))
    else:
        okno.blit(grafikaEnemyPrzewodnik, (405, 440))
        if  misia:
            okno.blit(fontMala.render(" Przewodnik: " + str(listaZniszczonychMisja[10]), True, 'white'), (470, 445))
        else:
            okno.blit(fontMala.render(" Przewodnik: " + str(listaZniszczonychAll[10]), True, 'white'), (470, 445))

    if listaZniszczonychAll[11] == 0:
        okno.blit(grafikaZnak, (400, 500))
        okno.blit(fontMala.render(" ?????????", True, 'white'), (470, 505))
    else:
        okno.blit(grafikaEnemyWieza, (400, 500))
        if  misia:
            okno.blit(fontMala.render(" Wieża: " + str(listaZniszczonychMisja[11]), True, 'white'), (470, 505))
        else:
            okno.blit(fontMala.render(" Wieża: " + str(listaZniszczonychAll[11]), True, 'white'), (470, 505))

    if listaZniszczonychAll[15] == 0:
        okno.blit(grafikaZnak, (700, 100))
        okno.blit(fontMala.render(" ?????????", True, 'white'), (770, 105))
    else:
        okno.blit(grafikaEnemyWsparcie, (700, 100))
        if  misia:
            okno.blit(fontMala.render(" Wsparciak: " + str(listaZniszczonychMisja[15]), True, 'white'), (790, 105))
        else:
            okno.blit(fontMala.render(" Wsparciak: " + str(listaZniszczonychAll[15]), True, 'white'), (790, 105))


    if listaZniszczonychAll[9] == 0:
        okno.blit(grafikaZnak, (700, 180))
        okno.blit(fontMala.render(" ?????????", True, 'white'), (770, 185))
    else:
        okno.blit(grafikaEnemyKrazownik, (700, 180))
        if  misia:
            okno.blit(fontMala.render(" Krążownik: " + str(listaZniszczonychMisja[9]), True, 'white'), (790, 185))
        else:
            okno.blit(fontMala.render(" Krążownik: " + str(listaZniszczonychAll[9]), True, 'white'), (790, 185))

    if listaZniszczonychAll[13] == 0:
        okno.blit(grafikaZnak, (700, 260))
        okno.blit(fontMala.render(" ?????????", True, 'white'), (770, 265))
    else:
        okno.blit(grafikaEnemyPancernik, (700, 260))
        if  misia:
            okno.blit(fontMala.render(" Pancernik: " + str(listaZniszczonychMisja[13]), True, 'white'), (790, 265))
        else:
            okno.blit(fontMala.render(" Pancernik: " + str(listaZniszczonychAll[13]), True, 'white'), (790, 265))

    if listaZniszczonychAll[14] == 0:
        okno.blit(grafikaZnak, (700, 340))
        okno.blit(fontMala.render(" ?????????", True, 'white'), (770, 345))
    else:
        okno.blit(grafikaEnemyHybryda, (700, 345))
        if  misia:
            okno.blit(fontMala.render(" Hybryda: " + str(listaZniszczonychMisja[14]), True, 'white'), (790, 345))
        else:
            okno.blit(fontMala.render(" Hybryda: " + str(listaZniszczonychAll[14]), True, 'white'), (790, 345))


def generujZlom(enemy,ZLOMY,PROCKI):
    ilosc_zlomu = 1
    if enemy.rodzaj == 1: ilosc_zlomu = random.randint(1,3)
    if enemy.rodzaj == 2: ilosc_zlomu = random.randint(2,4)
    if enemy.rodzaj == 3: ilosc_zlomu = random.randint(3,5)
    if enemy.rodzaj == 4: ilosc_zlomu = random.randint(3,5)
    if enemy.rodzaj == 5: ilosc_zlomu = 0
    if enemy.rodzaj == 6:
        ilosc_zlomu = random.randint(5,8)
        if random.randint(1,100) > 50:  PROCKI.append(Procek(enemy.x, enemy.y))
    if enemy.rodzaj == 7: ilosc_zlomu = random.randint(0,1)
    if enemy.rodzaj == 8:
        ilosc_zlomu = random.randint(8,12)
        if random.randint(1,100) > 50:  PROCKI.append(Procek(enemy.x, enemy.y))
    if enemy.rodzaj == 9:
        ilosc_zlomu = random.randint(6,8)
        PROCKI.append(Procek(enemy.x, enemy.y))
    if enemy.rodzaj == 10:
        ilosc_zlomu = random.randint(4,6)
        PROCKI.append(Procek(enemy.x, enemy.y))
        PROCKI.append(Procek(enemy.x, enemy.y))
    if enemy.rodzaj == 11:
        ilosc_zlomu = random.randint(4,7)
        PROCKI.append(Procek(enemy.x, enemy.y))
    if enemy.rodzaj == 12:
        ilosc_zlomu = random.randint(10, 12)
        PROCKI.append(Procek(enemy.x, enemy.y))
    if enemy.rodzaj == 13:
        ilosc_zlomu = random.randint(10, 14)
        PROCKI.append(Procek(enemy.x, enemy.y))
    if enemy.rodzaj == 14:
        ilosc_zlomu = random.randint(8, 12)
        PROCKI.append(Procek(enemy.x, enemy.y))
    if enemy.rodzaj == 15:
        ilosc_zlomu = random.randint(5, 8)
        PROCKI.append(Procek(enemy.x, enemy.y))
        if random.randint(1, 100) > 50:  PROCKI.append(Procek(enemy.x, enemy.y))


    for i in range(ilosc_zlomu):
        ZLOMY.append(Zlom(enemy.x,enemy.y))



SZEROKOSC = 1000
WYSOKOSC = 650
CZARNY = (0,0,0)
BIALY = (255,255,255)
CZERWONY = (255,0,0)
SZARY = (122,122,122)
LASERY = []
LASERY_ENEMY = []
WYBUCHY = []
ZLOMY = []
RAKIETY = []
RAKIETY_ENEMY = []
RODZAJ_MISJI = 1
DOSTEPNE_MISJE = []
AKTUALNA_MISJA = []
PROCKI = []
FAZA = 0
TRUDNOSC = 1
CZAS_GRY = 0
y_fabrykatora = 0
czas_gry = pygame.time.get_ticks()
prockiSprzedane = 0
# 0 - MENU
# 1 - WYBÓR MISJI
# 2 - MISJA
# 3 - ODLICZANIE
# 4 - PODSUMOWANIA MISJII
# 5 - BAZA
# 6 - STATYSTYKI ALL
# 7 - NAPRAWA DRONA
# 8 - ULEPSZENIA
# 9 - ZAPISZ GRĘ
# 10 - WCZYTAJ GRĘ
# 11 - NOWA GRA
# 12 - GWIAZY
# 13 - SKLEP
MUZA = False
KONIEC_MISJI = False
czasKoniec = pygame.time.get_ticks()
czasOdliczania = pygame.time.get_ticks()
czasKlik = pygame.time.get_ticks()
czasPoscigu = pygame.time.get_ticks()
czasAnimacji = pygame.time.get_ticks()
odliczanie = 3
nagrodaZaMisje = 0
misjaWykonana = False
iloscTechnologii = 15
TECHY = []
TECHY_WSZYSTKIE = []
GRA_ZAPISANA =False
AKTUALNA_LICZBA_GWIAZDEK = 0




okno = pygame.display.set_mode([SZEROKOSC, WYSOKOSC])
pygame.display.set_caption("Kosmos")
timer = pygame.time.Clock()
FPS = 60


tlo1 = pygame.image.load("Grafika\Tla\\tlo1.png")
tlo2 = pygame.image.load("Grafika\Tla\\tlo2.jpg")
tlo3 = pygame.image.load("Grafika\Tla\\tlo3.jpg")
tlo4 = pygame.image.load("Grafika\Tla\\tlo4.png")
hitD = pygame.mixer.Sound("Dzwieki\laser1.wav")
laserOdbityD = pygame.mixer.Sound("Dzwieki\sfx_weapon_singleshot10.wav")
wybuchD = pygame.mixer.Sound("Dzwieki\sfx_exp_short_hard15.wav")
wybuchRakietyD = pygame.mixer.Sound("Dzwieki\sfx_weapon_shotgun3.wav")
zlomD = pygame.mixer.Sound("Dzwieki\sfx_sounds_impact2.wav")
procekD = pygame.mixer.Sound("Dzwieki\sfx_coin_double4.wav")
sprzedajD = pygame.mixer.Sound("Dzwieki\sfx_coin_double3.wav")
produkcjaFabrykaD = pygame.mixer.Sound("Dzwieki\sfx_sounds_interaction12.wav")
muzyka1 = pygame.mixer.Sound("Muzyka\\n-Dimensions (Main Theme - Retro Ver.mp3")
muzyka2 = pygame.mixer.Sound("Muzyka\\Orbital Colossus.mp3")
muzyka3 = pygame.mixer.Sound("Muzyka\\fight.ogg")
muzykaMENU = pygame.mixer.Sound("Muzyka\\through space (mp3cut.net).mp3")
#muzyka2 = pygame.mixer.Sound("Muzyka\\18. Fc Kahuna - Glitterball.Mp3")
hitD.set_volume(0.1)
zlomD.set_volume(0.5)
button = Button('lightslateblue','cadetblue1','black','Rozpocznij misję')
button1 = Button('lightslateblue','cadetblue1','black','Losuj nowe misje (100$)')
button2 = Button('lightslateblue','cadetblue1','black','Powrót')
buttonMisja = Button('lightslateblue','cadetblue1','black','WYRUSZ NA MISJĘ !',20,20)
buttonStstystyki = Button('lightslateblue','cadetblue1','black','Zobasz statystyki')
buttonNaprawa = Button('lightslateblue','cadetblue1','black','Napraw drona')
buttonUlepszenia = Button('lightslateblue','cadetblue1','black','Ulepszenie')
buttonTechnilogie = Button('lightslateblue','cadetblue1','black','Technologie')
buttonBaza = Button('lightslateblue','cadetblue1','black','Powrót do bazy')
buttonNapraw1 = Button('lightslateblue','cadetblue1','black','Napraw o 1HP ('+' $)')
buttonNapraw10 = Button('lightslateblue','cadetblue1','black','Napraw o 10HP ('+' $)')
buttonNaprawMAX = Button('lightslateblue','cadetblue1','black','Napraw do MAX:' + '('+' $)')
buttonZbadaj1 = Button('lightslateblue', 'cadetblue1', 'black', 'Zbadaj',10,3)
buttonZbadaj2 = Button('lightslateblue', 'cadetblue1', 'black', 'Zbadaj',10,3)
buttonZbadaj3 = Button('lightslateblue', 'cadetblue1', 'black', 'Zbadaj',10,3)
buttonKup11 = Button('lightslateblue', 'cadetblue1', 'black', 'Kup',13,3)
buttonKup21 = Button('lightslateblue', 'cadetblue1', 'black', 'Kup',13,3)
buttonKup31 = Button('lightslateblue', 'cadetblue1', 'black', 'Kup',13,3)
buttonKup12 = Button('lightslateblue', 'cadetblue1', 'black', 'Kup',13,3)
buttonKup22 = Button('lightslateblue', 'cadetblue1', 'black', 'Kup',13,3)
buttonKup32 = Button('lightslateblue', 'cadetblue1', 'black', 'Kup',13,3)
buttonTECH_P = Button('lightslateblue', 'cadetblue1', 'black', '>',15,15)
buttonTECH_L = Button('lightslateblue', 'cadetblue1', 'black', '<',15,15)
buttonKONIEC = Button('lightslateblue', 'cadetblue1', 'black', 'KONIEC',70)
buttonTRUDNOSC = Button('lightslateblue', 'cadetblue1', 'black', 'Ustaw poziom TRUDNOŚCI',10)
buttonZAPISZ = Button('lightslateblue', 'cadetblue1', 'black', 'Zapisz stan gry',10)
buttonKONTYNUUJ = Button('lightslateblue', 'cadetblue1', 'black', 'WCZYTAJ GRĘ',50)
buttonNOWA_GRA = Button('lightslateblue', 'cadetblue1', 'black', 'NOWA GRA',60)
buttonGWIAZDY = Button('lightslateblue', 'cadetblue1', 'black', 'Osiągnięcia')
buttonSKLEP = Button('lightslateblue', 'cadetblue1', 'black', 'Sklep')
buttonSPRZEDAJ_PROCKI = Button('lightslateblue', 'cadetblue1', 'black', 'Sprzedaj procki')

buttonINNE = Button('lightslateblue', 'cadetblue1', 'black', 'Podaj inne imię',10)
buttonMENU = Button('lightslateblue', 'cadetblue1', 'black', 'Wróć do MENU gry',10)
buttonROZPOCZNIJ = Button('lightslateblue', 'cadetblue1', 'black', 'ROZPOCZNIJ GRĘ !',50,20)
fontOdliczanie = pygame.font.SysFont('perpetuatitlingpogrubiony', 450)
fontNazwyFaz = pygame.font.SysFont('comicsansms', 50)
font40 = pygame.font.SysFont('comicsansms', 80)
fontMala = pygame.font.SysFont('comicsansms', 20)
fontMniejsza = pygame.font.SysFont('comicsansms', 15)
wybranoMisje = False
numerWybranejMisji = 0

def trudnoscNAstring(TRUDNOSC):
    if TRUDNOSC == 1:
        return "normalna"
    if TRUDNOSC == 2:
        return "trudna"
    if TRUDNOSC == 3:
        return "hardcore"

def takiProfilJuzIstnieje(name):
    cursor.execute("SELECT name FROM gracze")
    names = []
    for n in cursor:
        names.append(n[0])
    return name in names

GRACZ = 0
ENEMY = []
AKTUALNY_ID_PROFILU = 0

muzyka1.set_volume(0.2)
muzyka2.set_volume(0.2)
muzykaMENU.set_volume(0.2)
MUZYKA = muzyka1

run = True
podawanieName = False
czasRespienia = 0
muzykaMENU.play()

while run:

    if pygame.time.get_ticks() - czas_gry > 1000:
        czas_gry = pygame.time.get_ticks()
        CZAS_GRY += 1

    timer.tick(FPS)
    okno.fill('indigo')
    klawisze = pygame.key.get_pressed()
    myszPozycja = pygame.mouse.get_pos()
    myszKlik = pygame.mouse.get_pressed()

    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            run = False
        if podawanieName and FAZA == 11 and len(name) < 9:
            if zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_a:name+="A"
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_b:name+="B"
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_c:name+="C"
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_d:name+="D"
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_e:name+="E"
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_f:name+="F"
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_g:name+="G"
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_h:name+="H"
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_i:name+="I"
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_j:name+="J"
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_k:name+="K"
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_l:name+="L"
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_m:name+="M"
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_n:name+="N"
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_o:name+="O"
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_p:name+="P"
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_r:name+="R"
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_s:name+="S"
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_t:name+="T"
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_y:name+="Y"
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_u:name+="U"
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_z:name+="Z"
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_w:name+="W"
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_SPACE:name+=" "
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_x:name+="X"
            elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_v:name+="V"
        if len(name) > 0 and podawanieName and FAZA == 11 and zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_BACKSPACE:
                kopiaName = ""
                for i in range(len(name)-1):
                    kopiaName += name[i]
                name = ""
                name = kopiaName
    if klawisze[pygame.K_ESCAPE]: run = False
    #MENU
    if FAZA == 0:
        okno.blit(grafikaScreen,(350,5))
        okno.blit(font40.render("HORDOWIE ATAKUJĄ!!! ", True, BIALY), (20, 100))

        buttonNOWA_GRA.render(okno, 30, 580, 280, 50)
        if iloscZapisow > 0:
            buttonKONTYNUUJ.render(okno, 360, 580, 280, 50)
        buttonKONIEC.render(okno, 690, 580, 280, 50)

        if buttonKONIEC.clik():
            run = False
        if buttonNOWA_GRA.clik():
            FAZA = 11
            podawanieName = True
        if buttonKONTYNUUJ.clik():
            FAZA = 10
            buttonMENU.time = pygame.time.get_ticks()

        #nowa gra
    if FAZA == 11:

        cursor.execute("SELECT COUNT(*) FROM gracze WHERE name = ?", ["WOLNE"])
        liczbaWolnychProfili = cursor.fetchone()[0]
        if liczbaWolnychProfili > 0:
            okno.blit(fontNazwyFaz.render("ZAKŁADANIE NOWEGO PROFILU", True, BIALY), (90, 10))
            okno.blit(fontNazwyFaz.render("Podaj nazwę profilu: " + name, True, BIALY), (50, 100))
            if takiProfilJuzIstnieje(name) and len(name) > 0:
                okno.blit(fontNazwyFaz.render("Taki profil już istnieje", True, BIALY), (50, 200))
            else:
                if len(name) > 0:
                    okno.blit(fontNazwyFaz.render("Ustaw trudność: " + trudnoscNAstring(TRUDNOSC), True, BIALY), (50, 200))
                    buttonTRUDNOSC.render(okno, 680, 215, 280, 50)
                    if buttonTRUDNOSC.clik():
                        TRUDNOSC += 1
                        if TRUDNOSC > 3:
                            TRUDNOSC = 1
                    buttonROZPOCZNIJ.render(okno, 350, 300, 300, 80)
                    if buttonROZPOCZNIJ.clik():
                        cursor.execute("SELECT MIN(id) FROM gracze WHERE name = ?",["WOLNE"])
                        id = cursor.fetchone()[0]
                        AKTUALNY_ID_PROFILU = id
                        cursor.execute("UPDATE gracze SET name = ? WHERE id = ?",[name,id])
                        cursor.execute("UPDATE technologie SET gracz = ? WHERE id = ?",[name,id])
                        cursor.execute("UPDATE zniszczone SET gracz = ? WHERE id = ?",[name,id])
                        cursor.execute("UPDATE gwiazdy SET gracz = ? WHERE id = ?",[name,id])
                        db.commit()
                        GRACZ = Gracz(1, 1, TRUDNOSC)
                        for i in range(iloscTechnologii):
                            TECHY_WSZYSTKIE.append(Technologia(i))
                            TECHY_WSZYSTKIE[i].odswiezObraz(GRACZ)
                            TECHY.append(TECHY_WSZYSTKIE[i])
                        iloscTechnologii = len(TECHY)
                        numerTechu = 0
                        DOSTEPNE_MISJE = losujNoweMisje(GRACZ.wykonaneMisje)
                        ENEMY = DOSTEPNE_MISJE[0].inicjujWrogow(TRUDNOSC)
                        katGracza = 0
                        FAZA = 5
                        podawanieName = False
        else:
            okno.blit(fontNazwyFaz.render("Brak wolnych profili :(", True, BIALY), (50, 200))
        buttonMENU.render(okno, 400, 580, 250, 50)
        if buttonMENU.clik():
            FAZA = 0
            buttonKONTYNUUJ.time = pygame.time.get_ticks()
        # Odczyt
    if FAZA == 10:
        okno.blit(fontNazwyFaz.render("WYBIERZ I WCZYTAJ PROFIL ", True, BIALY), (90, 10))
        buttonKONIEC.render(okno, 700, 580, 250, 50)
        buttonMENU.render(okno, 400, 580, 250, 50)
        y = 100
        for i in range(len(zapisy)):
            buttonsZapisy[i].render(okno,50,y,600,50)
            buttonsUsunZapisy[i].render(okno,750,y,150,50)

            y+=60
            if buttonsZapisy[i].clik():
                imie = zapisy[i][0]

                cursor.execute("SELECT * FROM gracze WHERE name = ?",[imie])
                d = cursor.fetchone()
                print(d)
                print(len(d))
                GRACZ = Gracz(1,1,d[17],d[2],d[3],d[4],d[5],d[6],d[7],d[8],d[9],d[10],d[11],d[12],d[13],d[14],d[15],d[16],d[18],d[19],d[20],d[21],d[22],d[23],d[24],d[25],d[26],d[27],d[28],d[29])

                DOSTEPNE_MISJE = losujNoweMisje(GRACZ.wykonaneMisje)
                FAZA = 5
                cursor.execute("SELECT id FROM gracze WHERE name = ?", [imie])
                id = cursor.fetchone()[0]
                AKTUALNY_ID_PROFILU = id
                cursor.execute("SELECT * FROM zniszczone WHERE id = ?",[id])
                z = cursor.fetchone()
                Z = []
                for i in range(2,len(z)):
                    Z.append(z[i])
                GRACZ.zniszczone.clear()
                for zn in Z:
                    GRACZ.zniszczone.append(zn)
                cursor.execute("SELECT * FROM technologie WHERE id = ?",[id])
                t = cursor.fetchone()
                T = []
                for i in range(2,len(t)):
                    T.append(t[i])
                TECHY.clear()
                for i in range(iloscTechnologii):
                    TECHY.append(Technologia(i,T[i]))
                    TECHY[i].odswiezObraz(GRACZ)
                buttonKONIEC.time = pygame.time.get_ticks()
                katGracza = 0
                buttonBaza.updateText("Powrót do bazy")
                cursor.execute("SELECT * FROM gwiazdy WHERE id = ?", [id])
                g = cursor.fetchone()
                G = []
                for i in range(2, len(g)):
                    G.append(g[i])
                print(G)
                print(len(G))
                for i in range(len(G)):
                    if G[i] == 1:
                        GRACZ.gwiazdy[i].zalicz()
                AKTUALNA_LICZBA_GWIAZDEK = GRACZ.zliczGwiazdy()
                przygotujPrzyciskiOdczyt()
                break

            if buttonsUsunZapisy[i].clik():
                imie = zapisy[i][0]
                cursor.execute("SELECT id FROM gracze WHERE name = ?", [imie])
                idDELETE = cursor.fetchone()[0]
                cursor.execute("DELETE FROM gracze WHERE name = ?", [imie])
                cursor.execute("DELETE FROM technologie WHERE id = ?", [idDELETE])
                cursor.execute("DELETE FROM zniszczone WHERE id = ?", [idDELETE])
                cursor.execute("DELETE FROM gwiazdy WHERE id = ?", [idDELETE])
                cursor.execute(
                    "INSERT INTO gracze VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    ["WOLNE", 200, 200, 15, 200, 5, 3, 100, 1, 3, 10, 10, 10000, 5000, 3, 0, 1, 0, 0, 0, 0, 0, 100, 0,
                     0, 0, 0, 0, 0])
                cursor.execute("INSERT INTO technologie VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                               ["WOLNE", -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])
                cursor.execute("INSERT INTO zniszczone VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                               ["WOLNE", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                cursor.execute(
                    "INSERT INTO gwiazdy VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    ["WOLNE", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

                db.commit()
                zapisy.pop(i)
                buttonsUsunZapisy.pop(i)
                buttonsZapisy.pop(i)
                for przyciski in buttonsUsunZapisy:
                    przyciski.time = pygame.time.get_ticks()
                przygotujPrzyciskiOdczyt()

                break

        if buttonMENU.clik():
            FAZA = 0
            buttonKONTYNUUJ.time = pygame.time.get_ticks()
        if buttonKONIEC.clik():
            run = False
    # Zapisz
    if FAZA == 9:
        cursor.execute("SELECT name FROM gracze WHERE id = ?", [AKTUALNY_ID_PROFILU])
        aktualneName = cursor.fetchone()[0]
        cursor.execute("DELETE FROM gracze WHERE id = ?", [AKTUALNY_ID_PROFILU])
        cursor.execute("DELETE FROM technologie WHERE id = ?", [AKTUALNY_ID_PROFILU])
        cursor.execute("DELETE FROM zniszczone WHERE id = ?", [AKTUALNY_ID_PROFILU])
        cursor.execute("DELETE FROM gwiazdy WHERE id = ?", [AKTUALNY_ID_PROFILU])
        cursor.execute("INSERT INTO gracze VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",[AKTUALNY_ID_PROFILU,aktualneName,GRACZ.hp,GRACZ.maxHP,GRACZ.maxZlom,GRACZ.zasiegMagnesu,GRACZ.maxRakiety,GRACZ.szybkoscRakiet,GRACZ.maxTemperatura,GRACZ.iloscLaserow,GRACZ.kosztNaprawy, GRACZ.cenaZlomu,GRACZ.mocLaseru,GRACZ.czasOdnawianiaOslony,GRACZ.kasa,GRACZ.procki,GRACZ.wykonaneMisje, TRUDNOSC, GRACZ.strzalyAll,GRACZ.trafioneAll,GRACZ.kasaAll,GRACZ.prockiAll,GRACZ.wirus,GRACZ.mocRakiet,GRACZ.glowica,GRACZ.zlomAll,GRACZ.wykonaneObrony,GRACZ.wykonanePoscigi,GRACZ.wykonaneSzwadrony,GRACZ.wykonaneFabrykatory])
        lista = [AKTUALNY_ID_PROFILU,aktualneName]
        for tech in TECHY:
            lista.append(tech.stopien)
        cursor.execute("INSERT INTO technologie VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",lista)
        lista.clear()
        lista = [AKTUALNY_ID_PROFILU,aktualneName]
        for zn in GRACZ.zniszczone:
                lista.append(zn)
        cursor.execute("INSERT INTO zniszczone VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",lista)
        lista.clear()
        lista = [AKTUALNY_ID_PROFILU, aktualneName]
        for gw in GRACZ.gwiazdy:
            lista.append(gw.zaliczone)
        cursor.execute("INSERT INTO gwiazdy VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",lista)

        db.commit()
        GRA_ZAPISANA = True
        FAZA = 5

    # Sklep
    if FAZA == 13:
        okno.blit(fontNazwyFaz.render("SKLEP", True, BIALY), (90, 10))

        buttonBaza.render(okno, 700,540, 250, 50)
        if buttonBaza.clik():
            FAZA = 5
            buttonMENU.time = pygame.time.get_ticks()
            buttonKONIEC.time = pygame.time.get_ticks()
        okno.blit(fontMala.render("PROCKI:         " + str(GRACZ.procki), True, BIALY), (20, 480))
        okno.blit(fontMala.render("KASA:           " + str(GRACZ.kasa) + " $", True, BIALY), (20, 500))
        if GRACZ.procki > 0:
            okno.blit(fontMala.render("Ile procków chcesz sprzedać? MAX: " + str(GRACZ.procki), True, BIALY), (20, 80))
            buttonTECH_L.render(okno,20,130,40,40)
            buttonTECH_P.render(okno,320,130,40,40)
            pasek(okno,65,130,40,250,GRACZ.procki,prockiSprzedane,'black',"springgreen2")
            okno.blit(fontMala.render("Procki: " + str(prockiSprzedane) + " = " + str(prockiSprzedane*50)+"$", True, BIALY), (85, 135))

        if buttonTECH_L.clik() and prockiSprzedane > 0:
            prockiSprzedane -= 1

        if buttonTECH_P.clik() and prockiSprzedane < GRACZ.procki:
            prockiSprzedane += 1
        if prockiSprzedane > 0:
            buttonSPRZEDAJ_PROCKI.render(okno, 80, 200, 200, 50)

        if buttonSPRZEDAJ_PROCKI.clik():
            GRACZ.procki -= prockiSprzedane
            GRACZ.kasa += (prockiSprzedane*50)
            prockiSprzedane = 0
            sprzedajD.play()

        dopalacz1.render(okno,myszPozycja)



    if FAZA == 5:

        okno.blit(fontNazwyFaz.render("BAZA", True, BIALY), (90, 10))
        x = 700
        y = 50
        if GRACZ.hp != GRACZ.maxHP:
            buttonNaprawa.color = (255,255,0)
        else:
            buttonNaprawa.color = 'lightslateblue'
        buttonNaprawa.render(okno,x,40,250,50)
        buttonUlepszenia.render(okno, x, 100, 250, 50)
        buttonStstystyki.render(okno,x,160,250,50)
        if AKTUALNA_LICZBA_GWIAZDEK != GRACZ.zliczGwiazdy():
            buttonGWIAZDY.color = (255, 255, 0)
        else:
            buttonGWIAZDY.color = 'lightslateblue'
        buttonGWIAZDY.render(okno, x, 220, 250, 50)
        buttonSKLEP.render(okno, x, 280, 250, 50)
        buttonMisja.render(okno, x, 370, 250, 75)
        if not GRA_ZAPISANA:
            buttonZAPISZ.render(okno,x,470,250,50)

        buttonMENU.render(okno, x, y+475, 250, 50)
        if buttonMENU.clik():
            FAZA = 0
            buttonKONTYNUUJ.time = pygame.time.get_ticks()

        buttonKONIEC.render(okno,700,y+530,250,50)
        okno.blit(fontMala.render("T W Ó J   D R O N", True, BIALY), (50, 80))
        okno.blit(fontMala.render("HP:                                "+ str(GRACZ.maxHP)+"/",True, BIALY), (20, 115))
        if GRACZ.maxHP == GRACZ.hp:
            okno.blit(fontMala.render(str(GRACZ.hp),True, BIALY), (288, 115))
        else:
            okno.blit(fontMala.render(str(GRACZ.hp),True, CZERWONY), (288, 115))

        okno.blit(fontMala.render("SZYBKOŚĆ:                  " + str(GRACZ.dx), True, BIALY), (20, 140))
        okno.blit(fontMala.render("LASERY:                       " + str(GRACZ.iloscLaserow), True, BIALY), (20, 165))
        okno.blit(fontMala.render("MOC LASERU:              " + str(GRACZ.mocLaseru), True, BIALY), (20, 190))
        okno.blit(fontMala.render("TEMPERATURA:           " + str(GRACZ.maxTemperatura), True, BIALY), (20, 215))
        okno.blit(fontMala.render("MAGAZYN ZŁOMU:     " + str(GRACZ.maxZlom), True, BIALY), (20, 240))
        okno.blit(fontMala.render("ZASIĘG MAGNESU:    " + str(GRACZ.zasiegMagnesu), True, BIALY), (20, 265))
        okno.blit(fontMala.render("ILOŚĆ RAKIET:            " + str(GRACZ.maxRakiety), True, BIALY), (20, 290))
        okno.blit(fontMala.render("SZYBKOŚĆ RAKIET:     " + str(GRACZ.szybkoscRakiet), True, BIALY), (20, 315))
        okno.blit(fontMala.render("MOC RAKIET:              " + str(GRACZ.mocRakiet), True, BIALY), (20, 340))
        okno.blit(fontMala.render("KOSZT NAPRAWY:      " + str(GRACZ.kosztNaprawy) + "$ / 1 HP", True, BIALY), (20, 365))
        okno.blit(fontMala.render("CENA ZŁOMU:             " + str(GRACZ.cenaZlomu) + "$ / 1 złom", True, BIALY), (20, 390))
        okno.blit(fontMala.render("CZAS OSŁONY:           " + str(GRACZ.czasOdnawianiaOslony/1000) + " s", True, BIALY), (20, 415))
        okno.blit(fontMala.render("PROCKI:         " + str(GRACZ.procki) , True, BIALY), (20, 480))
        okno.blit(fontMala.render("KASA:           " + str(GRACZ.kasa) + " $", True, BIALY), (20, 500))
        if TRUDNOSC == 1:
            okno.blit(fontMala.render("TRUDNOŚĆ GRY: NORMALNA", True, BIALY), (20, 560))
        elif TRUDNOSC == 2:
            okno.blit(fontMala.render("TRUDNOŚĆ GRY: TRUDNA", True, BIALY), (20, 560))
        elif TRUDNOSC == 3:
            okno.blit(fontMala.render("TRUDNOŚĆ GRY: HARDCORE", True, BIALY), (20, 560))

        if buttonKONIEC.clik():
            run = False
        if buttonSKLEP.clik():
            FAZA = 13
            prockiSprzedane = 0

        if buttonUlepszenia.clik():
            FAZA = 8
            numerTechu = 0
        if buttonMisja.clik() and GRACZ.hp > 0:
            FAZA = 1
            muzykaMENU.set_volume(0.08)
        if buttonStstystyki.clik():
            FAZA = 6
        if buttonGWIAZDY.clik():
            FAZA = 12
            AKTUALNA_LICZBA_GWIAZDEK = GRACZ.zliczGwiazdy()

        if buttonNaprawa.clik() and GRACZ.hp < GRACZ.maxHP:
            FAZA = 7
            buttonNapraw1.time = pygame.time.get_ticks()
            buttonNapraw10.time = pygame.time.get_ticks()
            buttonNaprawMAX.time = pygame.time.get_ticks()
        kopia = pygame.transform.scale(GRACZ.oryginalnaGrafika, (200, 140))
        kopia = pygame.transform.rotate(kopia, katGracza)
        kopia.set_colorkey('white')
        nx = (450 + (GRACZ.oryginalnaGrafika.get_width() - kopia.get_width()) / 2)
        ny = (120 + ((GRACZ.oryginalnaGrafika.get_height() - kopia.get_height()) / 2))
        okno.blit(kopia,(nx,ny))

        if pygame.time.get_ticks() - czasAnimacji > 50:
            czasAnimacji = pygame.time.get_ticks()
            katGracza+=1
            if katGracza > 360: katGracza = 0

        if buttonZAPISZ.clik():
            FAZA = 9

    if FAZA == 12:
        okno.blit(fontNazwyFaz.render("Twoje osiągnięcia ", True, BIALY), (180, 2))
        buttonBaza.render(okno, 30, WYSOKOSC - 70, 180, 50)


        if buttonBaza.clik():
            FAZA = 5
            GRACZ.zaktualizujNumeryGwiazdek()

        ilosc = 0
        xg = 30
        yg = 80
        for gwiazda in GRACZ.gwiazdy:
            ilosc += 1
            if ilosc == 17 or ilosc == 33:
                yg += 60
                xg = 30
            if gwiazda.numer not in GRACZ.numeryPosiadanychGwiazdek:
                gwiazda.render(okno,xg,yg,myszPozycja,True)
            else:
                gwiazda.render(okno,xg,yg,myszPozycja)
            xg += 60

        for i in range(35):
            if i < GRACZ.zliczGwiazdy():
                if i % 5 == 0 and i != 0:
                    okno.blit(grafikaGwiazda2, (10 + (i * 28), 500))
                else:
                    okno.blit(grafikaGwiazda2, (10 + (i * 28), 510))
            else:
                if i % 5 == 0 and i != 0:
                    okno.blit(grafikaGwiazda1, (10 + (i * 28), 500))
                else:
                    okno.blit(grafikaGwiazda1, (10 + (i * 28), 510))



    # STATYSTYKI ALL
    if FAZA == 6:
        buttonBaza.render(okno, 50, WYSOKOSC - 100, 180, 50)
        if buttonBaza.clik():
            FAZA = 5

            buttonKONIEC.time = pygame.time.get_ticks()
        okno.blit(fontNazwyFaz.render("Twoje statystyki ", True, BIALY), (150, 2))

        y = 90
        #okno.blit(fontMala.render("STATYSTYKI MISJI: ", True, CZARNY), (10, y))
        okno.blit(fontMala.render("Strzały laserem: " + str(GRACZ.strzalyAll), True, BIALY), (30, y+30))
        okno.blit(fontMala.render("Trafione: " + str(GRACZ.trafioneAll), True, BIALY), (30, y+50))
        if GRACZ.trafioneAll > 0:
            okno.blit(fontMala.render("Procent trafień: " + str(round((GRACZ.trafioneAll*100)/GRACZ.strzalyAll,1)) + " %", True, BIALY), (30, y+70))
        else:
            okno.blit(fontMala.render("Procent trafień: 0" , True, BIALY), (30, y+70))
        okno.blit(fontMala.render("Zebrany złom: " + str(GRACZ.zlomAll), True, BIALY),(30, y+90))
        okno.blit(fontMala.render("Zarobiona kasa: " + str(GRACZ.kasaAll) + " $", True, BIALY),(30, y+110))
        okno.blit(fontMala.render("Zebrane procki: " + str(GRACZ.prockiAll) , True, BIALY),(30, y+130))
        okno.blit(fontMala.render("Wykonane misje: " + str(GRACZ.wykonaneMisje) , True, BIALY),(30, y+160))
        okno.blit(fontMala.render("Wykonane Obrony planety: " + str(GRACZ.wykonaneObrony) , True, BIALY),(30, y+180))
        okno.blit(fontMala.render("Wykonane Pościgi: " + str(GRACZ.wykonanePoscigi) , True, BIALY),(30, y+200))
        okno.blit(fontMala.render("Wykonane Szwadrony: " + str(GRACZ.wykonaneSzwadrony) , True, BIALY),(30, y+220))
        okno.blit(fontMala.render("Wykonane Fabrykatory: " + str(GRACZ.wykonaneFabrykatory) , True, BIALY),(30, y+240))
        okno.blit(fontMala.render("Pokonanych przeciwników: " + str(sum(GRACZ.zniszczone)) , True, BIALY),(30, y+320))
        wyswietlStatystykeZniszczonych(GRACZ.zniszczone,GRACZ.zniszczoneMisja,False)
#naprawa
    if FAZA == 7:
        okno.blit(fontNazwyFaz.render("Naprawa drona ", True, BIALY), (150, 2))
        buttonBaza.render(okno, 50, WYSOKOSC - 100, 180, 50)
        if buttonBaza.clik():
            FAZA = 5
            GRA_ZAPISANA = False
            buttonKONIEC.time = pygame.time.get_ticks()

        pasek(okno, 20, 250, 50, 400, GRACZ.maxHP, GRACZ.hp, (255, 255, 255))

        okno.blit(fontMala.render("MAKSYMALNE HP:          " + str(GRACZ.maxHP), True, BIALY), (20, 90))
        okno.blit(fontMala.render("AKTUALNE HP:               " + str(GRACZ.hp), True, BIALY), (20, 120))
        okno.blit(fontMala.render("DOSTĘPNA  KASA:         " + str(GRACZ.kasa) + " $", True, BIALY), (20, 150))
        okno.blit(fontMala.render("KOSZT NAPRAWY:         " + str(GRACZ.kosztNaprawy) + " $/1HP", True, BIALY), (20, 180))
        x = 700
        y = 50
        buttonNaprawMAX.updateText('Napraw do MAX:' + '('+str(GRACZ.kosztNaprawy*(GRACZ.maxHP-GRACZ.hp))+' $)')
        buttonNapraw1.updateText('Napraw o 1HP ('+str(GRACZ.kosztNaprawy)+' $)')
        buttonNapraw10.updateText('Napraw o 10HP ('+str(GRACZ.kosztNaprawy*10)+' $)')
        buttonNapraw1.render(okno,x,y,250,50)
        buttonNapraw10.render(okno,x,y+60,250,50)
        buttonNaprawMAX.render(okno,x,y+120,250,50)
        if buttonNapraw1.clik() and GRACZ.kasa >= GRACZ.kosztNaprawy and GRACZ.maxHP - GRACZ.hp > 1:
            GRACZ.kasa -= GRACZ.kosztNaprawy
            GRACZ.hp += 1
            if GRACZ.hp > GRACZ.maxHP:
                GRACZ.hp = GRACZ.maxHP
        if buttonNapraw10.clik() and GRACZ.kasa >= GRACZ.kosztNaprawy*10 and GRACZ.maxHP - GRACZ.hp > 9:
            GRACZ.kasa -= GRACZ.kosztNaprawy*10
            GRACZ.hp += 10
            if GRACZ.hp > GRACZ.maxHP:
                GRACZ.hp = GRACZ.maxHP
        if buttonNaprawMAX.clik() and GRACZ.kasa >= (GRACZ.maxHP - GRACZ.hp)*GRACZ.kosztNaprawy and GRACZ.hp < GRACZ.maxHP:
            GRACZ.kasa -= ((GRACZ.maxHP - GRACZ.hp)*GRACZ.kosztNaprawy)
            GRACZ.hp = GRACZ.maxHP

    # ulepszenia
    if FAZA == 8:
        okno.blit(fontNazwyFaz.render("Kup ulepszenia i zbadaj technologie", True, BIALY),(50,10))
        buttonBaza.render(okno, 30,580, 180, 50)
        if buttonBaza.clik():
            FAZA = 5
            GRA_ZAPISANA = False
            buttonKONIEC.time = pygame.time.get_ticks()

        buttonTECH_L.render(okno,30,200,50,50)
        buttonTECH_P.render(okno,920,200,50,50)

        if buttonTECH_L.clik() and numerTechu > 0:
            numerTechu -= 1
        if buttonTECH_P.clik():
            if numerTechu < iloscTechnologii-3:
                numerTechu += 1

        pygame.draw.rect(okno,(115,106,255),((110,100),(250,300)),0,15)
        if pygame.Rect(((110,100),(250,300))).collidepoint(myszPozycja):
            okno.blit(fontMala.render(TECHY[numerTechu].opis, True, BIALY), (100, 410))

        okno.blit(TECHY[numerTechu].pokazObrazek(),(115,105))
        if not TECHY[numerTechu].stopien > -1 and GRACZ.procki >= TECHY[numerTechu].cenaBadania:
            buttonZbadaj1.render(okno,245,155,100,40)
            if buttonZbadaj1.clik():
                TECHY[numerTechu].zbadaj(GRACZ)


        if TECHY[numerTechu].stopien > -1 and TECHY[numerTechu].stopien == 0 and GRACZ.kasa >= TECHY[numerTechu].cena1:
            buttonKup11.render(okno,245,250,100,40)
            if buttonKup11.clik():
                TECHY[numerTechu].kup(GRACZ)


        if TECHY[numerTechu].stopien > -1 and TECHY[numerTechu].stopien == 1 and GRACZ.kasa >= TECHY[numerTechu].cena2 and TECHY[numerTechu].stopien == 1:
            buttonKup12.render(okno,245,345,100,40)
            if buttonKup12.clik():
                TECHY[numerTechu].kup(GRACZ)



        pygame.draw.rect(okno,(115,106,255),((370,100),(250,300)),0,15)
        if pygame.Rect(((370,100),(250,300))).collidepoint(myszPozycja):
            okno.blit(fontMala.render(TECHY[numerTechu+1].opis, True, BIALY), (100, 410))
        okno.blit(TECHY[numerTechu+1].pokazObrazek(), (375, 105))
        if TECHY[numerTechu+1].stopien == -1 and GRACZ.procki >= TECHY[numerTechu+1].cenaBadania:
            buttonZbadaj2.render(okno,505,155,100,40)
            if buttonZbadaj2.clik():
                TECHY[numerTechu+1].zbadaj(GRACZ)

        if TECHY[numerTechu+1].stopien>-1 and TECHY[numerTechu+1].stopien == 0 and GRACZ.kasa >= TECHY[numerTechu+1].cena1:
            buttonKup21.render(okno,505,250,100,40)
            if buttonKup21.clik():
                TECHY[numerTechu+1].kup(GRACZ)

        if TECHY[numerTechu+1].stopien>-1 and TECHY[numerTechu+1].stopien == 1 and GRACZ.kasa >= TECHY[numerTechu+1].cena2 and TECHY[numerTechu+1].stopien == 1:
            buttonKup22.render(okno,505,345,100,40)
            if buttonKup22.clik():
                TECHY[numerTechu+1].kup(GRACZ)


        pygame.draw.rect(okno,(115,106,255),((630,100),(250,300)),0,15)
        if pygame.Rect(((630,100),(250,300))).collidepoint(myszPozycja):
            okno.blit(fontMala.render(TECHY[numerTechu+2].opis, True, BIALY), (100, 410))
        okno.blit(TECHY[numerTechu+2].pokazObrazek(), (635, 105))
        if not TECHY[numerTechu+2].stopien > -1 and GRACZ.procki >= TECHY[numerTechu+2].cenaBadania:
            buttonZbadaj3.render(okno,765,155,100,40)
            if buttonZbadaj3.clik():
                TECHY[numerTechu+2].zbadaj(GRACZ)

        if TECHY[numerTechu+2].stopien >-1 and TECHY[numerTechu+2].stopien == 0 and GRACZ.kasa >= TECHY[numerTechu+2].cena1:
            buttonKup31.render(okno,765,250,100,40)
            if buttonKup31.clik():
                TECHY[numerTechu+2].kup(GRACZ)

        if TECHY[numerTechu+2].stopien > -1 and TECHY[numerTechu+2].stopien == 1 and GRACZ.kasa >= TECHY[numerTechu+2].cena2 and TECHY[numerTechu+2].stopien == 1:
            buttonKup32.render(okno,765,345,100,40)
            if buttonKup32.clik():
                TECHY[numerTechu+2].kup(GRACZ)

        okno.blit(fontMala.render("PROCKI:         " + str(GRACZ.procki), True, BIALY), (20, 480))
        okno.blit(fontMala.render("KASA:           " + str(GRACZ.kasa) + " $", True, BIALY), (20, 500))

    #wybór misji
    if FAZA == 1:
        okno.blit(fontNazwyFaz.render("Wybierz i rozpocznij misję",True,BIALY),(50,10))
        for i in range(3):
            okno.blit(DOSTEPNE_MISJE[i].wyswietlInfo(),(200+210*i,100))
            if pygame.Rect(200+210*i,100,200,300).collidepoint(myszPozycja):
                pygame.draw.rect(okno,CZERWONY,(200+210*i,100,200,300),4)
            if pygame.Rect(200 + 210 * i, 100, 200, 300).collidepoint(myszPozycja) and myszKlik[0] and pygame.time.get_ticks() - czasKlik > 500:
                AKTUALNA_MISJA = DOSTEPNE_MISJE[i]
                czasKlik = pygame.time.get_ticks()
                wybranoMisje = True
                numerWybranejMisji = i+1
        if wybranoMisje:
            okno.blit(fontNazwyFaz.render("Wybrałeś misję numer: " + str(numerWybranejMisji), True, BIALY), (250, 400))

        okno.blit(fontMala.render("PROCKI:         " + str(GRACZ.procki), True, BIALY), (20, 480))
        okno.blit(fontMala.render("KASA:           " + str(GRACZ.kasa) + " $", True, BIALY), (20, 500))

        #okno.blit(fontMala.render("Twoja kasa: " + str(GRACZ.kasa) + "$", True, BIALY), (50, 500))
        button.render(okno,785,WYSOKOSC-100,180,50)
        buttonBaza.render(okno,50,WYSOKOSC-100,180,50)
        if buttonBaza.clik():
            FAZA = 5
            buttonKONIEC.time = pygame.time.get_ticks()
            muzykaMENU.set_volume(0.2)
        button1.render(okno,720,20,250,50)

        if button.clik() and wybranoMisje:
            muzykaMENU.stop()
            FAZA = 3
            czasOdliczania = pygame.time.get_ticks()
            odliczanie = 3
            misjaWykonana = False
            y_fabrykatora = 0

        if button1.clik() and GRACZ.kasa > 99:
            wybranoMisje = False
            numerWybranejMisji = 0
            DOSTEPNE_MISJE.clear()
            DOSTEPNE_MISJE = losujNoweMisje(GRACZ.wykonaneMisje)
            GRACZ.kasa -= 100
    #odliczanie
    if FAZA == 3:
        napis = fontOdliczanie.render(str(odliczanie), True, BIALY)
        okno.blit(napis,(400,150))
        if pygame.time.get_ticks() - czasOdliczania > 750:
            czasOdliczania = pygame.time.get_ticks()
            odliczanie-=1

        if odliczanie == 0:
            FAZA = 2
            ENEMY = AKTUALNA_MISJA.inicjujWrogow(TRUDNOSC)
            RODZAJ_MISJI = AKTUALNA_MISJA.rodzaj
            GRACZ.ustawPodMisje(RODZAJ_MISJI)
            RAKIETY.clear()
            RAKIETY_ENEMY.clear()
            LASERY.clear()
            PROCKI.clear()
            LASERY_ENEMY.clear()
            ZLOMY.clear()
            WYBUCHY.clear()
            if RODZAJ_MISJI == 3:
                MUZYKA = muzyka2
            if RODZAJ_MISJI == 1 or RODZAJ_MISJI == 4:
                MUZYKA = muzyka1
            if RODZAJ_MISJI == 2:
                MUZYKA = muzyka3

            KONIEC_MISJI = False
            wybranoMisje = False
    #podsumowanie misji
    if FAZA == 4:
        MUZYKA.stop()
        MUZA = False
        RAKIETY.clear()
        RAKIETY_ENEMY.clear()
        LASERY.clear()
        PROCKI.clear()
        LASERY_ENEMY.clear()
        ZLOMY.clear()
        WYBUCHY.clear()
        if misjaWykonana:
            okno.blit(fontNazwyFaz.render("Misja zakończona sukcesem! ", True, BIALY), (150, 2))
        else:
            okno.blit(fontNazwyFaz.render("Misja zakończona porażką... ", True, BIALY), (150, 2))


        y = 90
        okno.blit(fontMala.render("STATYSTYKI MISJI: ", True, BIALY), (6, y))
        okno.blit(fontMala.render("STRZAŁY LASEREM: " + str(GRACZ.strzalyMisja), True, BIALY), (30, y+30))
        okno.blit(fontMala.render("TRAIONE: " + str(GRACZ.trafioneMisja), True, BIALY), (30, y+60))
        if GRACZ.trafioneMisja > 0:
            okno.blit(fontMala.render("PROCENT TRAFIEŃ: " + str(round((GRACZ.trafioneMisja*100)/GRACZ.strzalyMisja,1)) + " %", True, BIALY), (30, y+90))
        else:
            okno.blit(fontMala.render("PROCENT TRAFIEŃ: 0" , True, BIALY), (30, y+90))
        okno.blit(fontMala.render("ZEBRANY ZŁOM: " + str(GRACZ.zlomMisja), True, BIALY),(30, y+120))
        okno.blit(fontMala.render("SPRZEDANY ZŁOM: " + str(GRACZ.aktualnyZlom) + " * " + str(GRACZ.cenaZlomu) + " = " + str(GRACZ.aktualnyZlom*GRACZ.cenaZlomu)+" $", True, BIALY),(30, y+150))
        okno.blit(fontMala.render("ZDOBYTA KASA: " + str(AKTUALNA_MISJA.naroda) + " $", True, BIALY),(30, y+180))
        okno.blit(fontMala.render("POKONANYCH PRZECIWNIKÓW: " + str(sum(GRACZ.zniszczoneMisja)), True, BIALY),(30, y + 210))
        if misjaWykonana:
            okno.blit(fontMala.render("Zdobyte PROCKI: " + str(GRACZ.prockiMisja), True, BIALY), (30, WYSOKOSC-130))
            okno.blit(fontMala.render("Twoja nagroda: za misję ("+ str(AKTUALNA_MISJA.naroda)+"$) + za złom ("+ str(GRACZ.cenaZlomu * GRACZ.aktualnyZlom)+ "$) = " + str(GRACZ.cenaZlomu * GRACZ.aktualnyZlom+ AKTUALNA_MISJA.naroda) + "$", True, BIALY),(30, WYSOKOSC-100))
            okno.blit(fontMala.render("KASA: " + str(GRACZ.kasa+AKTUALNA_MISJA.naroda+GRACZ.cenaZlomu * GRACZ.aktualnyZlom)+ "$" , True, BIALY),(30, WYSOKOSC - 70))
        else:
            okno.blit(fontMala.render("KASA: " + str(GRACZ.kasa)+ "$", True, BIALY),(30, WYSOKOSC - 50))
        buttonBaza.render(okno,785,WYSOKOSC-100,180,50)

        if buttonBaza.clik():
            muzykaMENU.play()
            if misjaWykonana:
                GRACZ.kasa += (AKTUALNA_MISJA.naroda + GRACZ.cenaZlomu * GRACZ.aktualnyZlom)
                GRACZ.kasaAll += (AKTUALNA_MISJA.naroda + GRACZ.cenaZlomu * GRACZ.aktualnyZlom)
                if AKTUALNA_MISJA.naroda + GRACZ.cenaZlomu * GRACZ.aktualnyZlom > 1000:
                    GRACZ.gwiazdy[26].zalicz()
                if ((GRACZ.trafioneMisja*100)/GRACZ.strzalyMisja) > 75:
                    GRACZ.gwiazdy[27].zalicz()
                if ((GRACZ.trafioneMisja*100)/GRACZ.strzalyMisja) > 90:
                    GRACZ.gwiazdy[28].zalicz()
                if GRACZ.wykonaneObrony > 4:
                    GRACZ.gwiazdy[29].zalicz()
                if GRACZ.wykonanePoscigi > 4:
                    GRACZ.gwiazdy[30].zalicz()
                if GRACZ.wykonaneSzwadrony > 4:
                    GRACZ.gwiazdy[31].zalicz()
                if GRACZ.wykonaneFabrykatory > 4:
                    GRACZ.gwiazdy[32].zalicz()
                if GRACZ.wykonaneObrony > 14:
                    GRACZ.gwiazdy[33].zalicz()
                if GRACZ.wykonanePoscigi > 14:
                    GRACZ.gwiazdy[34].zalicz()
                if GRACZ.wykonaneSzwadrony > 14:
                    GRACZ.gwiazdy[35].zalicz()
                if GRACZ.wykonaneFabrykatory > 14:
                    GRACZ.gwiazdy[36].zalicz()

            FAZA = 5
            GRA_ZAPISANA = False
            buttonKONIEC.time = pygame.time.get_ticks()
            buttonMENU.time = pygame.time.get_ticks()
            DOSTEPNE_MISJE.clear()
            DOSTEPNE_MISJE = losujNoweMisje(GRACZ.wykonaneMisje)
            button.time = pygame.time.get_ticks()
            #weryfikacja gwiazdek
            GRACZ.zaktualizujGwiazdy()




        wyswietlStatystykeZniszczonych(GRACZ.zniszczone,GRACZ.zniszczoneMisja,True)
    #misje

    if FAZA == 2:
        if not MUZA:
            if AKTUALNA_MISJA.rodzaj == 4:
                MUZYKA = muzyka2
            MUZYKA.play(-1)
            MUZA = True

        if RODZAJ_MISJI == 1:
            okno.blit(tlo1,(0,0))
        if RODZAJ_MISJI == 2:
            okno.blit(tlo4,(0,0))
            if AKTUALNA_MISJA.beczki[0] == 1:
                okno.blit(grafikaFabrykaLewa,(250,0))
            okno.blit(grafikaFabryka,(337,y_fabrykatora))
            if AKTUALNA_MISJA.beczki[1] == 1:
                okno.blit(grafikaFabrykaPrawa,(687,0))
            if AKTUALNA_MISJA.beczki.count(0) == 2 and AKTUALNA_MISJA.iloscWiez == 0:
                y_fabrykatora+=1
        if RODZAJ_MISJI == 3:
            okno.blit(tlo2,(0,0))
        if RODZAJ_MISJI == 4:
            okno.blit(tlo3,(0,0))
        pygame.draw.line(okno,CZARNY,(0,550),(SZEROKOSC,550),4)


        if RODZAJ_MISJI == 2 and CZAS_GRY % 7 == 0 and pygame.time.get_ticks() - czasRespienia > 1100 and (AKTUALNA_MISJA.beczki[0] == 1 or AKTUALNA_MISJA.beczki[1] == 1):
            czasRespienia = pygame.time.get_ticks()
            produkcjaFabrykaD.play()
            if random.randint(1,100) < 50:
                if AKTUALNA_MISJA.wiodacyPrzeciwnik in (1, 2, 3):
                    AKTUALNA_MISJA.przeciwnicy.append(Enemy(RODZAJ_MISJI))
                elif AKTUALNA_MISJA.wiodacyPrzeciwnik in (4, 5):
                    AKTUALNA_MISJA.przeciwnicy.append(EnemyMysliwiec(RODZAJ_MISJI))
                elif AKTUALNA_MISJA.wiodacyPrzeciwnik in (6, 7):
                    AKTUALNA_MISJA.przeciwnicy.append(EnemyKanonierka(RODZAJ_MISJI))
                elif AKTUALNA_MISJA.wiodacyPrzeciwnik in (8, 9):
                    AKTUALNA_MISJA.przeciwnicy.append(EnemyScigacz(RODZAJ_MISJI))
                elif AKTUALNA_MISJA.wiodacyPrzeciwnik == 10:
                    AKTUALNA_MISJA.przeciwnicy.append(EnemyKanonierka(RODZAJ_MISJI))
                elif AKTUALNA_MISJA.wiodacyPrzeciwnik >= 11:
                    AKTUALNA_MISJA.przeciwnicy.append(EnemyPancernik(RODZAJ_MISJI))

            czasRespienia = pygame.time.get_ticks()

        dopalacz1.render(okno,myszPozycja)
        numerTrafionegoRakieta = -1
        for rakieta in RAKIETY:
            for enemy in ENEMY:
                if rakieta.getRect().colliderect(enemy.getRect()):
                    numerTrafionegoRakieta = ENEMY.index(enemy)
                    if (not AKTUALNA_MISJA.trwaPoscig and RODZAJ_MISJI ==3) or RODZAJ_MISJI !=3  :
                        if enemy.rodzaj == 9 and enemy.odpornosc == 1 and GRACZ.wirus > 0:
                            enemy.odpornosc = 0
                        if enemy.rodzaj == 13 and enemy.odpornosc == 2 and GRACZ.wirus > 0:
                            enemy.odpornosc = 0
                        if enemy.rodzaj in [6,8,10,14,15]:
                            if enemy.oslona:
                                enemy.oslona = False
                                enemy.czasOslony = pygame.time.get_ticks()
                            else:
                                enemy.hit(rakieta.moc)
                        else:
                            enemy.hit(rakieta.moc)

                        rakieta.jest = False
                        wybuchRakietyD.play()
                        if enemy.hp <= 0:
                            if enemy.rodzaj in [9,10,13]:
                                WYBUCHY.append(Wybuch(enemy.x - 50, enemy.y - 50,3))
                            elif enemy.rodzaj in [12,14]:
                                if enemy.rodzaj == 14:
                                    ENEMY.append(Enemy(RODZAJ_MISJI,enemy.x+60,enemy.y+60))
                                    ENEMY.append(Enemy(RODZAJ_MISJI,enemy.x+60,enemy.y+60))
                                    ENEMY.append(Enemy(RODZAJ_MISJI,enemy.x+60,enemy.y+60))
                                    ENEMY.append(EnemyMysliwiec(RODZAJ_MISJI,enemy.x+60,enemy.y+60))
                                    ENEMY.append(EnemyMysliwiec(RODZAJ_MISJI,enemy.x+60,enemy.y+60))
                                    ENEMY.append(EnemyScigacz(RODZAJ_MISJI,enemy.x+60,enemy.y+60))
                                WYBUCHY.append(Wybuch(enemy.x - 50, enemy.y - 50, 3))
                                WYBUCHY.append(Wybuch(enemy.x - 25, enemy.y + 50, 3))
                                WYBUCHY.append(Wybuch(enemy.x, enemy.y + 75, 3))
                            else:
                                WYBUCHY.append(Wybuch(enemy.x - 50, enemy.y - 50,1))
                            wybuchD.play()
                            generujZlom(enemy, ZLOMY,PROCKI)
                            GRACZ.zniszczone[enemy.rodzaj] += 1
                            GRACZ.zniszczoneMisja[enemy.rodzaj] += 1
                        if not enemy.jest:
                            if enemy.rodzaj == 11:
                                AKTUALNA_MISJA.iloscWiez -= 1
                            if enemy.rodzaj == 12 and enemy.x == 300:
                                AKTUALNA_MISJA.beczki[0] = 0
                            if enemy.rodzaj == 12 and enemy.x == 695:
                                AKTUALNA_MISJA.beczki[1] = 0
                            ENEMY.remove(enemy)
                    elif AKTUALNA_MISJA.trwaPoscig and enemy.rodzaj == 5:
                            enemy.hit(rakieta.moc)
                            rakieta.jest = False
                            wybuchRakietyD.play()
                            if not enemy.jest:
                                WYBUCHY.append(Wybuch(enemy.x - 50, enemy.y - 50, 1))
                                ENEMY.remove(enemy)

        for rakieta in RAKIETY:
            rakieta.update(okno,RODZAJ_MISJI)
            if not rakieta.jest:
                WYBUCHY.append(Wybuch(rakieta.getRect().topleft[0]-20,rakieta.getRect().topleft[1]-20,2))
                if GRACZ.glowica > 0 and rakieta.x < SZEROKOSC and rakieta.y > 0:
                    pygame.draw.circle(okno, CZERWONY, (rakieta.x, rakieta.y), GRACZ.glowica, 4)
                    for enemy in ENEMY:
                        if ENEMY.index(enemy) != numerTrafionegoRakieta:
                            odleglosc = obliczOdleglosc(rakieta.x, rakieta.y, enemy.getRect().centerx,enemy.getRect().centery)
                            if odleglosc <= GRACZ.glowica:
                                obrazenia = GRACZ.mocRakiet * 0.01 * ((odleglosc * 100) // GRACZ.glowica)
                                if enemy.rodzaj in [6, 8, 10, 14, 15]:
                                    if enemy.oslona:
                                        enemy.oslona = False
                                        enemy.czasOslony = pygame.time.get_ticks()
                                else:
                                    enemy.hit(int(obrazenia))
                            if enemy.hp <= 0:
                                if enemy.rodzaj in [9, 10, 13]:
                                    WYBUCHY.append(Wybuch(enemy.x - 50, enemy.y - 50, 3))
                                elif enemy.rodzaj in [12,14]:
                                    if enemy.rodzaj == 14:
                                        ENEMY.append(Enemy(RODZAJ_MISJI, enemy.x + 60, enemy.y + 60))
                                        ENEMY.append(Enemy(RODZAJ_MISJI, enemy.x + 60, enemy.y + 60))
                                        ENEMY.append(Enemy(RODZAJ_MISJI, enemy.x + 60, enemy.y + 60))
                                        ENEMY.append(EnemyMysliwiec(RODZAJ_MISJI, enemy.x + 60, enemy.y + 60))
                                        ENEMY.append(EnemyMysliwiec(RODZAJ_MISJI, enemy.x + 60, enemy.y + 60))
                                        ENEMY.append(EnemyScigacz(RODZAJ_MISJI, enemy.x + 60, enemy.y + 60))
                                    WYBUCHY.append(Wybuch(enemy.x - 50, enemy.y - 50, 3))
                                    WYBUCHY.append(Wybuch(enemy.x - 25, enemy.y + 50, 3))
                                    WYBUCHY.append(Wybuch(enemy.x, enemy.y + 75, 3))
                                else:
                                    WYBUCHY.append(Wybuch(enemy.x - 50, enemy.y - 50, 1))
                                wybuchD.play()
                                generujZlom(enemy, ZLOMY, PROCKI)
                                GRACZ.zniszczone[enemy.rodzaj] += 1
                                GRACZ.zniszczoneMisja[enemy.rodzaj] += 1
                            if not enemy.jest:
                                if enemy.rodzaj == 11:
                                    AKTUALNA_MISJA.iloscWiez -= 1
                                if enemy.rodzaj == 12 and enemy.x == 300:
                                    AKTUALNA_MISJA.beczki[0] = 0
                                if enemy.rodzaj == 12 and enemy.x == 695:
                                    AKTUALNA_MISJA.beczki[1] = 0
                                ENEMY.remove(enemy)
                RAKIETY.remove(rakieta)



        GRACZ.update(okno,RODZAJ_MISJI,klawisze,myszKlik,myszPozycja,LASERY,RAKIETY)
        for laser in LASERY:
            laser.update(okno,RODZAJ_MISJI)
            if not laser.jest:
                LASERY.remove(laser)

#obrazenia PLANETY (tylko obrona planety)
        for laserE in LASERY_ENEMY:
            laserE.update(okno,RODZAJ_MISJI)
            if RODZAJ_MISJI == 1 and laserE.y + laserE.wysokosc > WYSOKOSC - 100:
                AKTUALNA_MISJA.aktualnehpPlanety-=1
            if not laserE.jest:
                LASERY_ENEMY.remove(laserE)

        for rakietaE in RAKIETY_ENEMY:
            rakietaE.update(okno,RODZAJ_MISJI)
            if rakietaE.getRect().colliderect(GRACZ.getRect()):
                WYBUCHY.append(Wybuch(rakietaE.x, rakietaE.y, 2))
                wybuchD.play()
                rakietaE.jest = False
                if GRACZ.oslona:
                    GRACZ.oslona = False
                    GRACZ.czasOslony = pygame.time.get_ticks()
                else:
                    GRACZ.hit(rakietaE.moc)
            if not rakietaE.jest:
                RAKIETY_ENEMY.remove(rakietaE)


        for zlom in ZLOMY:
            zlom.update(okno)
            if GRACZ.aktualnyZlom < GRACZ.maxZlom and obliczOdleglosc(zlom.x,zlom.y,GRACZ.x+GRACZ.szerokosc//2,GRACZ.y+GRACZ.wysokosc//2) <= GRACZ.zasiegMagnesu:
                if zlom.y > GRACZ.y + GRACZ.wysokosc//2:
                    zlom.dy -= 0.05
                else:
                    zlom.dy += 0.05
                if zlom.x > GRACZ.x + GRACZ.szerokosc//2:
                    zlom.dx-= 0.07
                else:
                    zlom.dx += 0.07
            if not zlom.jest:
                ZLOMY.remove(zlom)


        for procek in PROCKI:
            procek.update(okno)
            if procek.getRect().colliderect(GRACZ.getRect()):
                procekD.play()
                procek.jest = False
                GRACZ.procki += 1
                GRACZ.prockiAll += 1
                GRACZ.prockiMisja +=1

            if not procek.jest:
                PROCKI.remove(procek)


        for zlom in ZLOMY:
            if zlom.getRect().colliderect(GRACZ.getRect()) and GRACZ.aktualnyZlom < GRACZ.maxZlom:
                zlom.jest = False
                GRACZ.aktualnyZlom += 1
                GRACZ.zlomAll += 1
                GRACZ.zlomMisja += 1
                zlomD.play()
            if not zlom.jest:
                ZLOMY.remove(zlom)

        for laserE in LASERY_ENEMY:
            if laserE.getRect().colliderect(GRACZ.getRect()):
                laserE.jest = False
                hitD.play()
                LASERY_ENEMY.remove(laserE)
                GRACZ.hit(laserE.moc)


        for enemy in ENEMY:
            if enemy.rodzaj == 11:
                enemy.obliczKat(GRACZ)
            if RODZAJ_MISJI == 3 and not AKTUALNA_MISJA.trwaPoscig and enemy.rodzaj == 5:
                ENEMY.remove(enemy)
            if RODZAJ_MISJI == 3 and AKTUALNA_MISJA.trwaPoscig and AKTUALNA_MISJA.aktualnyStanPoscigu < AKTUALNA_MISJA.dystansPoscigu:
                if pygame.time.get_ticks() - czasPoscigu > 1000:
                    czasPoscigu = pygame.time.get_ticks()
                    AKTUALNA_MISJA.aktualnyStanPoscigu += GRACZ.dx
                if AKTUALNA_MISJA.aktualnyStanPoscigu >= AKTUALNA_MISJA.dystansPoscigu:
                    AKTUALNA_MISJA.trwaPoscig = False
                    enemy.czas = pygame.time.get_ticks()
                    enemy.czasStrzalu = pygame.time.get_ticks()
                    if enemy.rodzaj == 8:
                        enemy.czasOslony = pygame.time.get_ticks()
                if enemy.rodzaj == 5:
                    enemy.update(okno,ENEMY,LASERY_ENEMY,RAKIETY_ENEMY,RODZAJ_MISJI)
            else:
                enemy.update(okno,ENEMY,LASERY_ENEMY,RAKIETY_ENEMY,RODZAJ_MISJI)
                if enemy.rodzaj == 7 and enemy.y + enemy.wysokosc > 545:
                    AKTUALNA_MISJA.aktualnehpPlanety -= 10
                    if not enemy.jest:
                        ENEMY.remove(enemy)

        for laser in LASERY:
            for enemy in ENEMY:
                if RODZAJ_MISJI == 3 and AKTUALNA_MISJA.trwaPoscig and enemy.rodzaj == 5 and laser.getRect().colliderect(enemy.getRect()):
                    hitD.play()
                    enemy.hit(laser.moc)
                    laser.jest = False
                    GRACZ.trafioneAll += 1
                    GRACZ.trafioneMisja += 1
                    if enemy.hp <= 0:
                        if enemy.rodzaj in [9, 10, 13]:
                            WYBUCHY.append(Wybuch(enemy.x - 50, enemy.y - 50, 3))
                        elif enemy.rodzaj == 14:
                            ENEMY.append(Enemy(RODZAJ_MISJI, enemy.x + 60, enemy.y + 60))
                            ENEMY.append(Enemy(RODZAJ_MISJI, enemy.x + 60, enemy.y + 60))
                            ENEMY.append(Enemy(RODZAJ_MISJI, enemy.x + 60, enemy.y + 60))
                            ENEMY.append(EnemyMysliwiec(RODZAJ_MISJI, enemy.x + 60, enemy.y + 60))
                            ENEMY.append(EnemyMysliwiec(RODZAJ_MISJI, enemy.x + 60, enemy.y + 60))
                            ENEMY.append(EnemyScigacz(RODZAJ_MISJI, enemy.x + 60, enemy.y + 60))
                            WYBUCHY.append(Wybuch(enemy.x - 50, enemy.y - 50, 3))
                            WYBUCHY.append(Wybuch(enemy.x - 25, enemy.y + 50, 3))
                            WYBUCHY.append(Wybuch(enemy.x, enemy.y + 75, 3))
                        else:
                            WYBUCHY.append(Wybuch(enemy.x - 50, enemy.y - 50, 1))
                        wybuchD.play()
                        enemy.y = SZEROKOSC + 200

                if RODZAJ_MISJI != 3 or (RODZAJ_MISJI == 3 and not AKTUALNA_MISJA.trwaPoscig):
                    if laser.getRect().colliderect(enemy.getRect()):
                        if enemy.odpornosc == 0:
                            hitD.play()
                            enemy.hit(laser.moc)
                        if enemy.odpornosc == 1:
                            laserOdbityD.play()
                        if enemy.odpornosc == 2:
                            laserOdbityD.play()
                            if AKTUALNA_MISJA.rodzaj in (1,2):
                                LASERY_ENEMY.append(Laser(laser.x,laser.y,0,5,0,AKTUALNA_MISJA.rodzaj,laser.moc))
                            if AKTUALNA_MISJA.rodzaj in (3,4):
                                LASERY_ENEMY.append(Laser(laser.x,laser.y,-5,0,-90,AKTUALNA_MISJA.rodzaj,laser.moc))
                        laser.jest = False
                        GRACZ.trafioneAll += 1
                        GRACZ.trafioneMisja += 1
                        if enemy.hp <= 0:
                            if enemy.rodzaj in [9, 10,13]:
                                WYBUCHY.append(Wybuch(enemy.x - 50, enemy.y - 50, 3))
                            elif enemy.rodzaj in [12,14]:
                                if enemy.rodzaj == 14:
                                    ENEMY.append(Enemy(RODZAJ_MISJI, enemy.x + 60, enemy.y + 60))
                                    ENEMY.append(Enemy(RODZAJ_MISJI, enemy.x + 60, enemy.y + 60))
                                    ENEMY.append(EnemyMysliwiec(RODZAJ_MISJI, enemy.x + 60, enemy.y + 60))
                                    ENEMY.append(EnemyMysliwiec(RODZAJ_MISJI, enemy.x + 60, enemy.y + 60))
                                    ENEMY.append(EnemyScigacz(RODZAJ_MISJI, enemy.x + 60, enemy.y + 60))

                                WYBUCHY.append(Wybuch(enemy.x - 50, enemy.y - 50, 3))
                                WYBUCHY.append(Wybuch(enemy.x - 25, enemy.y + 50, 3))
                                WYBUCHY.append(Wybuch(enemy.x , enemy.y + 75, 3))
                            else:
                                WYBUCHY.append(Wybuch(enemy.x - 50, enemy.y - 50, 1))
                            wybuchD.play()
                            generujZlom(enemy,ZLOMY,PROCKI)
                            GRACZ.zniszczone[enemy.rodzaj] += 1
                            GRACZ.zniszczoneMisja[enemy.rodzaj] += 1
                        if not enemy.jest:
                            if enemy.rodzaj == 11:
                                AKTUALNA_MISJA.iloscWiez -= 1
                            if enemy.rodzaj == 12 and enemy.x == 300:
                                AKTUALNA_MISJA.beczki[0] = 0
                            if enemy.rodzaj == 12 and enemy.x == 695:
                                AKTUALNA_MISJA.beczki[1] = 0
                            ENEMY.remove(enemy)

        for wybuch in WYBUCHY:
            wybuch.update(okno)
            if not wybuch.jest:
                WYBUCHY.remove(wybuch)

        for enemy in ENEMY:
            if enemy.getRect().colliderect(GRACZ.getRect()):
                if (RODZAJ_MISJI == 3 and AKTUALNA_MISJA.trwaPoscig and enemy.rodzaj == 5) or (RODZAJ_MISJI == 3 and not AKTUALNA_MISJA.trwaPoscig and enemy.rodzaj != 5) or RODZAJ_MISJI != 3:
                    WYBUCHY.append(Wybuch(enemy.getRect().topleft[0],enemy.getRect().topleft[1], 2))
                    wybuchD.play()
                    if GRACZ.oslona:
                        GRACZ.oslona = False
                        GRACZ.czasOslony = pygame.time.get_ticks()
                    else:
                        GRACZ.hit(100)
                    if enemy.rodzaj in [6, 8, 10,14, 15]:
                        if enemy.oslona:
                            enemy.oslona = False
                            enemy.czasOslony = pygame.time.get_ticks()
                        else:
                            enemy.hit(300)
                    else:
                        enemy.hit(300)

                if enemy.hp <= 0:
                    if enemy.rodzaj == 11:
                        AKTUALNA_MISJA.iloscWiez -= 1


                    GRACZ.zniszczone[enemy.rodzaj] += 1
                    ENEMY.remove(enemy)





        if RODZAJ_MISJI == 1:
            pasek(okno,800,10,25,180,AKTUALNA_MISJA.hpPlanety,AKTUALNA_MISJA.aktualnehpPlanety,BIALY)
            okno.blit(fontMniejsza.render("PLANETA " + str(AKTUALNA_MISJA.hpPlanety)+"/"+str(AKTUALNA_MISJA.aktualnehpPlanety),True,'black'),(810,11))
        if RODZAJ_MISJI == 3 and AKTUALNA_MISJA.trwaPoscig:
            pasek(okno, 800, 10, 25, 180, AKTUALNA_MISJA.dystansPoscigu, AKTUALNA_MISJA.aktualnyStanPoscigu, BIALY,(0,255,0))
            okno.blit(fontMniejsza.render("POŚCIG " + str(AKTUALNA_MISJA.dystansPoscigu) + "/" + str(AKTUALNA_MISJA.aktualnyStanPoscigu), True,'black'), (810, 11))
        if RODZAJ_MISJI == 4:
            jestPrzewodnik = False
            for enemy in ENEMY:
                if enemy.rodzaj == 10:
                    jestPrzewodnik = True

            pasek(okno, 800, 10, 25, 180, AKTUALNA_MISJA.czasDoUcieczki, AKTUALNA_MISJA.aktualnyCzasDoUcieczki, BIALY,(0,255,0))
            okno.blit(fontMniejsza.render("CZAS SKOKU: " + str(AKTUALNA_MISJA.czasDoUcieczki//1000) + "/" + str(AKTUALNA_MISJA.aktualnyCzasDoUcieczki//1000), True,'black'), (810, 11))
            if pygame.time.get_ticks() - AKTUALNA_MISJA.czasUcieczki > 1000 and jestPrzewodnik:
                AKTUALNA_MISJA.czasUcieczki = pygame.time.get_ticks()
                AKTUALNA_MISJA.aktualnyCzasDoUcieczki -= 1000

        if not KONIEC_MISJI and len(ENEMY) == 0 or (not KONIEC_MISJI and RODZAJ_MISJI == 2 and AKTUALNA_MISJA.iloscWiez == 0 and AKTUALNA_MISJA.beczki[0] == 0 and AKTUALNA_MISJA.beczki[1] == 0):
            KONIEC_MISJI = True
            czasKoniec = pygame.time.get_ticks()
            if RODZAJ_MISJI == 1 and AKTUALNA_MISJA.hpPlanety > 0 and GRACZ.hp:
                GRACZ.wykonaneMisje += 1
                GRACZ.wykonaneObrony += 1
                misjaWykonana = True
            if RODZAJ_MISJI == 2 and GRACZ.hp:
                GRACZ.wykonaneMisje += 1
                GRACZ.wykonanePoscigi += 1
                misjaWykonana = True
            if (RODZAJ_MISJI == 3) and GRACZ.hp > 0:
                GRACZ.wykonaneMisje += 1
                GRACZ.wykonaneSzwadrony += 1
                misjaWykonana = True
            if (RODZAJ_MISJI == 4):
                GRACZ.wykonaneMisje += 1
                GRACZ.wykonaneFabrykatory += 1
                misjaWykonana = True

        if GRACZ.hp <= 0 and not KONIEC_MISJI:
            KONIEC_MISJI = True
            czasKoniec = pygame.time.get_ticks()
            GRACZ.aktualnyZlom = 0
            WYBUCHY.append(Wybuch(GRACZ.x+GRACZ.grafika.get_width()//2, GRACZ.y+GRACZ.grafika.get_height()//2, 2))
            wybuchD.play()

        if GRACZ.hp <= 0:
            GRACZ.y +=3
            GRACZ.oslona = False
            GRACZ.czasOslony = pygame.time.get_ticks()
            GRACZ.kat +=10

        if RODZAJ_MISJI == 4 and AKTUALNA_MISJA.aktualnyCzasDoUcieczki <= 0:
            KONIEC_MISJI = True
            czasKoniec = pygame.time.get_ticks()
            ENEMY.clear()

        if RODZAJ_MISJI == 2 and KONIEC_MISJI and pygame.time.get_ticks() - czasKoniec > 6000 and GRACZ.hp > 0 and len(PROCKI) == 0:
            FAZA = 4

        if KONIEC_MISJI and pygame.time.get_ticks() - czasKoniec > 3000 and GRACZ.hp <= 0:
            FAZA = 4

        if KONIEC_MISJI and pygame.time.get_ticks() - czasKoniec > 6000 and len(ZLOMY) == 0:
            FAZA = 4

        if AKTUALNA_MISJA.aktualnehpPlanety <= 0 and pygame.time.get_ticks() - czasKoniec > 5000:
            FAZA = 4

# NA DOLE

    #rakiety





    pygame.display.update()

pygame.quit()
