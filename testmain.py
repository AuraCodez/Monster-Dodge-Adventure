import pygame #imports the pygame library into usage
import math
import random

pygame.init() #initializes the pygame modules
window = pygame.display.set_mode((1200, 720)) #creates a window with the function


ball = pygame.image.load("ball.png")
robot = pygame.image.load("robot.png")
ball_speed = 5
ball_velocity = 0
ball_position = (900,5)

x = 0
y = 720-robot.get_height()
a = 0

b = 560
width = ball.get_width()
height = ball.get_height()

velocity = 1
angle = 0
clock = pygame.time.Clock()

moveRight = False
moveLeft = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveLeft = True
            if event.key == pygame.K_RIGHT:
                moveRight = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveLeft = False
            if event.key == pygame.K_RIGHT:
                moveRight = False

        if event.type == pygame.QUIT:
           exit()


    if moveRight:
        x+= 5
    if moveLeft:
        x-= 5



    window.fill((0,204,204))
    window.blit(pygame.transform.scale(ball,(150, 150)), (0, 0)) 
    window.blit(pygame.transform.scale(ball,(150,150)),ball_position)
    window.blit(robot,(x,y))
    #window.blit(ball,(600-width/2,360-height/2)) #Puts the ball at the middle of the screen, the centre of the window is at half its width and height
    pygame.display.flip() # After the window is filled with colour the image is drawn at the given location with the blit method. Then the contents of the window are updated with the function pygame.display.flip.

    clock.tick(60) #60 dictates that the loop should be executed 60 times a second

