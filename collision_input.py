import pygame, sys, random
from pygame.locals import *
from collectibles import *
from windowSettings import *
from player import *


def terminate():
    pygame.quit()
    sys.exit()



window = Window(400, 400)


food_range = [window.width, window.height]
redFood = RedFood(food_range)
greenFood = GreenFood(food_range)
blueFood = BlueFood(food_range)



#set up
pygame.init()
mainClock = pygame.time.Clock()


#window
windowSurface = pygame.display.set_mode((window.width, window.height), 0, 32)
pygame.display.set_caption('Collision Input')

#colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
PURPLE = (180, 40, 215)



player = Player(300, 100, 50, 50, 6)

foods = []
foods_red = []
foods_blue = []

for i in range(20):
    foods.append(GreenFood(food_range))

#Score
gameScore = 0


#movement variables

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

movement = {"hor": False, "ver": False }

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
                movement["hor"] = "left"
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == ord('d'):
                movement["hor"] = "right"
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == ord('w'):
                movement["ver"] = "up"
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == ord('s'):
                movement["ver"] = "down"
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
        foods.append(GreenFood(food_range))
    if redFood.foodCounter == redFood.newFoodCounter:
        redFood.foodCounter = 0
        foods_red.append(RedFood(food_range))
    if blueFood.foodCounter == redFood.newFoodCounter:
        blueFood.foodCounter = 0
        foods_blue.append(BlueFood(food_range))


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
