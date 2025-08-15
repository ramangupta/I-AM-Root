# src/main.py
import os
import pygame
import time
import random
import math
from datetime import datetime
from breathing_visual_audio import breathing_session
from stories import show_free_story, show_premium_story
from quotes import show_quote  # assuming you have quotes.py

# --- Flower image ---
flower_img = pygame.Surface((16, 16), pygame.SRCALPHA)
pygame.draw.circle(flower_img, (255, 100, 150), (8, 8), 8)  # flower outer
pygame.draw.circle(flower_img, (255, 200, 50), (8, 8), 4)   # flower center

class Leaf:
    def __init__(self, img, screen_w, screen_h):
        self.base_img = img
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.reset()

    def reset(self):
        self.x = random.randint(0, self.screen_w)
        self.y = random.randint(-self.screen_h, 0)
        self.speed_y = random.uniform(1, 3)
        self.angle = random.uniform(0, 360)
        self.rotation_speed = random.uniform(-1, 1)
        self.size_factor = random.uniform(0.5, 1.2)
        self.alpha = random.randint(100, 255)
        self.wind_offset = random.uniform(0, 1000)

        # Resize image based on size_factor
        w, h = self.base_img.get_size()
        self.img = pygame.transform.smoothscale(self.base_img, (int(w * self.size_factor), int(h * self.size_factor)))
        self.img.set_alpha(self.alpha)

    def update(self, frame):
        # vertical fall
        self.y += self.speed_y
        # horizontal wind sway
        self.x += math.sin((self.y + self.wind_offset) / 30) * 0.5
        # rotation
        self.angle += self.rotation_speed

        if self.y > self.screen_h:
            self.reset()

    def draw(self, surface):
        rotated = pygame.transform.rotate(self.img, self.angle)
        rect = rotated.get_rect(center=(self.x, self.y))
        surface.blit(rotated, rect.topleft)


class Shoot:
    def __init__(self, x, max_height, leaf_img=None, flower_img=None):
        self.x = x
        self.max_height = max_height
        self.height = 0
        self.growth_speed = random.uniform(1, 2.5)
        self.color = (34, 139, 34)  # stem color
        self.leaves = []
        self.leaf_img = leaf_img
        self.flower_img = flower_img
        self.flower_added = False

    def update(self):
        # Grow stem
        if self.height < self.max_height:
            self.height += self.growth_speed
            # Chance to add a leaf
            if random.random() < 0.08:
                leaf_x_offset = random.choice([-10, 10])
                leaf_size = random.uniform(8, 15)
                self.leaves.append({
                    "y": self.height,
                    "x_offset": leaf_x_offset,
                    "angle": random.uniform(-25, 25),
                    "size": leaf_size
                })

        # Add flower at the top when fully grown
        if self.height >= self.max_height and not self.flower_added:
            self.flower_added = True

    def draw(self, screen, ground_y, frame):
        # --- Draw stem ---
        points = []
        for h in range(int(self.height)):
            sway = math.sin((h / 10) + (frame / 20)) * 2
            points.append((self.x + sway, ground_y - h))
        if len(points) > 1:
            pygame.draw.lines(screen, self.color, False, points, 2)

        # --- Draw leaves ---
        for leaf in self.leaves:
            leaf_y = ground_y - leaf["y"]
            sway_angle = leaf["angle"] + math.sin(frame / 15 + leaf["y"] / 15) * 5
            if self.leaf_img:
                rotated = pygame.transform.rotate(self.leaf_img, sway_angle)
                rect = rotated.get_rect(center=(self.x + leaf["x_offset"], leaf_y))
                screen.blit(rotated, rect.topleft)
            else:
                end_x = self.x + leaf["x_offset"] + math.cos(math.radians(sway_angle)) * leaf["size"]
                end_y = leaf_y + math.sin(math.radians(sway_angle)) * leaf["size"] / 2
                pygame.draw.line(screen, (50, 205, 50),
                                 (self.x + leaf["x_offset"], leaf_y),
                                 (end_x, end_y), 3)

        # --- Draw flower ---
        if self.flower_added:
            flower_y = ground_y - self.height
            if self.flower_img:
                rect = self.flower_img.get_rect(center=(self.x, flower_y))
                screen.blit(self.flower_img, rect.topleft)
            else:
                # simple circular flower
                pygame.draw.circle(screen, (255, 100, 150), (int(self.x), int(flower_y)), 8)


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

