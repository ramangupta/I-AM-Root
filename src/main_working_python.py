# src/main.py
import os
import pygame
import time
from breathing_visual_audio import breathing_session
from stories import show_free_story, show_premium_story
from quotes import show_quote  # assuming you have quotes.py

class Leaf:
    def __init__(self, img, screen_w, screen_h):
        self.img = img
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.reset()

    def reset(self):
        self.x = random.randint(0, self.screen_w)
        self.y = random.randint(-self.screen_h, 0)
        self.speed_y = random.uniform(1, 3)
        self.speed_x = random.uniform(-0.5, 0.5)
        self.angle = random.uniform(0, 360)
        self.rotation_speed = random.uniform(-1, 1)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.angle += self.rotation_speed
        if self.y > self.screen_h:
            self.reset()

    def draw(self, surface):
        rotated = pygame.transform.rotate(self.img, self.angle)
        rect = rotated.get_rect(center=(self.x, self.y))
        surface.blit(rotated, rect.topleft)

def draw_gradient_background(surface, time_elapsed):
    w, h = surface.get_size()
    color1 = (int(50 + 30 * math.sin(time_elapsed / 2000)),
              int(50 + 30 * math.sin(time_elapsed / 3000)),
              int(50 + 30 * math.sin(time_elapsed / 2500)))
    color2 = (0, 0, 0)

    for y in range(h):
        r = color1[0] + (color2[0] - color1[0]) * y // h
        g = color1[1] + (color2[1] - color1[1]) * y // h
        b = color1[2] + (color2[2] - color1[2]) * y // h
        pygame.draw.line(surface, (r, g, b), (0, y), (w, y))

# ---------------- Colors ---------------- #
BLACK = (0, 0, 0)
GREEN = (50, 205, 50)
YELLOW = (255, 215, 0)
CYAN = (0, 255, 255)

# ---------------- Assets ---------------- #
ASSETS = os.path.join(os.path.dirname(__file__), "..", "assets")
LOGO_FONT_PATH = os.path.join(ASSETS, "consola.ttf")
EMOJI_FONT_PATH = os.path.join(ASSETS, "seguiemj.ttf")
CALM_MUSIC = os.path.join(ASSETS, "calm_music1.wav")

# ---------------- Text ---------------- #
logo_lines = [
    "===============================================================",
    "   ██╗ █████╗ ███╗   ███╗    ██████╗  ██████╗  ██████╗ ████████╗",
    "   ██║██╔══██╗████╗ ████║    ██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝",
    "   ██║███████║██╔████╔██║    ██████╔╝██║   ██║██║   ██║   ██║   ",
    "   ██║██╔══██║██║╚██╔╝██║    ██╔\\═══ ██║   ██║██║   ██║   ██║   ",
    "   ██║██║  ██║██║ ╚═╝ ██║    ██║ \\  ╚ ██████╔╝╚██████╔╝   ██║   ",
    "   ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝    ╚═╝  \\   ╚═════╝  ╚═════╝    ╚═╝   "
]

motivational_lines = [
    "   🌱  Root yourself in calm. Grow your system. 🌱",
    "============================================================",
    "🪴 I AM is the root of all. There is nothing else to know 🪴",
    "                       🌱",
    "                     🌿 🌿",
    "                  🌿   🌿   🌿",
    "                 Stay focused. 🚀",
    "============================================================"
]

menu_options = [
    "[1] 🌬️  Breathing Exercise",
    "[2] 💬  Daily Quote",
    "[3] ⏳  Focus Timer",
    "[4] 🩺  System Health Check",
    "[5] 📖  Free Motivational Story",
    "[6] 🌟  Premium Motivational Story",
    "[Q] 🚪  Quit"
]

# ---------------- Helper ---------------- #
def typewriter_text(surface, font, text, color, pos, delay=0.01):
    x, y = pos
    for char in text:
        char_surf = font.render(char, True, color)
        surface.blit(char_surf, (x, y))
        pygame.display.update()
        x += char_surf.get_width()
        time.sleep(delay)

# ---------------- Main ---------------- #
def main():
    pygame.init()
    info = pygame.display.Info()
    screen = pygame.display.set_mode((info.current_w, info.current_h))
    pygame.display.set_caption("I-AM-ROOT")
    clock = pygame.time.Clock()

    # Fonts
    logo_font = pygame.font.Font(LOGO_FONT_PATH, 32)
    emoji_font = pygame.font.Font(EMOJI_FONT_PATH, 32)
    menu_font = pygame.font.Font(EMOJI_FONT_PATH, 28)

    # Load leaf image (or placeholder)
    leaf_img = pygame.Surface((20, 10), pygame.SRCALPHA)
    pygame.draw.ellipse(leaf_img, (34, 139, 34), [0, 0, 20, 10])

    leaves = [Leaf(leaf_img, info.current_w, info.current_h) for _ in range(20)]

    # Music
    if os.path.exists(CALM_MUSIC):
        pygame.mixer.init()
        pygame.mixer.music.load(CALM_MUSIC)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

    # Draw logo + motivational text + menu once
    screen.fill(BLACK)
    y_offset = 50
    for line in logo_lines:
        typewriter_text(screen, logo_font, line, GREEN, (50, y_offset), delay=0.002)
        y_offset += logo_font.get_height() + 2

    y_offset += 20
    for line in motivational_lines:
        typewriter_text(screen, emoji_font, line, YELLOW, (50, y_offset), delay=0.005)
        y_offset += emoji_font.get_height() + 2

    y_offset += 30
    for line in menu_options:
        text_surf = menu_font.render(line, True, CYAN)
        screen.blit(text_surf, (50, y_offset))
        y_offset += menu_font.get_height() + 10

    pygame.display.update()

    # ---------------- Event loop ---------------- #
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_1, pygame.K_KP1]:
                    breathing_session()
                elif event.key in [pygame.K_2, pygame.K_KP2]:
                    show_quote()
                elif event.key in [pygame.K_3, pygame.K_KP3]:
                    print("Focus Timer not implemented yet.")
                elif event.key in [pygame.K_4, pygame.K_KP4]:
                    print("System Health Check not implemented yet.")
                elif event.key in [pygame.K_5, pygame.K_KP5]:
                    show_free_story()
                elif event.key in [pygame.K_6, pygame.K_KP6]:
                    show_premium_story(token=None)
                elif event.key in [pygame.K_q, pygame.K_ESCAPE]:
                    running = False

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

