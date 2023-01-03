import pygame


pygame.font.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('robot.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rise_speed = 5

    def move_left(self):
        self.rect.x -= 5

    def move_right(self):
        self.rect.x += 5

    def jump(self):
        self.rect.y -= 5
        
    def downJump(self):
        self.rect.y += 5

    def update(self):
        self.rect.y += self.rise_speed

#The robot can also shoot out soccer balls if they want.
class SoccerBall(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.image.load("soccerBall.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction
        self.speed = 5   
        
    def update(self):
        if self.direction == "horizontal":
            self.rect.x += 7
        if self.direction == "leftHorizontal":
            self.rect.x -= 5  

        
#The Robot will shoot out basketballs        
class Ball(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("ball.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        
        
    def update(self):
        self.rect.y -= 5


RES = 800, 600
fps = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BORDER_SIZE = 10
background_image = pygame.image.load("bluemoon.png")

#Ball Counter
font = pygame.font.Font(None, 36)
textBasketBallCount = "Ball Count: "
text_image_basketBall = font.render(textBasketBallCount, True, (255, 255, 255))

text_width, text_height = text_image_basketBall.get_size()
text_x = SCREEN_WIDTH - text_width - 35
text_y = 10



#To detect if the player goes out of bounds.
left_boundary = BORDER_SIZE
right_boundary = SCREEN_WIDTH - BORDER_SIZE
top_boundary = BORDER_SIZE
bottom_boundary = SCREEN_HEIGHT - BORDER_SIZE


clock = pygame.time.Clock()


def main():
    pygame.init()
    robot = Player(50, 490)
    group = pygame.sprite.Group()
    group.add(robot)
    
    balls = pygame.sprite.Group()
    soccerBalls = pygame.sprite.Group()
    
    screen = pygame.display.set_mode((RES))
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE:
                        ball = Ball(robot.rect.x, robot.rect.y - 25) 
                        balls.add(ball)
                if event.key == pygame.K_1:
                        soccerBall = SoccerBall(robot.rect.x, robot.rect.y + 35, "horizontal")
                        soccerBalls.add(soccerBall)
                        
                if event.key == pygame.K_2:
                    soccerBall = SoccerBall(robot.rect.x, robot.rect.y + 35, "leftHorizontal")
                    soccerBalls.add(soccerBall)
                   
                    
                

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
           robot.move_left()
        if keys[pygame.K_RIGHT]:
           robot.move_right()
        if keys[pygame.K_UP]:
           robot.jump()
        if keys[pygame.K_DOWN]:
           robot.downJump()
            
            
        if robot.rect.left < left_boundary:
            robot.rect.left = left_boundary
        if robot.rect.right > right_boundary:
            robot.rect.right = right_boundary
            
        if robot.rect.y > SCREEN_HEIGHT:
            robot.rect.y = 0
            
        if robot.rect.y < 0:
            robot.rect.y = SCREEN_HEIGHT
            
        screen.blit(background_image, (0, 0))
        screen.blit(text_image_basketBall, (text_x, text_y))
        balls.update()
        balls.draw(screen)
        
        soccerBalls.update()
        soccerBalls.draw(screen)
        
        group.draw(screen)

        pygame.display.flip()
        screen.fill((0,0,0))
        clock.tick(fps)


if __name__ == "__main__":
    main()
