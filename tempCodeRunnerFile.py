import pygame
import random

pygame.init()

# Set display size and colors
display_width = 800
display_height = 600
black = (0, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Moving Colored Balls')
clock = pygame.time.Clock()

# Ball class to manage movement
class Ball:
    def __init__(self):
        self.radius = random.randint(10, 30)  # Random radius
        self.x = random.randint(self.radius, display_width - self.radius)
        self.y = random.randint(self.radius, display_height - self.radius)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Random color
        self.speed_x = random.choice([-5, 5])  # Random speed in x-direction
        self.speed_y = random.choice([-5, 5])  # Random speed in y-direction

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        
        # Bounce off the walls
        if self.x - self.radius <= 0 or self.x + self.radius >= display_width:
            self.speed_x *= -1
        if self.y - self.radius <= 0 or self.y + self.radius >= display_height:
            self.speed_y *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

def game_loop():
    # Create a list of balls
    balls = [Ball() for _ in range(20)]  # Create 20 random balls

    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        gameDisplay.fill(black)

        # Move and draw balls
        for ball in balls:
            ball.move()
            ball.draw(gameDisplay)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

game_loop()
