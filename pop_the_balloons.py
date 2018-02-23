#########################################
# Programmer: Mrs. G
# Date: 20/03/2014
# File Name: pop_the_balloons.py
# Description: This program is a template for a game. It demonstrates use of lists.
#########################################

import pygame
pygame.init()

from math import sqrt                   # only sqrt function is needed from the math module
from random import randint             # only randint function is needed from the random module
import time
gameOver = False
font = pygame.font.SysFont("Arial Black",30)

HEIGHT = 600
WIDTH  = 800
game_window=pygame.display.set_mode((WIDTH,HEIGHT))

ground = pygame.image.load("groundResized.png")
ground = ground.convert_alpha()

ballBack = pygame.image.load("ballBackResized.png")
ballBack = ballBack.convert_alpha()

sky = pygame.image.load("skyResized.png")
sky = sky.convert_alpha()

blue = pygame.image.load("balloon blue.png")
blue = blue.convert_alpha()

purple = pygame.image.load("balloon purple.png")
purple = purple.convert_alpha()

red = pygame.image.load("balloon red.png")
red = red.convert_alpha()

green = pygame.image.load("balloon green.png")
green = green.convert_alpha()

orange = pygame.image.load("balloon orange.png")
orange = orange.convert_alpha()

ballR = []
ballG = []
ballB = []

balloonVisible = []

balloonCLR = []
balloonRH = []

WHITE = (255,255,255)                   #
BLACK = (0,0,0)                   # used colours
outline = 0
counter = 0
message = "0"
time7 = 30
gametime = 1
# thickness of the shapes' outline
#---------------------------------------#
# function that calculates distance     #
# between two points in coordinate system
#---------------------------------------#
def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)# Pythagorean theorem    

#---------------------------------------#
# function that redraws all objects     #
#---------------------------------------#
def redraw_game_window():
    global time7
    global blue
    global purple
    global red
    global green
    global orange
    
    
    game_window.fill(BLACK)
    game_window.blit(sky, (0,0))
    game_window.blit(ground, (0,0))
    game_window.blit(ballBack, (0,0))

    for i in range(20):
        if(balloonVisible[i]):
            if(balloonCLR[i]==1):
                scaledBlue = pygame.transform.scale(blue, (balloonR[i],int(balloonR[i]*1.6))) 
                game_window.blit(scaledBlue, (balloonX[i]-(balloonR[i]),balloonY[i]-(balloonR[i])))
            if(balloonCLR[i]==2):
                scaledPurple = pygame.transform.scale(purple, (balloonR[i],int(balloonR[i]*1.6)))
                game_window.blit(scaledPurple, (balloonX[i]-(balloonR[i]),balloonY[i]-(balloonR[i])))
            if(balloonCLR[i]==3):
                scaledRed = pygame.transform.scale(red, (balloonR[i],int(balloonR[i]*1.6)))
                game_window.blit(scaledRed, (balloonX[i]-(balloonR[i]),balloonY[i]-(balloonR[i])))
            if(balloonCLR[i]==4):
                scaledGreen = pygame.transform.scale(green, (balloonR[i],int(balloonR[i]*1.6)))
                game_window.blit(scaledGreen, (balloonX[i]-(balloonR[i]),balloonY[i]-(balloonR[i])))
            if(balloonCLR[i]==5):
                scaledOrange = pygame.transform.scale(orange, (balloonR[i],int(balloonR[i]*1.6)))
                game_window.blit(scaledOrange, (balloonX[i]-(balloonR[i]),balloonY[i]-(balloonR[i])))
            #pygame.draw.circle(game_window, (ballR[i],ballG[i],ballB[i]), (int(balloonX[i]-(balloonR[i]/2)), int(balloonY[i]-(balloonR[i]/2))), int(balloonR[i]/2), outline)
    
    text = font.render(str(counter), 1, WHITE)
    text2 = font.render("Balloons Popped: ", 1, WHITE)
    text7 = font.render("Time Remaining: ", 1, WHITE)
    text3 = font.render(tim, 1, WHITE)
    game_window.blit(text,((WIDTH/2)+330,20))
    game_window.blit(text7,((WIDTH/2)+45,50))
    game_window.blit(text2,((WIDTH/2)+45,20))
    game_window.blit(text3,((WIDTH/2)+320,50))
    
    pygame.display.update()             # display must be updated, in order
                                        # to show the drawings
       
#---------------------------------------#
# the main program begins here          #
#---------------------------------------#
exit_flag = False                       #

balloonR = [0]*20                       # create lists of 20 items each
balloonX = [0]*20                       # for balloons' properties
balloonY = [0]*20
balloonRH = [0]*20
balloonSPEED = [0]*20
balloonCLR = [0]*20
balloonVisible = [0]*20
ballR = [0]*20
ballG = [0]*20
ballB = [0]*20

for i in range(20):
    balloonR[i] = randint(60,100)
    balloonX[i] = randint(int(balloonR[i]/2), int(WIDTH-(balloonR[i]/2)))     # initialize the coordinates and the size of the balloons
    balloonY[i] = randint(0, int(HEIGHT-(balloonR[i]/2)))
    balloonSPEED[i] = randint(1,3)
    ballR[i] = randint(0,255)
    ballG[i] = randint(0,255)
    ballB[i] = randint(0,255)
    balloonCLR[i] = randint(1,5)
    balloonVisible[i] = True


while not exit_flag:                    #
    for event in pygame.event.get():    # check for any events
        if event.type == pygame.QUIT:   # If user clicked close
            exit_flag = True            # Flag that we are done so we exit this loop

# act upon mouse events
        if(gameOver==False):
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(20):
                    (cursorX,cursorY)=pygame.mouse.get_pos()
                    if (distance(cursorX, cursorY, balloonX[i]-(balloonR[i]/2), balloonY[i]-(balloonR[i]/2))< balloonR[i]/2):
                        balloonVisible[i] = False
                        balloonY[i] = HEIGHT+balloonR[i]
                        balloonX[i] = randint(0,WIDTH)
                        balloonVisible[i] = True
                        counter+=1
                        print(counter)
                    
# move the balloons
    for i in range(20):
        balloonY[i] = balloonY[i] - balloonSPEED[i]
        if(balloonY[i]<=0-balloonR[i]):
                balloonVisible[i] = False
                balloonY[i] = HEIGHT+balloonR[i]
                balloonX[i] = randint(0,WIDTH)
                balloonVisible[i] = True
            
# update the screen
    tim = str(int(60-time.clock()))
    if(gameOver==False):
        redraw_game_window()
    pygame.time.delay(10)

    if(int(tim)<=0):
        gameOver = True

        game_window.fill(BLACK)
        game_window.blit(sky, (0,0))
        game_window.blit(ground, (0,0))
        game_window.blit(ballBack, (0,0))
        
        font1 = pygame.font.SysFont("Arial Black",70)
        text0 = font1.render("Game Over!", 1, WHITE)
        text2 = font.render("Balloons Popped: ", 1, WHITE)
        text = font.render(str(counter), 1, WHITE)
        game_window.blit(text0,((WIDTH/2)-210, (HEIGHT/2)-50))
        game_window.blit(text2,((WIDTH/2)-150, (HEIGHT/2)+50))
        game_window.blit(text,((WIDTH/2)+140, (HEIGHT/2)+50))
        pygame.display.update() 
        #exit_flag = True
    
pygame.quit()                           # always quit pygame when done!
