import os
import random
import requests
import time
import sys

# ------------------- Colors ------------------- #
GREEN = "\033[1;32m"
CYAN = "\033[1;36m"
MAGENTA = "\033[1;35m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

# ------------------- Paths ------------------- #
FREE_DIR = os.path.join(os.path.dirname(__file__), "stories", "free")
PREMIUM_FILES = ["story1.txt", "story2.txt", "story3.txt", "story4.txt", "story5.txt"]
PREMIUM_BASE_URL = "https://raw.githubusercontent.com/ramangupta/I-AM-Root-Premium/main/stories/"

# ------------------- Helpers ------------------- #
def typewriter(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_banner(title):
    clear_screen()
    print(GREEN + "="*60 + RESET)
    print(CYAN + f"🌱  {title}  🌱".center(60) + RESET)
    print(GREEN + "="*60 + RESET + "\n")

def reading_animation(duration=3):
    print(YELLOW + "\nGet ready to read..." + RESET)
    for i in range(duration, 0, -1):
        sys.stdout.write(f"\rStarting in {i} second(s)... ")
        sys.stdout.flush()
        time.sleep(1)
    print("\n")

def print_story_text(story_text, scroll=False):
    if scroll:
        for line in story_text.splitlines():
            print(line)
            time.sleep(0.15)
    else:
        print(story_text)

# ------------------- Free Stories ------------------- #
def show_free_story(scroll=False):
    files = [os.path.join(FREE_DIR, f) for f in os.listdir(FREE_DIR) if f.endswith(".txt")]
    if not files:
        print(YELLOW + "No free stories found!" + RESET)
        return
    story = random.choice(files)
    show_banner("Free Motivational Story")
    reading_animation()
    print(CYAN)
    print_story_text(load_story(story), scroll)
    print(RESET)
    print(GREEN + "="*60 + RESET)
    input("\nPress Enter to return to menu...")

def load_story(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# ------------------- Premium Stories ------------------- #
def show_premium_story(token, scroll=False):
    headers = {"Authorization": f"token {token}"}
    story_file = random.choice(PREMIUM_FILES)
    api_url = f"https://api.github.com/repos/ramangupta/I-AM-Root-Premium/contents/stories/{story_file}"
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        import base64
        data = response.json()
        story_text = base64.b64decode(data["content"]).decode("utf-8")
        show_banner("Premium Motivational Story")
        reading_animation()
        print(MAGENTA)
        print_story_text(story_text, scroll)
        print(RESET)
        print(GREEN + "="*60 + RESET)
        input("\nPress Enter to return to menu...")
    else:
        print(YELLOW + f"Failed to fetch premium story. Status: {response.status_code}" + RESET)
        input("\nPress Enter to return to menu...")

# ------------------- Menu ------------------- #
def main_menu():
    scroll = True
    while True:
        show_banner("I AM Root — Motivation Hub")
        typewriter(f"{YELLOW}[1]{RESET} 📖 Read a Free Motivational Story", 0.01)
        typewriter(f"{YELLOW}[2]{RESET} 🌟 Read a Premium Motivational Story", 0.01)
        typewriter(f"{YELLOW}[q]{RESET} 🚪 Quit", 0.01)
        print()
        choice = input(YELLOW + "Enter your choice: " + RESET).strip().lower()

        if choice == "1":
            show_free_story(scroll)
        elif choice == "2":
            token = os.getenv("GITHUB_TOKEN")
            if not token:
                token = input("Enter your GitHub token to unlock premium stories: ").strip()
            show_premium_story(token, scroll)
        elif choice == "q":
            clear_screen()
            print(GREEN + "Goodbye! Stay motivated! 🌱" + RESET)
            break
        else:
            print(YELLOW + "Invalid choice, please try again." + RESET)
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
