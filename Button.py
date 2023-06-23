import pygame

class Button:
    x = 0
    y = 0
    width = 0
    height = 0
    color = (0,0,0)
    activeColor = (255,255,255)
    textColor = (0,0,0)
    text = ""
    textX = 10
    textY = 10
    font = 0
    time = 0.0
    wav = pygame.mixer.Sound("Dzwieki\sfx_menu_select1.wav")


    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.color = (0, 0, 0)
        self.activeColor = (255, 255, 255)
        self.text = ""
        self.font = pygame.font.SysFont('comicsansms', 20)
        self.time = pygame.time.get_ticks()
        self.textX = 10
        self.textY = 10

    def __init__(self, color, aColor, tColor, text, textX = 10, textY=10):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.color = color
        self.activeColor = aColor
        self.textColor = tColor
        self.text = text
        self.font = pygame.font.SysFont('comicsansms', 20)
        self.time = pygame.time.get_ticks()
        self.textX = textX
        self.textY = textY

    def render(self, window,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        if pygame.Rect(x,y,width,height).collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(window,self.activeColor,(x,y,width,height),0,4)
        else:
            pygame.draw.rect(window, self.color, (x, y, width, height),0,4)

        window.blit(self.font.render(self.text, True, self.textColor), (x+self.textX, y+self.textY))

    def clik(self):

        if pygame.time.get_ticks() - self.time > 300 and pygame.mouse.get_pressed()[0] and pygame.Rect(self.x,self.y,self.width,self.height).collidepoint(pygame.mouse.get_pos()):
            self.time = pygame.time.get_ticks()
            #self.wav.play()
            return True
        else:
            return False

    def updateText(self,newText):
        self.text = newText