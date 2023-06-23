import pygame
import math
from random import randint
from random import choice
from Laser import Laser
from Rakieta import Rakieta
from Pasek import pasek
SZEROKOSC = 1000
WYSOKOSC = 550

class Gracz:
    x = 0
    y = 0
    dx= 0
    dy = 0
    hp = 0
    maxHP = 0
    liczbaWykonanychMisji = 0
    aktualnyZlom = 0
    maxZlom = 0
    zasiegMagnesu = 0
    rakietyMax = 0
    aktualneRakiety = 0
    szybkoscRakiet = 3
    maxTemperatura = 0
    aktualnaTemperatura = 0
    oryginalnaGrafika = pygame.image.load("Grafika\Gracz\\gracz.png")
    oslonaG = pygame.image.load("Grafika\spr_shield.png")
    oslonaG.set_colorkey('white')
    grafika = oryginalnaGrafika
    pygame.mixer.init()
    laserD = pygame.mixer.Sound("Dzwieki\Laser_09.wav")
    alarmTemperaturyD = pygame.mixer.Sound("Dzwieki\\alarm.ogg")
    rakietaD = pygame.mixer.Sound("Dzwieki\sfx_sounds_falling11.wav")
    oslonaD = pygame.mixer.Sound("Dzwieki\sfx_sounds_interaction20.wav")
    laserD.set_volume(0.1)
    iloscLaserow = 1
    grafika.set_colorkey('white')
    szerokosc = grafika.get_width()
    wysokosc = grafika.get_height()
    przegrzanie = False
    czasLaseru = 0
    czasRakiety = 0
    czasTemperatury = 0
    czasPrzegrzania = 0
    czasMiedzyLaserami = 0
    czasOslony = 0
    font = 0
    kasa = 0
    kosztNaprawy = 3
    cenaZlomu = 10
    czasOdnawianiaOslony = 10000
    oslona = False
    zbadalOslone = True
    procki = 0
    mocLaseru = 10
    wirus = 0
    kat = 0


    #statystyki
    strzalyAll = 0
    strzalyMisja = 0
    trafioneAll = 0
    trafioneMisja = 0
    zniszczone = []
    zniszczoneMisja = []
    wykonaneMisje = 0
    zlomMisja = 0
    zlomAll = 0
    kasaAll = 0
    prockiAll = 0
    prockiMisja = 0
    __cecha = 0


    def __init__(self,numer,rodzajMisji, TRUDNOSC,hp = None, maxHP = None,maxZlomu = None,zasiegMagnezu = None,rakietyMax = None, szybkoscTakiet = None, maxTemperatura = None, iloscLaserow = None, kosztNaprawy = None, cenaZlomu = None,mocLaseru = None, czasOdnawianiaOslony = None, kasa = None,procki = None, liczbaWykonanychMisji =None,strzalyAll = None,trafioneAll = None,kasaAll = None, prockiAll = None,wirus =None):
        if numer == 1:
            if rodzajMisji in [1,2]:
                self.x = SZEROKOSC//2
                self.y = 470
            if rodzajMisji in [3,4]:
                self.x = 100
                self.y = WYSOKOSC//2
                kopia = pygame.transform.rotate(self.grafika, -90)
                kopia.set_colorkey('white')
                self.grafika = kopia
                self.szerokosc = self.grafika.get_width()
                self.wysokosc = self.grafika.get_height()

            self.__cecha = 10
            self.dx = 3
            self.dy = 3
            if mocLaseru == None:
                self.mocLaseru = 10
            else:
                self.mocLaseru = mocLaseru
            self.wirus = 0
            if szybkoscTakiet == None:
                self.szybkoscRakiet = 3
            else:
                self.szybkoscRakiet = szybkoscTakiet
            self.czasMiedzyLaserami = 200
            self.czasLaseru = pygame.time.get_ticks()
            self.czasTemperatury = pygame.time.get_ticks()
            self.czasPrzegrzania = pygame.time.get_ticks()
            self.czasOslony = pygame.time.get_ticks()
            if czasOdnawianiaOslony == None:
                self.czasOdnawianiaOslony = 10000
            else:
                self.czasOdnawianiaOslony = czasOdnawianiaOslony
            self.oslona = False
            if maxHP == None:
                self.maxHP = 200
            else:
                self.maxHP = maxHP
            if hp == None:
                self.hp = self.maxHP
            else:
                self.hp = hp
            self.aktualnyZlom = 0
            if maxZlomu == None:
                self.maxZlom = 15
            else:
                self.maxZlom = maxZlomu
            if zasiegMagnezu == None:
                self.zasiegMagnesu = 200
            else:
                self.zasiegMagnesu = zasiegMagnezu
            if rakietyMax == None:
                self.maxRakiety = 5
            else:
                self.maxRakiety = rakietyMax
            self.aktualneRakiety = self.maxRakiety
            if maxTemperatura == None:
                self.maxTemperatura = 100
            else:
                self.maxTemperatura = maxTemperatura
            self.aktualnaTemperatura = 0
            self.przegrzanie = False
            self.font = pygame.font.SysFont('comicsansms', 20)
            if iloscLaserow == None:
                self.iloscLaserow = 1
            else:
                self.iloscLaserow = iloscLaserow
            if kasa == None and procki == None:
                if TRUDNOSC == 1:
                    self.kasa = 5000
                    self.procki = 3
                if TRUDNOSC == 2:
                    self.kasa = 3000
                    self.procki = 2
                if TRUDNOSC == 3:
                    self.kasa = 1500
                    self.procki = 1
            else:
                self.kasa = kasa
                self.procki = procki
            if kosztNaprawy == None:
                self.kosztNaprawy = 3
            else:
                self.kosztNaprawy = kosztNaprawy
            if cenaZlomu == None:
                self.cenaZlomu = 10
            else:
                self.cenaZlomu = cenaZlomu

            if wirus == None:
                self.wirus = 0
            else:
                self.wirus = wirus

            if liczbaWykonanychMisji == None:
                self.wykonaneMisje = 0
            else:
                self.wykonaneMisje = liczbaWykonanychMisji
            # statystyki
            if strzalyAll == None:
                self.strzalyAll = 0
            else:
                self.strzalyAll = strzalyAll
            if trafioneAll == None:
                self.trafioneAll = 0
            else:
                self.trafioneAll = trafioneAll
            if kasaAll == None:
                self.kasaAll = 0
            else:
                self.kasaAll = kasaAll
            if prockiAll == None:
                self.prockiAll = 0
            else:
                self.prockiAll = prockiAll

            self.strzalyMisja = 0
            self.trafioneMisja = 0
            self.prockiMisja = 0
            for i in range(20):
                self.zniszczone.append(0)
                self.zniszczoneMisja.append(0)

    def obroc(self, okno, obraz, x, y, punktX, punktY):
        #global czas
        srodekX = x + obraz.get_width() // 2
        srodekY = y + obraz.get_height() // 2
        cwiartka = 1

        if punktX > srodekX and punktY < srodekY:
            cwiartka = 1
        if punktX > srodekX and punktY >= srodekY:
            cwiartka = 2
        if punktX <= srodekX and punktY >= srodekY:
            cwiartka = 3
        if punktX <= srodekX and punktY < srodekY:
            cwiartka = 4

        odleglosc = math.sqrt((punktX - srodekX) ** 2 + (punktY - srodekY) ** 2)
        if cwiartka == 1:
            a = punktX - srodekX
        if cwiartka == 2:
            a = punktY - srodekY
        if cwiartka == 3:
            a = srodekX - punktX
        if cwiartka == 4:
            a = srodekY - punktY

        kat = math.asin(a / odleglosc)
        kat = (kat * 180) / math.pi

        if cwiartka == 1: kat += 270
        if cwiartka == 2: kat += 0
        if cwiartka == 3: kat += 90
        if cwiartka == 4: kat += 180

        kat = - kat

        kopia = pygame.transform.rotate(obraz, kat)
        rect = kopia.get_rect()
        kopia.set_colorkey('white')
        nx = (x + (obraz.get_width() - rect.width) / 2)
        ny = (y + ((obraz.get_height() - rect.height) / 2))

        self.kat = kat

        okno.blit(kopia, (nx, ny))
        """
        if myszKlik[0] and pygame.time.get_ticks() - czas > 50:
            czas = pygame.time.get_ticks()
            pociski.append([x + obraz.get_width() // 2 - obraz.get_width() // 2 * math.sin(kat * math.pi / 180),
                            y + obraz.get_height() // 2 - obraz.get_height() // 2 * math.cos(kat * math.pi / 180),
                            -5 * math.sin(kat * math.pi / 180), -5 * math.cos(kat * math.pi / 180)])"""



    def ustawPodMisje(self,rodzajMisji):
        self.aktualnaTemperatura = 0
        self.przegrzanie = False
        self.aktualneRakiety = self.maxRakiety
        self.kat = 0
 #tutaj
        #self.hp = self.maxHP
        self.aktualnyZlom = 0
        self.strzalyMisja = 0
        self.trafioneMisja = 0
        self.zlomMisja = 0
        self.prockiMisja = 0
        self.zniszczoneMisja.clear()
        self.czasOslony = pygame.time.get_ticks()
        self.oslona = False
        for i in range(20):
            self.zniszczoneMisja.append(0)

        if rodzajMisji in [1, 2]:
            self.x = SZEROKOSC // 2
            self.y = 470
            self.grafika = self.oryginalnaGrafika
            self.grafika.set_colorkey('white')
            self.szerokosc = self.grafika.get_width()
            self.wysokosc = self.grafika.get_height()
        if rodzajMisji in [3, 4]:
            self.x = 100
            self.y = WYSOKOSC // 2
            kopia = pygame.transform.rotate(self.oryginalnaGrafika, -90)
            kopia.set_colorkey('white')
            self.grafika = kopia
            self.szerokosc = self.grafika.get_width()
            self.wysokosc = self.grafika.get_height()

    def render(self, window, rodzajMisji,myszPozycja):
        CZARNY = (0,0,0)
        if self.kat != 0:
            kopia = pygame.transform.rotate(self.oryginalnaGrafika, self.kat)
            kopia.set_colorkey('white')
            self.grafika = kopia
            self.szerokosc = self.grafika.get_width()
            self.wysokosc = self.grafika.get_height()

        window.blit(self.grafika,(self.x,self.y))
        #self.obroc(window,self.grafika,self.x,self.y,myszPozycja[0], myszPozycja[1])
        if self.oslona:
            kopia = pygame.transform.scale(self.oslonaG,(self.szerokosc+20,self.wysokosc+20))
            window.blit(kopia,(self.x-12,self.y-12))

        window.blit(self.font.render("HP ", True, (255,255,255)),(10,558))
        window.blit(self.font.render("ZŁOM ", True, (255,255,255)),(10,588))
        window.blit(self.font.render("TEMP ", True, (255,255,255)),(10,618))
        if self.zbadalOslone:
            window.blit(self.font.render("OSŁONA ", True, (255, 255, 255)), (263, 558))
            #print(self.czasOdnawianiaOslony,pygame.time.get_ticks() - self.czasOslony )
            if not self.oslona:
                pasek(window, 355, 558, 25, 170, self.czasOdnawianiaOslony, pygame.time.get_ticks() - self.czasOslony, (255, 255, 255),'lightpink4')
            else:
                pasek(window, 355, 558, 25, 170, self.czasOdnawianiaOslony, self.czasOdnawianiaOslony, (255, 255, 255),'lightpink4')

        pasek(window, 80, 558, 25, 170, self.maxHP, self.hp, (255,255,255))
        pasek(window, 80, 588, 25, 170, self.maxZlom, self.aktualnyZlom, (255,255,255), (122,122,122))
        pasek(window, 80, 618, 25, 170, self.maxTemperatura, self.aktualnaTemperatura, (255,255,255), (255,0,0))
        window.blit(self.font.render(str(self.maxHP) + "/" + str(self.hp), True, CZARNY), (90, 556))
        window.blit(self.font.render(str(self.maxZlom) + "/" + str(self.aktualnyZlom), True, CZARNY), (90, 586))
        window.blit(self.font.render(str(self.maxTemperatura) + "/" + str(self.aktualnaTemperatura), True, CZARNY),(90, 616))
        window.blit(self.font.render(str(round(self.czasOdnawianiaOslony/1000)) + "/" + str(min(round(self.czasOdnawianiaOslony/1000),round((pygame.time.get_ticks() - self.czasOslony)/1000,1))), True, CZARNY), (365, 556))
        for i in range(self.aktualneRakiety):
            window.blit(Rakieta.grafika, (830+i*15,590))
        window.blit(self.font.render("RAKIETY ", True, (255, 255, 255)), (845, 558))

    def getRect(self):
        return pygame.Rect((self.x+10,self.y+10,self.szerokosc-10,self.wysokosc-10))

    def update(self, window, rodzajMisji, klawisze,myszKlik, myszPozycja, LASERY, RAKIETY):

        if self.zbadalOslone and not self.oslona and pygame.time.get_ticks() - self.czasOslony > self.czasOdnawianiaOslony:
            self.oslona = True
            self.oslonaD.play()

        if self.hp > 0:
            if rodzajMisji != 1 and klawisze[pygame.K_w] and self.y > 0:
                if rodzajMisji == 2 and self.y > 150:
                    self.y -= self.dy
                elif rodzajMisji != 2:
                    self.y -= self.dy
            if rodzajMisji != 1 and klawisze[pygame.K_s] and self.y + self.wysokosc < WYSOKOSC:
                self.y += self.dy
            if klawisze[pygame.K_a] and self.x > 0:
                self.x -= self.dx
            if klawisze[pygame.K_d] and self.x+self.szerokosc < SZEROKOSC:
                self.x += self.dx

            if myszKlik[1]:
                pygame.draw.circle(window,(255,255,255),(self.x + self.szerokosc//2,self.y+self.wysokosc//2),self.zasiegMagnesu,1)

            if not self.przegrzanie and myszKlik[0] and pygame.time.get_ticks() - self.czasLaseru > self.czasMiedzyLaserami:
                self.czasLaseru = pygame.time.get_ticks()
                self.laserD.play()
                if self.mocLaseru == 10:
                    self.aktualnaTemperatura += 1
                if self.mocLaseru == 15:
                    self.aktualnaTemperatura += 2
                if self.mocLaseru == 20:
                    self.aktualnaTemperatura += 3
                self.strzalyAll += self.iloscLaserow
                self.strzalyMisja += self.iloscLaserow

                if self.aktualnaTemperatura == ((self.maxTemperatura)//10 * 9):
                    self.alarmTemperaturyD.play()

                if self.aktualnaTemperatura >= self.maxTemperatura:
                    self.przegrzanie = True
                    self.czasPrzegrzania = pygame.time.get_ticks()
                if rodzajMisji in [1,2]:
                    if self.iloscLaserow == 1:
                        LASERY.append(Laser(self.x+self.szerokosc//2,self.y-3,0,-6,self.kat,rodzajMisji,self.mocLaseru))
                    elif self.iloscLaserow == 2:
                        LASERY.append(Laser(self.x+self.szerokosc-20,self.y+self.wysokosc//2,0,-6,0,rodzajMisji,self.mocLaseru))
                        LASERY.append(Laser(self.x+20,self.y+self.wysokosc//2,0,-6,0,rodzajMisji,self.mocLaseru))
                        self.aktualnaTemperatura += 1
                    elif self.iloscLaserow == 3:
                        LASERY.append(Laser(self.x + self.szerokosc - 15, self.y+self.wysokosc//2, 0, -6, 0, rodzajMisji,self.mocLaseru))
                        LASERY.append(Laser(self.x + self.szerokosc // 2, self.y-3, 0, -6, 0, rodzajMisji,self.mocLaseru))
                        LASERY.append(Laser(self.x + 15, self.y + self.wysokosc//2, 0, -6, 0, rodzajMisji,self.mocLaseru))
                        self.aktualnaTemperatura += 2
                if rodzajMisji in [3,4]:
                    if self.iloscLaserow == 1:
                        LASERY.append(Laser(self.x+self.szerokosc-3,self.y+self.wysokosc//2,6,0,-90,rodzajMisji,self.mocLaseru))
                    elif self.iloscLaserow == 2:
                        LASERY.append(Laser(self.x+self.szerokosc//2,self.y+20,6,0,-90,rodzajMisji,self.mocLaseru))
                        LASERY.append(Laser(self.x+self.szerokosc//2,self.y + self.wysokosc-20,6,0,-90,rodzajMisji,self.mocLaseru))
                    elif self.iloscLaserow == 3:
                        LASERY.append(Laser(self.x + self.szerokosc//2, self.y + 15, 6, 0, -90,rodzajMisji,self.mocLaseru))
                        LASERY.append(Laser(self.x + self.szerokosc - 3, self.y + self.wysokosc // 2, 6, 0, -90, rodzajMisji,self.mocLaseru))
                        LASERY.append(Laser(self.x + self.szerokosc//2, self.y +self.wysokosc - 15, 6, 0, -90, rodzajMisji,self.mocLaseru))

            if pygame.time.get_ticks() - self.czasPrzegrzania > 5000:
                self.przegrzanie = False

            if self.aktualnaTemperatura > 0 and pygame.time.get_ticks() - self.czasTemperatury > 500:
                self.czasTemperatury = pygame.time.get_ticks()
                self.aktualnaTemperatura -= 1

            if myszKlik[2] and pygame.time.get_ticks() - self.czasRakiety > 500 and self.aktualneRakiety > 0:
                self.czasRakiety = pygame.time.get_ticks()
                self.rakietaD.play()
                self.aktualneRakiety -= 1
                if rodzajMisji in [1, 2]:
                    RAKIETY.append(Rakieta(self.x+self.szerokosc//2-8,self.y,0,-self.szybkoscRakiet,0,rodzajMisji))
                if rodzajMisji in [3, 4]:
                    RAKIETY.append(Rakieta(self.x+self.szerokosc-5,self.y+self.wysokosc//2-8,self.szybkoscRakiet,0,-90,rodzajMisji))

        self.render(window,rodzajMisji,myszPozycja)


    def hit(self,ile):
        self.hp -= ile
        if self.hp < 0:
            self.hp = 0




