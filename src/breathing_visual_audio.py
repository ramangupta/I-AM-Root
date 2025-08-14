# src/breathing_visual_audio.py
import pygame
import time
import os
import math

# --- Pygame setup ---
pygame.init()
font = pygame.font.SysFont('Arial', 48, bold=True)

# Screen setup
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("I-AM-ROOT Breathing")
clock = pygame.time.Clock()

# Colors
BG_COLOR = (30, 30, 30)
CIRCLE_COLOR = (50, 205, 50)
GLOW_COLOR = (50, 205, 50, 60)  # Semi-transparent glow

# Assets
CALM_MUSIC = os.path.join("assets", "calm_music1.wav")

# Breathing parameters
inhale_time = 3
hold_time   = 2
exhale_time = 3
cycles      = 4
min_radius = 50
max_radius = 200

# Pygame mixer
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

# Play background music
if os.path.exists(CALM_MUSIC):
    pygame.mixer.music.load(CALM_MUSIC)
    pygame.mixer.music.set_volume(0.5)  # Pleasant audible volume
    pygame.mixer.music.play(-1)
else:
    print(f"Background music file not found: {CALM_MUSIC}")

# --- Animation functions ---

def animate_circle(duration, start_radius, end_radius, label="", hold=False):
    start_ticks = pygame.time.get_ticks()
    
    while True:
        elapsed = (pygame.time.get_ticks() - start_ticks) / 1000
        if elapsed > duration:
            break

        t = elapsed / duration
        eased = math.sin(t * math.pi / 2)
        radius = int(start_radius + (end_radius - start_radius) * eased)

        if hold:
            radius = int(radius * (1 + 0.05 * math.sin(elapsed * 2 * math.pi)))

        # Draw background & glow
        screen.fill(BG_COLOR)
        glow_radius = int(radius * 1.3)
        glow_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        pygame.draw.circle(glow_surface, GLOW_COLOR, (WIDTH//2, HEIGHT//2), glow_radius)
        screen.blit(glow_surface, (0, 0))

        # Draw main circle
        pygame.draw.circle(screen, CIRCLE_COLOR, (WIDTH//2, HEIGHT//2), radius)

        # Draw label text
        if label:
            text_surface = font.render(label, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(60)

def breathing_session(cycles=cycles):
    for i in range(cycles):
        animate_circle(inhale_time, min_radius, max_radius, label="Inhale")          # Inhale
        animate_circle(hold_time, max_radius, max_radius, label="Hold", hold=True)   # Hold
        animate_circle(exhale_time, max_radius, min_radius, label="Exhale")          # Exhale
        animate_circle(hold_time, min_radius, min_radius, label="Hold", hold=True)   # Hold

    # Clear screen at the end
    screen.fill(BG_COLOR)
    pygame.display.flip()
    print("\nBreathing session complete. 🌱")
    pygame.mixer.music.stop()

    # Keep window open until user closes
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

# --- Main ---
if __name__ == "__main__":
    breathing_session()
