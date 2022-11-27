import pygame
import random
#Setting up my game with Classes
#Using sprites, 2d piece of art


class Robot(pygame.sprite.Sprite):
    def __init__(self,width, height, x, y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect() #Rect to draw the image around 
        self.rect.center = [x, y]

#Game Screen
RES = 800, 600
fps = 60


#Game Loop

def main():
    pygame.init()
    window = pygame.display.set_mode(RES)
    c, clock = 0, pygame.time.Clock()

    robot = Robot(95,53,650,575,(204,153,255)) #Creating the object.
    robot_group = pygame.sprite.Group()
    robot_group.add(robot)



    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
        pygame.display.flip()
        robot_group.draw(window)
        clck = clock.tick(fps)

    
if __name__ == "__main__":
    main()
