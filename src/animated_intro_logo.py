# src/animated_intro_logo.py
import pygame
import random
import math
import time
import os

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("I-AM-ROOT Intro Animation")
clock = pygame.time.Clock()

# Animation duration
duration = 6  # seconds
start_time = time.time()

# Leaf class
class Leaf:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)
        self.size = random.randint(10, 30)
        self.speed = random.uniform(0.5, 2)
        self.angle = random.uniform(0, 2*math.pi)

    def move(self):
        self.y += self.speed
        self.x += math.sin(self.angle) * 0.5
        self.angle += 0.01
        if self.y > HEIGHT:
            self.y = random.randint(-HEIGHT, 0)
            self.x = random.randint(0, WIDTH)

    def draw(self, surface):
        pygame.draw.ellipse(surface, (34, 139, 34), (int(self.x), int(self.y), self.size, self.size//2))

# Generate leaves
leaves = [Leaf() for _ in range(20)]

# Load logo
logo_path = os.path.join("assets", "logo.png")  # Place your logo in assets folder
if os.path.exists(logo_path):
    logo = pygame.image.load(logo_path).convert_alpha()
    logo = pygame.transform.scale(logo, (400, 200))  # Resize as needed
else:
    logo = None
    print("Logo not found!")

running = True
while running:
    elapsed = time.time() - start_time
    if elapsed > duration:
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Smooth background color change
    r = int((1 + math.sin(elapsed)) * 127)
    g = int((1 + math.sin(elapsed + 2)) * 127)
    b = int((1 + math.sin(elapsed + 4)) * 127)
    screen.fill((r, g, b))

    # Draw and move leaves
    for leaf in leaves:
        leaf.move()
        leaf.draw(screen)

    # Draw fading logo
    if logo:
        alpha = int(min(255, (elapsed / duration) * 255))  # Fade in over duration
        logo.set_alpha(alpha)
        screen.blit(logo, ((WIDTH - logo.get_width()) // 2, (HEIGHT - logo.get_height()) // 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

