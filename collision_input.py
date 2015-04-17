import pygame, sys, random
from pygame.locals import *


def terminate():
    pygame.quit()
    sys.exit()

class Food:

    def __init__(self, newFoodCounter, foodScore):
        self.foodCounter = 0
        self.foodSize = 20
        self.newFoodCounter = newFoodCounter
        self.foodScore = foodScore
        self.rectangle = pygame.Rect(random.randint(0, window.width-self.foodSize), random.randint(0, window.height - self.foodSize), self.foodSize, self.foodSize)

class GreenFood(Food):

    def __init__(self):
        Food.__init__(self, 40, 1)

class RedFood(Food):

    def __init__(self):
        Food.__init__(self, 100, 2)

class BlueFood(Food):

    def __init__(self):
        Food.__init__(self, 200, 5)

class Window:

    def __init__(self, width, height):
        self.width = width
        self.height = height

window = Window(400, 400)

class Player:

    def __init__(self, left, top, width, height):
        self.rectangle = pygame.Rect(left, top, width, height)



redFood = RedFood()
greenFood = GreenFood()
blueFood = BlueFood()



#set up
pygame.init()
mainClock = pygame.time.Clock()


#window


#WINDOWWIDTH = 400
#WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((window.width, window.height), 0, 32)
pygame.display.set_caption('Collision Input')

#colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
PURPLE = (180, 40, 215)


#food data
'''
foodCounter = 0
foodRedCounter = 0
foodBlueCounter = 0
NEWREDFOOD = 100
NEWBLUEFOOD = 200
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(300, 100, 50, 50)
'''


player = Player(300, 100, 50, 50)

foods = []
foods_red = []
foods_blue = []

for i in range(20):
    foods.append(GreenFood())

#Score
gameScore = 0


#movement variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

#gameLoop
while True:

    #Get events
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        #Press button
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == ord('a'):
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == ord('d'):
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == ord('w'):
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == ord('s'):
                moveUp = False
                moveDown = True
        #Release button
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                terminate()
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = False
            if event.key == K_UP or event.key == ord('w'):
                moveUp = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveDown = False
            if event.key == ord('x'):
                player.rectangle.top = random.randint(0, window.height - player.rectangle.height)
                player.rectangle.left = random.randint(0, window.width - player.rectangle.width)

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))

    greenFood.foodCounter += 1
    redFood.foodCounter += 1
    blueFood.foodCounter += 1
    if greenFood.foodCounter == greenFood.newFoodCounter:
        greenFood.foodCounter = 0
        foods.append(GreenFood())
    if redFood.foodCounter == redFood.newFoodCounter:
        redFood.foodCounter = 0
        foods_red.append(RedFood())
    if blueFood.foodCounter == redFood.newFoodCounter:
        blueFood.foodCounter = 0
        foods_blue.append(BlueFood())


    #Draw Background
    windowSurface.fill(BLACK)

    #Move player

    if moveDown and player.rectangle.bottom < window.height:
        player.rectangle.top += MOVESPEED
    if moveUp and player.rectangle.top > 0:
        player.rectangle.top -= MOVESPEED
    if moveLeft and player.rectangle.left > 0:
        player.rectangle.left -= MOVESPEED
    if moveRight and player.rectangle.right < window.width:
        player.rectangle.left += MOVESPEED

    #Draw player
    pygame.draw.rect(windowSurface, WHITE, player.rectangle)


    #Player vs Food
    for food in foods[:]:
        if player.rectangle.colliderect(food.rectangle):
            foods.remove(food)
            gameScore += 1
    for food_red in foods_red[:]:
        if player.rectangle.colliderect(food_red.rectangle):
            foods_red.remove(food_red)
            gameScore += 2
    for food_blue in foods_blue[:]:
        if player.rectangle.colliderect(food_blue.rectangle):
            foods_blue.remove(food_blue)
            gameScore += 5


    #Draw food
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, GREEN, foods[i].rectangle)
    for i in range(len(foods_red)):
        pygame.draw.rect(windowSurface, RED, foods_red[i].rectangle)
    for i in range(len(foods_blue)):
        pygame.draw.rect(windowSurface, BLUE, foods_blue[i].rectangle)

    #Displaying Score
    basicFont = pygame.font.SysFont(None, 48)
    text = basicFont.render('Score'+ str(gameScore), True, WHITE, BLUE)
    textRect = text.get_rect()
    textRect.centerx = window.width - textRect.width/2
    textRect.centery = 0 + textRect.height/2
    windowSurface.blit(text, textRect)

    #Draw window
    pygame.display.update()
    mainClock.tick(40)