class Firefly:
    def __init__(self, screen_w, screen_h):
        self.x = random.uniform(0, screen_w)
        self.y = random.uniform(0, screen_h)
        self.prev_positions = [(self.x, self.y)]  # store trail positions
        self.angle = random.uniform(0, math.pi * 2)
        self.speed = random.uniform(0.2, 0.5)
        self.phase = random.uniform(0, math.pi * 2)
        self.size = random.randint(2, 4)
        self.screen_w = screen_w
        self.screen_h = screen_h

    def update(self, frame, mouse_pos=None):
        # Slight wandering
        self.angle += random.uniform(-0.02, 0.02)
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

        # Attracted to mouse if provided
        if mouse_pos:
            dx = mouse_pos[0] - self.x
            dy = mouse_pos[1] - self.y
            self.x += dx * 0.002  # attraction strength
            self.y += dy * 0.002

        # Keep within screen
        self.x %= self.screen_w
        self.y %= self.screen_h

        # Update trail
        self.prev_positions.append((self.x, self.y))
        if len(self.prev_positions) > 10:  # limit trail length
            self.prev_positions.pop(0)

    def draw(self, surface, frame):
        flicker = (math.sin(frame / 10 + self.phase) + 1) / 2
        brightness = int(150 + 105 * flicker)
        color = (brightness, brightness, 100)
        
        # Draw normally
        pygame.draw.circle(surface, color, (int(self.x), int(self.y)), self.size)
        
        # Optional: soft glow
        for i in range(1, 4):
            alpha = max(10, 50 - i*10)
            glow_surf = pygame.Surface((self.size*4, self.size*4), pygame.SRCALPHA)
            glow_color = (*color, alpha)  # RGBA
            pygame.draw.circle(glow_surf, glow_color, (self.size*2, self.size*2), self.size + i*2)
            surface.blit(glow_surf, (int(self.x)-self.size*2, int(self.y)-self.size*2))



def draw_text_with_shadow_glow(surface, font, text, base_color, pos, frame):
    x, y = pos

    # --- PULSING COLOR ---
    pulse = (math.sin(frame / 15) + 1) / 2  # 0 → 1
    r = min(255, int(base_color[0] + 150 * pulse))
    g = min(255, int(base_color[1] + 150 * pulse))
    b = min(255, int(base_color[2] + 150 * pulse))
    color = (r, g, b)

    # --- MULTI-LAYER GLOW ---
    for i in range(1, 5):
        alpha = max(10, 80 - i * 15)
        glow_surf = font.render(text, True, (0,0,0))
        glow_surf.set_alpha(alpha)
        surface.blit(glow_surf, (x + i, y + i))
        surface.blit(glow_surf, (x - i, y + i))
        surface.blit(glow_surf, (x + i, y - i))
        surface.blit(glow_surf, (x - i, y - i))

    # --- MAIN TEXT ---
    text_surf = font.render(text, True, color)
    surface.blit(text_surf, (x, y))

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
    "                           WELCOME TO NIRVANA                             ",
    "==========================================================================",
    "      ██╗   █████╗ ███╗   ███╗    ██████╗  ██████╗  ██████╗ ████████╗",
    "      ██║  ██╔══██╗████╗ ████║    ██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝",
    "      ██║  ███████║██╔████╔██║    ██████╔╝██║   ██║██║   ██║   ██║   ",
    "      ██║  ██╔══██║██║╚██╔╝██║    ██╔══██╗██║   ██║██║   ██║   ██║   ",
    "      ██║  ██║  ██║██║ ╚═╝ ██║    ██║  ██║╚██████╔╝╚██████╔╝   ██║   ",
    "      ╚═╝  ╚═╝  ╚═╝╚═╝     ╚═╝    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝   "
]

