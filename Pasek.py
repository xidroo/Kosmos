import pygame
def pasek(okno,x,y,wys, szer,wartoscMax,wartoscAktualna,kolorTla,kolor = 0):
    pygame.draw.rect(okno,kolorTla,[x,y,szer,wys],0,5)
    dlugosc = (wartoscAktualna*szer)//wartoscMax
    if wartoscAktualna > 0:
        if kolor == 0:
            pygame.draw.rect(okno,(255-((wartoscAktualna*255)/wartoscMax),255-(255-((wartoscAktualna*255)/wartoscMax)),0),[x+1,y+1,dlugosc-2,wys-2],0,5)
        else:
            pygame.draw.rect(okno, kolor ,[x + 1, y + 1, dlugosc - 2, wys - 2],0,5)
