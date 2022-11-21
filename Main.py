import pygame #imports the pygame library into usage

pygame.init() #initializes the pygame modules
window = pygame.display.set_mode((1200, 720)) #creates a window with the function


ball = pygame.image.load("ball.png")
robot = pygame.image.load("robot.png")

x = 0
y = 0

a = 0

b = 560
width = ball.get_width()
height = ball.get_height()

velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           exit()

    window.fill((0,204,204))
    window.blit(pygame.transform.scale(ball,(150, 150)), (x, y)) 
    window.blit(robot, (0, 200))
    window.blit(pygame.transform.scale(ball,(150, 150)), (0, 0)) 
    window.blit(pygame.transform.scale(ball,(150, 150)), (a,560)) 
    window.blit(pygame.transform.scale(ball,(150, 150)), (0,560)) 
       #window.blit(ball,(600-width/2,360-height/2)) #Puts the ball at the middle of the screen, the centre of the window is at half its width and height
    pygame.display.flip() # After the window is filled with colour the image is drawn at the given location with the blit method. Then the contents of the window are updated with the function pygame.display.flip.

    x+= velocity 
    a+= velocity + 3

    if velocity > 0 and x+ball.get_width() >= 1200:
        velocity = -velocity

    if velocity < 0 and x <=0:
        velocity = -velocity


    
    if velocity > 0 and a+ball.get_width() >= 1200:
        velocity = -velocity

    if velocity < 0 and a <=0:
        velocity = -velocity


    


    clock.tick(60) #60 dictates that the loop should be executed 60 times a second


    