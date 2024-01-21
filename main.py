#This is a challenge to add on to HW-2
#As you remember the creeper face isnt just solid green, it has squares of different colors
#Use your knowledge in geometry and math to calculate the sizes of thse squares, use your knowledge on RGB values and the random number generator to get colors, and, utilize programming knowledge to write up an algorithm that can generate the squares (think of what coding fundamentels we learned to do this.)
#This assignment is the same as hw2 just making the different face colors, so you can copy paste what you did previously below, and then edit.

import secrets
import random
import pygame, sys
from pygame.locals import QUIT

#Assignment 2
#Draw Out A Creeper Face Using Rects
#The referance image you see of the creeper shows his head is a bunch of different colored squares
#Dont worry just make the head part all green, but, the challenge assignment for this will make you do the colors

#__SETUP__#
pygame.init()
#--Resolution--#
DISPLAYSURF = pygame.display.set_mode((500, 500))
#--Tab_Name--#
pygame.display.set_caption('Creeper Face Disco')
#--Frames_Per_Second--#
clock = pygame.time.Clock()
#--Color Palettes--#
greenPalet = [(51, 204, 51), (51, 153, 51), (0, 153, 51), (0, 102, 0),
              (102, 153, 0)]
bluePalet = [(0, 0, 255), (153, 204, 255), (0, 255, 255), (0, 51, 204),
             (51, 102, 204)]
redPalet = [(255, 80, 80), (204, 0, 0), (255, 0, 0), (204, 51, 0),
            (255, 92, 51)]
#--User Inputs--#
tickSpeed = input("What tick speed do you want (60 is the normal one.)")
sqreORcircle = input("Do you want rectangle or circle? (R/C) ")
if sqreORcircle == "R":
    widthSq = int(input("What size rectangle you want? (WIDTH) "))
    lenghtSq = int(input("What size rectangle you want? (LENGHT) "))
else:
    radius = int(input("What radius circle you? (RADIUS) "))
    spaceCol = int(input("How much space you want you? (Colum) "))
    spaceRow = int(input("How much space you want you? (Row) "))

colorChoice = input(
    "What color palet do you want. (Grean = G, Red = R, Blue = B)")

if colorChoice == "G":
    color = greenPalet
elif colorChoice == "B":
    color = bluePalet
else:
    color = redPalet
#__GAME_LOOP__#
#--Loops_Every_Frame--#
while True:
    #__Infinite Loop__#
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #EVERYTHING UNDER THIS... IS THE GAME#
    #Pressed A key, which moves them to the left#               #  X    Y    W    H

    if sqreORcircle == "R":
        for col in range(0, 500, widthSq):
            for row in range(0, 500, lenghtSq):

                pygame.draw.rect(DISPLAYSURF, secrets.choice(color),
                                 [col, row, widthSq, lenghtSq])
    else:
        for col in range(0, 500, spaceCol + radius):
            for row in range(0, 500, spaceRow + radius):
                pygame.draw.circle(DISPLAYSURF, secrets.choice(color),
                                   (col, row), (radius))

    leftEye = pygame.draw.rect(DISPLAYSURF, (0, 0, 0), [75, 100, 100, 100])
    rightEye = pygame.draw.rect(DISPLAYSURF, (0, 0, 0), [315, 100, 100, 100])
    main_nose = pygame.draw.rect(DISPLAYSURF, (0, 0, 0), [175, 200, 140, 200])
    right_nose = pygame.draw.rect(DISPLAYSURF, (0, 0, 0), [100, 275, 75, 200])
    left_nose = pygame.draw.rect(DISPLAYSURF, (0, 0, 0), [315, 275, 75, 200])

    pygame.display.update()
    clock.tick(int(tickSpeed))
