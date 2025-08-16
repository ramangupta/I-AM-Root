# src/breathing_visual_audio.py
import pygame
import time
import os
import math
import sys
from datetime import datetime
import json

# ---------------- Colors ---------------- #
BG_COLOR = (30, 30, 30)
CIRCLE_COLOR = (50, 205, 50)
GLOW_COLOR = (50, 205, 50, 50)

# ---------------- Default Breathing Patterns ---------------- #
PATTERNS = {
    "Box Breathing": {"inhale": 4, "hold": 2, "exhale": 4, "cycles": 2},
    "4-7-8 Breathing": {"inhale": 4, "hold": 7, "exhale": 8, "cycles": 4},
}

# ---------------- Circle Parameters ---------------- #
MIN_RADIUS = 50
MAX_RADIUS = 200

# ---------------- Sounds ---------------- #
CALM_MUSIC = os.path.join("assets", "calm_music1.wav")
CHIME_SOUND = os.path.join("assets", "chime.wav")


def animate_circle(screen, clock, font, duration, start_radius, end_radius, label="", hold=False, chime=None):
    """Animate circle for inhale, hold, exhale."""
    start_ticks = pygame.time.get_ticks()
    played_chime = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()

        elapsed = (pygame.time.get_ticks() - start_ticks) / 1000
        if elapsed > duration:
            break

        # Play chime at start of phase
        if chime and not played_chime:
            chime.play()
            played_chime = True

        t = elapsed / duration
        eased = math.sin(t * math.pi / 2)
        radius = int(start_radius + (end_radius - start_radius) * eased)
        if hold:
            radius = int(radius * (1 + 0.05 * math.sin(elapsed * 2 * math.pi)))

        # Dynamic background color (optional)
        color_shift = int(20 * math.sin(elapsed * 2 * math.pi / duration))
        screen.fill((BG_COLOR[0] + color_shift, BG_COLOR[1] + color_shift, BG_COLOR[2] + color_shift))

        # Glow
        glow_radius = int(radius * 1.3)
        glow_surface = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
        pygame.draw.circle(glow_surface, GLOW_COLOR, (screen.get_width() // 2, screen.get_height() // 2), glow_radius)
        screen.blit(glow_surface, (0, 0))

        # Main circle
        pygame.draw.circle(screen, CIRCLE_COLOR, (screen.get_width() // 2, screen.get_height() // 2), radius)

        # Label
        if label:
            text_surface = font.render(label, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(60)


def breathing_session(pattern_name="Box Breathing", screen=None, play_music=True):
    if screen is None:
        info = pygame.display.Info()
        screen = pygame.display.set_mode((info.current_w, info.current_h))
    """Main breathing session."""
    if not pygame.get_init():
        pygame.init()
    if not pygame.mixer.get_init():
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

    pygame.display.set_caption("I-AM-ROOT Breathing")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 48, bold=True)

    # Load music
    if play_music and os.path.exists(CALM_MUSIC):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(CALM_MUSIC)
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1)

    # Load chime
    chime = None
    if os.path.exists(CHIME_SOUND):
        chime = pygame.mixer.Sound(CHIME_SOUND)
        chime.set_volume(0.5)

    pattern = PATTERNS.get(pattern_name, PATTERNS["Box Breathing"])
    cycles = pattern["cycles"]
    inhale_time = pattern["inhale"]
    hold_time = pattern["hold"]
    exhale_time = pattern["exhale"]

    print(f"\nStarting {pattern_name} session for {cycles} cycles...\n")
    for _ in range(cycles):
        animate_circle(screen, clock, font, inhale_time, MIN_RADIUS, MAX_RADIUS, label="Inhale", chime=chime)
        animate_circle(screen, clock, font, hold_time, MAX_RADIUS, MAX_RADIUS, label="Hold", hold=True, chime=chime)
        animate_circle(screen, clock, font, exhale_time, MAX_RADIUS, MIN_RADIUS, label="Exhale", chime=chime)
        animate_circle(screen, clock, font, hold_time, MIN_RADIUS, MIN_RADIUS, label="Hold", hold=True, chime=chime)

    print("\nBreathing session complete! 🌱")
    log_session(pattern_name, cycles)


def log_session(pattern_name, cycles):
    """Log completed breathing session to JSON."""
    log_file = os.path.join("logs", "breathing_sessions.json")
    os.makedirs("logs", exist_ok=True)
    data = []
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    data.append({"datetime": str(datetime.now()), "pattern": pattern_name, "cycles": cycles})
    with open(log_file, "w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    pattern_name = sys.argv[1] if len(sys.argv) > 1 else "Box Breathing"
    breathing_session(pattern_name)
