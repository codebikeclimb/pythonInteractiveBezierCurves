'''
@ Asher Holloman
'''

import pygame, sys, math
from pygame.locals import *
from operator import itemgetter

pygame.init()


pygame.display.set_caption('Bezier Curviness!')

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
LIGHTBLUE = (0, 255, 255)
CHARTREUSE = (0, 100, 0)
MIDNIGHTBLUE = (25,25,112)
DARKSLATEBLUE = (72,61,139)
DARKTURQUOISE = (0,206,209)
STEELBLUE = (70,130,180)
colors = [BLUE,GREEN,YELLOW,LIGHTBLUE]
blues = [BLUE,LIGHTBLUE,MIDNIGHTBLUE,STEELBLUE,DARKTURQUOISE,DARKSLATEBLUE]

size = [1280, 720]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pointList = []
curve = []
t = 0
done = False



def lerp(t, start, end):
        return (1-t)*start + t*end

def lerp2(t, start,end):
        return [lerp(t,start[0], end[0]), lerp(t,start[1], end[1])]

def reduce(t, poly):
        return [lerp2(t, poly[i], poly[i+1]) for i in range(len(poly)-1)]

def drawPoints(poly, color):
    if(len(poly) == 1):
        curve.append(poly[0])
    elif(len(poly) > 1):

        for i in range(len(poly)-1):
            pygame.draw.aaline(screen, color, (poly[i]),(poly[i+1]), 1)
            drawPoints(reduce(t, poly), color)

def drawCurve(self):

    for i in range(len(curve)-1):
        pygame.draw.aalines(screen, RED, False, curve, 4)





screen.fill(WHITE)

while not done:
    clock.tick(10)
    t = t + .01

    if(t > 1):
        t = 0
        curve = []
        screen.fill(WHITE)  #if it is running slow, comment this out and uncomment the screen.fill below so that it updates the screen at every tick instead of every Bezier curve cycle

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        if event.type == pygame.MOUSEBUTTONDOWN:
            pointList.append(pygame.mouse.get_pos())

   # screen.fill(WHITE)    #uncomment this

    p = pointList
    while len(p) > 1:
        drawPoints(p, blues[len(p)%6])
        p = reduce(t,p)


    drawCurve(curve)
    pygame.display.flip()

pygame.quit()

