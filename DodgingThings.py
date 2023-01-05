import pygame
import os
import random

pygame.font.init()
pygame.init()

# To keep tally of the users scores
global score
score = 0


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

# The robot can also shoot out soccer balls if they want.


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
        global score
        if self.direction == "horizontal":
            self.rect.x += 7
        if self.direction == "leftHorizontal":
            self.rect.x -= 5

        if pygame.sprite.spritecollide(self, movingSprites, True):
            self.kill()
            score += 2


# The Robot will shoot out basketballs
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
        global score
        self.rect.y -= 7.5
        if pygame.sprite.spritecollide(self, movingSprites, True):
            self.kill()
            score += 2


class PinkMonster(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, flipped):
        super().__init__()

        self.animation_list = []
        # Loading the animations in
        self.right_animation_list = []

        # Loading the original animation
        for i in range(10):
            image = pygame.image.load(os.path.join(
                'animation', 'image{}.png'.format(i)))
            image = pygame.transform.scale(
                image, (image.get_width() * 1.5, image.get_height() * 1.5))
            self.animation_list.append(image)

        # Want to make the monster walk Right, so use pygame.transfom.flip()
        for image in self.animation_list:
            flipped_image = pygame.transform.flip(image, True, False)
            self.right_animation_list.append(flipped_image)

        self.current_sprite = 0
        self.current_sprite_forRight = 0
        self.image = self.animation_list[self.current_sprite]
        self.flipped_image = self.right_animation_list[self.current_sprite_forRight]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction
        self.flipped = flipped

    def update(self):
        self.current_sprite += 0.5
        self.current_sprite_forRight += 0.5

        if self.flipped == "left":
            if self.current_sprite >= len(self.animation_list):
                self.current_sprite = 0
            self.image = self.animation_list[int(self.current_sprite)]

        if self.flipped == "right":
            if self.current_sprite_forRight >= len(self.right_animation_list):
                self.current_sprite_forRight = 0
            self.flipped_image = self.right_animation_list[int(
                self.current_sprite_forRight)]

        if self.direction == "left":
            self.rect.x -= 4

        if self.direction == "right":
            self.image = self.flipped_image
            self.rect.x += 4


# Game resolution
RES = 800, 600
fps = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BORDER_SIZE = 10

# Background music
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.music.load("BackgroundMusic.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Background image
background_image = pygame.image.load("bluemoon.png")

# Ball Counter
font = pygame.font.Font(None, 22)


# timer
timerFont = pygame.font.Font(None, 22)
timer = pygame.time.get_ticks()


# To detect if the player goes out of bounds.
left_boundary = BORDER_SIZE
right_boundary = SCREEN_WIDTH - BORDER_SIZE
top_boundary = BORDER_SIZE
bottom_boundary = SCREEN_HEIGHT - BORDER_SIZE


clock = pygame.time.Clock()
pygame.display.set_caption('Dodging Things')

# The sprite groups
movingSprites = pygame.sprite.Group()
group = pygame.sprite.Group()
balls = pygame.sprite.Group()
soccerBalls = pygame.sprite.Group()


def main():
    global score
    positionForMonsterX = random.randint(0, 800)
    positionForMonsterY = random.randint(0, 600)

    x = random.randint(0, 800)
    y = random.randint(0, 600)

    robot = Player(50, 490)
    pinkMonster = PinkMonster(
        positionForMonsterX, positionForMonsterY, "left", "left")
    pinkMonsterRight = PinkMonster(x, y, "right", "right")

    group.add(robot)
    movingSprites.add(pinkMonster)
    movingSprites.add(pinkMonsterRight)

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
                    soccerBall = SoccerBall(
                        robot.rect.x, robot.rect.y + 35, "horizontal")
                    soccerBalls.add(soccerBall)

                if event.key == pygame.K_2:
                    soccerBall = SoccerBall(
                        robot.rect.x, robot.rect.y + 35, "leftHorizontal")
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

        if pinkMonster.rect.x < -30:
            pinkMonster.rect.x = -30
            pinkMonster.direction = "right"
            pinkMonster.flipped = "right"

        if pinkMonster.rect.x > SCREEN_WIDTH:
            pinkMonster.rect.x = SCREEN_WIDTH
            pinkMonster.direction = "left"
            pinkMonster.flipped = "left"

        if pinkMonsterRight.rect.x < -30:
            pinkMonsterRight.rect.x = -30
            pinkMonsterRight.direction = "right"
            pinkMonsterRight.flipped = "right"

        if pinkMonsterRight.rect.x > SCREEN_WIDTH:
            pinkMonsterRight.rect.x = SCREEN_WIDTH
            pinkMonsterRight.direction = "left"
            pinkMonsterRight.flipped = "left"

        # The score for the user

        textBasketBallCount = "Ball Count: {} ".format(score)
        text_image_basketBall = font.render(
         textBasketBallCount, True, (255, 255, 255))
        text_width, text_height = text_image_basketBall.get_size()
        text_x = SCREEN_WIDTH - text_width - 35
        text_y = 10
        
        #The amount of time that the user has survived in the game

        timer = pygame.time.get_ticks()
        timer_text = f"Time Survived: {str(timer // 1000)}"
        timer_image = timerFont.render(timer_text, True, (255, 255, 255))
        
        
        screen.blit(background_image, (0, 0))  # Image Goes First
        screen.blit(timer_image, (text_x - 675, text_y))
        screen.blit(text_image_basketBall, (text_x, text_y - text_height // 2))

        balls.update()
        balls.draw(screen)

        soccerBalls.update()
        soccerBalls.draw(screen)

        movingSprites.update()
        movingSprites.draw(screen)

        group.draw(screen)

        pygame.display.flip()
        screen.fill((0, 0, 0))
        clock.tick(60)


if __name__ == "__main__":
    main()
