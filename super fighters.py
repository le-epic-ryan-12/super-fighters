from cv2 import CAP_OPENNI_DISPARITY_MAP_32F
import pygame
from pygame import mixer
pygame.init()

mixer.music.load('music.wav')
mixer.music.play(-1)


WIDTH = 1100
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))


backgrounds = []
city1 = pygame.image.load('newcity1.png')
city2 = pygame.image.load('newcity2.png')
city3 = pygame.image.load('newcity3.png')
city4 = pygame.image.load('newcity4.png')
city5 = pygame.image.load('newcity5.png')
city6 = pygame.image.load('newcity6.png')
city7 = pygame.image.load('newcity7.png')

for city in range(15):
    backgrounds.append(city1)
for city in range(15):
    backgrounds.append(city2)
for city in range(15):
    backgrounds.append(city3)
for city in range(15):
    backgrounds.append(city4)
for city in range(15):
    backgrounds.append(city5)
for city in range(15):
    backgrounds.append(city6)
for city in range(15):
    backgrounds.append(city7)    
n = 0

how_to = pygame.image.load('how_to.png')

class button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.hovered = False

    def draw(self):

        action = False

        pos = pygame.mouse.get_pos()




        if self.rect.collidepoint(pos) and self.hovered is False:
            self.hovered = True
            if self.hovered is True:
                self.image = pygame.image.load('how_to_selected.png')
                selection_sound = mixer.Sound('selection.wav')
                selection_sound.play()

        if self.hovered is True and not self.rect.collidepoint(pos):
            self.hovered = False
            if self.hovered is False:
                self.image = pygame.image.load('how_to.png')

        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked == True
            
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

    
            
        

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

 

        



how_to_button = button(100, 480, how_to)

pygame.display.set_caption("game")
#icon = pygame.image.load('undefined.png')
#pygame.display.set_icon(icon)

running = True

while running:

    how_to_button.draw()


    if n < (len(backgrounds)-1):
        n += 1
    else:
        n = 0

    screen.fill((0, 0, 0))
    screen.blit(backgrounds[n], ((0,0)))

    if how_to_button.draw():
        print("clicked")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    pygame.display.update()