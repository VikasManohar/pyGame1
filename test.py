# import the pygame module, so you can use it
import pygame
import time
import random
# initialize the pygame module
pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 50
# load and set the logo
# create a surface on screen that has the size of display_width and display_height
gameDisplay = pygame.display.set_mode((display_width,display_height))
logo = pygame.image.load("hello.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("pyGame Test")
clock = pygame.time.Clock()

carImg = pygame.image.load('car.png')
carImg = pygame.transform.scale(carImg, (50,100))

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()
    time.sleep(2)
    
    game_loop()


def crash():
    message_display('You Crashed!')
    
    
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
     
    x_change = 0
    
    thing_width = 100
    thing_height = 100
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    dodged = 0
    
    # define a variable to control the main loop
    gameExit = False
     
    # main loop
    while not gameExit:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    
        
        x += x_change
        
        gameDisplay.fill(white)
        
        
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)
        
        if x > display_width - car_width or x < 0:
            crash()
        
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
#            thing_speed += 1
#            thing_width += (dodged * 1.2)
            
        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                crash()
            
        pygame.display.update()
        clock.tick(60)

game_loop()  
pygame.quit()
     
