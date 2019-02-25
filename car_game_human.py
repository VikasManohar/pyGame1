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
car_height = 75
# load and set the logo
# create a surface on screen that has the size of display_width and display_height
gameDisplay = pygame.display.set_mode((display_width,display_height))
logo = pygame.image.load("hello.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("pyGame Test")
clock = pygame.time.Clock()

#carImg = pygame.image.load('car.png')
#carImg = pygame.transform.scale(carImg, (50,100))
def basic_policy(x,car_width,thingx,thingw):
#   if x > display_width - car_width or x < 0:
    
    if(x >= thingx and (x + car_width) <= (thingx + thingw)):
        if(abs(x - thingx) < abs((x + car_width) - (thingx + thingw))):#left
            if((x -(x - thingx + car_width)) >= 0): #left
                return -(x - thingx + car_width)
            else: 
                return ((x + car_width) - (thingx + thingw) + car_width)#right
        else:
            if (((x +((x + car_width) - (thingx + thingw) + car_width))) <= display_width - car_width): #right
                return ((x + car_width) - (thingx + thingw) + car_width)#right
            else:
                return -(x - thingx + car_width)#left
                
    if(x >= thingx and x <= (thingx + thingw)):#right
        if( x + (thingx + thingw - x) <= (display_width - car_width)):#right
            return (thingx + thingw - x)
        else:
            return -( (x - thingx) + car_width )#left
    if((x + car_width) >= thingx and (x + car_width) <= (thingx + thingw)):#left
        if( (x - ((x + car_width) - thingx)) >= 0 ):
            return -((x + car_width) - thingx)
        else:
            return (((thingx+thingw) - (x+car_width)) + car_width)
    return 0
#    if(x > thingx + thingw):
#        do nothing
#    if(x + car_width < thingx):
#        do nothing
            
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, white)
    gameDisplay.blit(text, (0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
#    gameDisplay.blit(carImg, (x,y))
    pygame.draw.rect(gameDisplay, red, [x,y,car_width,car_height])

def text_objects(text,font):
    textSurface = font.render(text, True, white)
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
    y = (display_height * 0.85)
     
    x_change = 0
    
    thing_width = 100
    thing_height = 100
    thing_startx = random.randrange(0, display_width-100)
    thing_starty = -600
    thing_speed = 10
    dodged = 0
    
    # define a variable to control the main loop
    gameExit = False
     
    # main loop
    for episode in range(3):
        # event handling, gets all event from the event queue
        x = (display_width * 0.45)
        y = (display_height * 0.85)
         
        x_change = 0
        
        thing_width = 100
        thing_height = 100
        thing_startx = random.randrange(0, display_width)
        thing_starty = -600
        thing_speed = 10
        dodged = 0
        
#        for event in pygame.event.get():
#            # only do something if the event is of type QUIT
#            if event.type == pygame.QUIT:
#                pygame.quit()

        for step in range(2400000):
            for event in pygame.event.get():
            # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    pygame.quit()
            x_change = basic_policy(x,car_width,thing_startx,thing_width)
        
            x += x_change
        
            gameDisplay.fill(black)
            
            
            things(thing_startx, thing_starty, thing_width, thing_height, white)
            thing_starty += thing_speed
            car(x,y)
            things_dodged(dodged)
            
            if x > display_width - car_width or x < 0:
                print("----Crash------")
#                crash()
            
            if thing_starty > display_height:
                thing_starty = 0 - thing_height
                thing_startx = random.randrange(0, display_width)
                dodged += 1
    #            thing_speed += 1
    #            thing_width += (dodged * 1.2)
                
            if y < thing_starty + thing_height:
                if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
#                    crash()
                     print("----Crash------")
                
            pygame.display.update()
            clock.tick(240)

game_loop()  
pygame.quit()
     