motivational_lines = [
    "                            🌱  Root yourself in calm. Let Awareness be your anchor 🌱",
    "============================================================",
    "                            🪴 I AM is the root of all. There is nothing else to know 🪴",
    "                                                                             ",
    "                                                               🌱",
    "                                                           🌿 🌿",
    "                                                       🌿   🌿   🌿",
    "                                                                               ",
    "                                                  🪴 Dwell in I AM. 🪴",
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

    logo_font = pygame.font.Font(LOGO_FONT_PATH, 32)
    emoji_font = pygame.font.Font(EMOJI_FONT_PATH, 32)
    menu_font = pygame.font.Font(EMOJI_FONT_PATH, 24)

    # Load leaf image (or placeholder)
    leaf_img = pygame.Surface((20, 10), pygame.SRCALPHA)
    pygame.draw.ellipse(leaf_img, (34, 139, 34), [0, 0, 20, 10])

    leaves = [Leaf(leaf_img, info.current_w, info.current_h) for _ in range(20)]
    shoots = [Shoot(random.randint(50, info.current_w - 50), random.randint(80, 200),
              leaf_img=leaf_img, flower_img=flower_img)
              for _ in range(20)]  # more shoots
    fireflies = [Firefly(info.current_w, info.current_h) for _ in range(15)]

    if os.path.exists(CALM_MUSIC):
        pygame.mixer.init()
        pygame.mixer.music.load(CALM_MUSIC)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

    # First draw (typing effect)
    screen.fill(BLACK)
    y_offset = 50
    for line in logo_lines:
        typewriter_text(screen, logo_font, line, GREEN, (50, y_offset), delay=0.002)
        y_offset += logo_font.get_height() + 2
    y_offset += 20
    for line in motivational_lines:
        typewriter_text(screen, emoji_font, line, YELLOW, (50, y_offset), delay=0.005)
        y_offset += emoji_font.get_height() + 2
    pygame.display.update()

    running = True
    start_time = pygame.time.get_ticks()
    frame = 0

    while running:
        frame += 1
        elapsed = pygame.time.get_ticks() - start_time

        # --- BACKGROUND ---
        draw_gradient_background(screen, elapsed)

        # --- ANIMATIONS ---
        for leaf in leaves:
            leaf.update(frame)
            leaf.draw(screen)

        for shoot in shoots:
            shoot.update()
            shoot.draw(screen, info.current_h - 10, frame)

        mouse_pos = pygame.mouse.get_pos()
        for firefly in fireflies:
            firefly.update(frame, mouse_pos)
            firefly.draw(screen, frame)

        # --- TEXT LAYER ---
        y_offset = 50
        for line in logo_lines:
            draw_text_with_shadow_glow(screen, logo_font, line, GREEN, (50, y_offset), frame)
            y_offset += logo_font.get_height() + 2

        y_offset += 20
        for line in motivational_lines:
            draw_text_with_shadow_glow(screen, emoji_font, line, YELLOW, (50, y_offset), frame)
            y_offset += emoji_font.get_height() + 2

        y_offset += 30
        for line in menu_options:
            text_surf = menu_font.render(line, True, CYAN)
            screen.blit(text_surf, (50, y_offset))
            y_offset += menu_font.get_height() + 10

        # --- DISPLAY ---
        pygame.display.flip()

        # --- INPUT HANDLING ---
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
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:  # Press S to save screenshot
                        os.makedirs("assets", exist_ok=True)  # Make sure folder exists
                        pygame.image.save(screen, "assets/screenshot.png")
                        print("📸 Screenshot saved to assets/screenshot.png")

        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
