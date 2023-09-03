import pygame
import sys
import string
from triangleMethod import process
pygame.init()

SCREEN_HEIGHT = 1080
SCREEN_WIDTH = 1920

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('MY PROJECT')
bg_img = pygame.image.load('menuassets/back.jpg')
bg = pygame.transform.scale(bg_img, (SCREEN_WIDTH,SCREEN_HEIGHT))
start_img = pygame.image.load('menuassets/start.png').convert_alpha()
ascii_img = pygame.image.load('menuassets/ASCII.jpg').convert_alpha()
salem_img = pygame.image.load('menuassets/salem2.jpg').convert_alpha()
sketch_img = pygame.image.load('menuassets/sketch.png').convert_alpha()

ACCEPTED = string.ascii_letters+string.digits+string.punctuation+" "


vec = pygame.math.Vector2

class TextBox(object):
    def __init__(self, rect, **kwargs):
        self.rect =pygame.Rect(rect)
        self.buffer = []
        self.final = None
        self.rendered = None
       
        
    def process_kwargs(self,kwargs):
        defaults = {
            "id" : None,
            "command" : None,
            "colour" : pygame.Color("white"),
            "font_colour" : pygame.Color("black"),
            "outline_colour" : pygame.Color("black"),
            "clean_on_enter" : False,
            "inactive_on_enter" : True
        }
        for kwarg in kwargs:
            if kwarg in defaults:
                defaults[kwarg] = kwargs[kwarg]
            else:
                print("error")
            self.__dict__.update(defaults)
            
    def get_event(self, event):
        if event.type == pygame.KEYDOWN and self.active:
            if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                self.execute()
            elif event.key == pygame.K_BACKSPACE:
                if self.buffer:
                    self.buffer.pop()
            elif event.unicode in ACCEPTED:
                self.buffer.append(event.unicode)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.alive = self.rectcollidepoint(event.pos)
            
        

    def draw(self):
        
        outline_color = self.active_color if self.active else self.outline_color
        outline = self.rect.inflate(self.outline_width*2,self.outline_width*2)
        #surface.fill(outline_color,outline)
        #surface.fill(self.color,self.rect)
        #if self.rendered:
            #surface.blit(self.rendered,self.render_rect,self.render_area)
       # if self.blink and self.active:
           # curse = self.render_area.copy()
           # curse.topleft = self.render_rect.topleft
           # surface.fill(self.font_color,(curse.right+1,curse.y,2,curse.h))
#

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
                
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action
start_button = Button(900, 888, start_img)
ASCII_button = Button(236,288,ascii_img)
salem_button = Button(1358,288,salem_img)
sketch_button = Button(797,288,sketch_img)
box1 = TextBox((100,100,150,30), clear_on_enter=True, inactive_on_enter=False)





def start_menu():
    i=0
    run=True
    while run:
        

        
        screen.fill((0,0,0))
        screen.blit(bg, (i,0))
        screen.blit(bg, (SCREEN_WIDTH+i,0))
        
        if i == -SCREEN_WIDTH:
            screen.blit(bg, (SCREEN_WIDTH+i,0))
            i=0
        i-= 1
        
        
        
        if start_button.draw():
            game_menu()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()

    

def game_menu():
    i=0
    run=True
    while run:
        screen.fill((0,0,0))
        screen.blit(bg, (i,0))
        
        screen.blit(bg, (SCREEN_WIDTH+i,0))
        if i == -SCREEN_WIDTH:
            screen.blit(bg, (SCREEN_WIDTH+i,0))
            i=0
        
        i-= 1
        
        if ASCII_button.draw():
            print("ascii")
            
        if salem_button.draw():
            triangle()
            
        if sketch_button.draw():
            print("sketch")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()

        
        
def triangle():
    i=0
    run=True
    while run:
        

        
        screen.fill((0,0,0))
        screen.blit(bg, (i,0))
        screen.blit(bg, (SCREEN_WIDTH+i,0))
        
        if i == -SCREEN_WIDTH:
            screen.blit(bg, (SCREEN_WIDTH+i,0))
            i=0
        i-= 1
        
        
        
        if box1.draw():
            ()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()

while True:
    start_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    

pygame.quit()