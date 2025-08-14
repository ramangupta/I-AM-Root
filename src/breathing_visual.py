import pygame
import time
import os

# --- Setup ---
pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("I-AM-ROOT Breathing Exercise")

# Colors
BG_COLOR = (30, 30, 30)
CIRCLE_COLOR = (102, 205, 170)

# Music
MUSIC_FILE = os.path.join("assets", "calm_music1.mp3")
if os.path.exists(MUSIC_FILE):
    pygame.mixer.init()
    pygame.mixer.music.load(MUSIC_FILE)
    pygame.mixer.music.play(-1)

# Breathing timings (seconds)
inhale_time = 4
hold_time = 2
exhale_time = 4
cycles = 4

# Circle parameters
min_radius = 10
max_radius = 200

def breathe_circle(inhale, hold, exhale):
    for cycle in range(cycles):
        # Inhale - expand circle
        start_time = time.time()
        while time.time() - start_time < inhale:
            t = (time.time() - start_time) / inhale
            radius = int(min_radius + t * (max_radius - min_radius))
            screen.fill(BG_COLOR)
            pygame.draw.circle(screen, CIRCLE_COLOR, (WIDTH//2, HEIGHT//2), radius)
            pygame.display.flip()
        
        # Hold - keep max circle
        start_time = time.time()
        while time.time() - start_time < hold:
            screen.fill(BG_COLOR)
            pygame.draw.circle(screen, CIRCLE_COLOR, (WIDTH//2, HEIGHT//2), max_radius)
            pygame.display.flip()
        
        # Exhale - shrink circle
        start_time = time.time()
        while time.time() - start_time < exhale:
            t = (time.time() - start_time) / exhale
            radius = int(max_radius - t * (max_radius - min_radius))
            screen.fill(BG_COLOR)
            pygame.draw.circle(screen, CIRCLE_COLOR, (WIDTH//2, HEIGHT//2), radius)
            pygame.display.flip()
        
        # Hold - keep min circle
        start_time = time.time()
        while time.time() - start_time < hold:
            screen.fill(BG_COLOR)
            pygame.draw.circle(screen, CIRCLE_COLOR, (WIDTH//2, HEIGHT//2), min_radius)
            pygame.display.flip()

try:
    breathe_circle(inhale_time, hold_time, exhale_time)
finally:
    pygame.mixer.music.stop()
    pygame.quit()

