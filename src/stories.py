import os
import random
import requests
import time
import sys

# ------------------- Paths ------------------- #
FREE_DIR = os.path.join(os.path.dirname(__file__), "stories", "free")

# Remote premium stories
PREMIUM_FILES = ["story1.txt", "story2.txt", "story3.txt", "story4.txt", "story5.txt"]
PREMIUM_BASE_URL = "https://raw.githubusercontent.com/ramangupta/I-AM-Root-Premium/main/stories/"

# ------------------- Helpers ------------------- #
def load_story(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def show_banner(title="Motivational Story"):
    print("\033[1;32m" + "="*60 + "\033[0m")
    print("\033[1;36m" + f"       {title}       " + "\033[0m")
    print("\033[1;32m" + "="*60 + "\033[0m\n")

def reading_animation(duration=3):
    """Countdown before showing story text."""
    print("\n\033[1;33mGet ready to read...\033[0m")
    for i in range(duration, 0, -1):
        sys.stdout.write(f"\rStarting in {i} second(s)... ")
        sys.stdout.flush()
        time.sleep(1)
    print("\n")

def print_story_text(story_text, scroll=False):
    """Print story with optional scrolling effect."""
    if scroll:
        for line in story_text.splitlines():
            print(line)
            time.sleep(0.2)
    else:
        print(story_text)

# ------------------- Free Stories ------------------- #
def show_free_story(scroll=False):
    files = [os.path.join(FREE_DIR, f) for f in os.listdir(FREE_DIR) if f.endswith(".txt")]
    if not files:
        print("\033[1;33mNo free stories found!\033[0m")
        return

    story = random.choice(files)
    show_banner("Free Motivational Story")
    reading_animation(duration=3)
    print("\033[1;36m")  # cyan
    print_story_text(load_story(story), scroll)
    print("\033[0m")
    print("\n" + "\033[1;32m" + "="*60 + "\033[0m")
    input("\nPress Enter to continue...")

# ------------------- Premium Stories ------------------- #
def show_premium_story(token, scroll=False):
    headers = {"Authorization": f"token {token}"}
    story_file = random.choice(PREMIUM_FILES)

    # Use GitHub API to get private content
    api_url = f"https://api.github.com/repos/ramangupta/I-AM-Root-Premium/contents/stories/{story_file}"
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        import base64
        data = response.json()
        story_text = base64.b64decode(data["content"]).decode("utf-8")

        show_banner("Premium Motivational Story")
        reading_animation(duration=3)
        print("\033[1;35m")  # magenta
        print_story_text(story_text, scroll)
        print("\033[0m")
        print("\n" + "\033[1;32m" + "="*60 + "\033[0m")
        input("\nPress Enter to continue...")
    else:
        print(f"\033[1;33mFailed to fetch premium story. Status: {response.status_code}\033[0m")

# ------------------- CLI Entry ------------------- #
if __name__ == "__main__":
    import sys
    scroll = True  # optional scrolling effect
    if "--premium" in sys.argv:
        user_token = input("Enter your GitHub token to unlock premium stories: ").strip()
        show_premium_story(user_token, scroll=scroll)
    else:
        show_free_story(scroll=scroll)
