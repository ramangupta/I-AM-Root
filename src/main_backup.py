# src/main.py
import sys
import os
import time
import pygame
from breathing_visual_audio import breathing_session
from stories import show_free_story, show_premium_story
from quotes import show_quote  # assuming you have quote.py

# ------------------- Colors ------------------- #
GREEN = "\033[1;32m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

# ------------------- Helper Functions ------------------- #
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_input_buffer():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios
        termios.tcflush(sys.stdin, termios.TCIFLUSH)

def wait_for_enter():
    input("\nPress Enter to continue...")

def reading_animation(seconds=3):
    print(YELLOW + "\nGet Ready to focus on I AM ..." + RESET)
    for i in range(seconds, 0, -1):
        print(f"\rStarting in {i} second(s)... ", end='', flush=True)
        time.sleep(1)
    print("\n")

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

def print_menu():
    print(CYAN + "\n=================== I AM Root Menu ==================" + RESET)
    print(YELLOW + "[1]" + RESET + " 🌬️  Breathing Exercise")
    print(YELLOW + "[2]" + RESET + " 💬  Daily Quote")
    print(YELLOW + "[3]" + RESET + " ⏳  Focus Timer")
    print(YELLOW + "[4]" + RESET + " 🩺  System Health Check")
    print(YELLOW + "[5]" + RESET + " 📖  Free Motivational Story")
    print(YELLOW + "[6]" + RESET + " 🌟  Premium Motivational Story")
    print(YELLOW + "[q]" + RESET + " 🚪  Quit")

def typewriter_print(text, delay=0.01):
    """Prints text character by character for a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Newline at the end

def print_logo_animated():
    # Print ASCII logo in green
    print(GREEN)
    for line in logo_lines:
        typewriter_print(line, delay=0.005)
    print(RESET)

    # Print motivational lines in yellow
    print(YELLOW)
    for line in motivational_lines:
        typewriter_print(line, delay=0.01)
    print(RESET)

# ------------------- Animated Background ------------------- #
def animated_background(duration=5):
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("I-AM-ROOT Main Menu Animation")
    clock = pygame.time.Clock()
    
    CALM_MUSIC = os.path.join("assets", "calm_music1.wav")
    if os.path.exists(CALM_MUSIC):
        pygame.mixer.init(frequency=44100)
        pygame.mixer.music.load(CALM_MUSIC)
        pygame.mixer.music.set_volume(0.8)
        pygame.mixer.music.play(-1)  # loop indefinitely
    
    start_time = time.time()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.mixer.music.stop()
                break

        t = (time.time() - start_time)
        color1 = (int(50 + 50*t) % 256, 30, 100)
        color2 = (100, int(50 + 80*t) % 256, 200)
        screen.fill(color1)
        pygame.draw.circle(screen, color2, (WIDTH//2, HEIGHT//2), int(50 + 30*(t%1)))
        pygame.display.flip()
        clock.tick(60)


# ------------------- Main Function ------------------- #
def main():
    while True:
        animated_background(duration=1.5)
        clear_screen()
        print_logo_animated()
        print_menu()
        choice = input(YELLOW + "Enter your choice: " + RESET).strip()

        if choice == "1":
            reading_animation(2)
            breathing_session()
            wait_for_enter()
        elif choice == "2":
            reading_animation(2)
            show_quote()
            wait_for_enter()
        elif choice == "3":
            try:
                minutes = int(input("Enter focus duration in minutes: "))
                start_timer(minutes)
            except ValueError:
                print(YELLOW + "Invalid input." + RESET)
            wait_for_enter()
        elif choice == "4":
            print(YELLOW + "System Health Check not implemented yet." + RESET)
            wait_for_enter()
        elif choice == "5":
            reading_animation(2)
            show_free_story()
            wait_for_enter()
        elif choice == "6":
            reading_animation(2)
            show_premium_story(token=None)  # prompt for token inside function
            wait_for_enter()
        elif choice.lower() == "q":
            print(GREEN + "Goodbye, Stay with I AM! 🌱" + RESET)
            break
        else:
            print(YELLOW + "Invalid choice. Try again." + RESET)
            wait_for_enter()

if __name__ == "__main__":
    main()

