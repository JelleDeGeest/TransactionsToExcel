import pygame as pg

BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Transaction:
    def __init__(self, transaction, screen):
        if transaction[3] != "                                                                       ":
            self.begunstigde = Text(2,5, transaction[3], 40, screen)
        else:
            self.begunstigde = Text(2,5, "Bankcontact", 40, screen)
        value = float(transaction[1])
        if(value > 0):
            color = GREEN
        elif(value < 0):
            color = RED
        else:
            color = BLACK
        self.bedrag = Text(2,10, transaction[1] + " €", 40, screen, color)
        self.datum = Text(2,15, transaction[0], 25, screen)
        self.beschrijving = Text(2,20, transaction[4], 30, screen)
        self.screen = screen
    def draw(self):
        self.datum.draw()
        self.bedrag.draw()
        self.begunstigde.draw()
        self.beschrijving.draw()
class Text:
    def __init__(self, x, y, text, fontsize, screen,color=BLACK):
        self.x = x
        self.y = y
        self.text = text
        self.fontsize = fontsize
        self.screen = screen
        self.color = color
    def draw(self):
        font = pg.font.SysFont("Arial", self.fontsize)
        text = font.render(self.text, True, self.color)
        textRect = text.get_rect()
        textRect.midleft = (self.screen.get_width()*self.x/100, self.screen.get_height()*self.y/100)
        self.screen.blit(text,textRect)

class Buttons:
    def __init__(self, sheetnames, screen):
        self.buttons = []
        self.x = 5
        self.y = 0
        for sheetname in sheetnames:
            self.buttons.append(Button(self.x, self.y + 30, sheetname, screen))
            self.next()
    def draw(self):
        for button in self.buttons:
            button.draw()
    def next(self):
        self.x += 33
        if self.x >= 95:
            self.y += 7
            self.x = 5
    def click(self, x, y):
        for button in self.buttons:
            if button.click(x,y):
                return button.name
        return None
    
class Button:
    def __init__(self, x, y, name, screen):
        self.x = x
        self.y = y
        self.name = name
        self.screen = screen
        self.rect = None
    def draw(self):
        font = pg.font.SysFont("Arial", 30)
        text = font.render(self.name, True, BLACK)
        self.rect = text.get_rect()
        self.rect.midleft = (self.screen.get_width()*self.x/100, self.screen.get_height()*self.y/100)
        self.screen.blit(text,self.rect)
        pg.draw.rect(self.screen, BLACK, self.rect, 1)
    def click(self, x, y):
        if self.rect.collidepoint(x,y):
            return True
        else:
            return False



