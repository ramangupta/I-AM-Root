import pygame
import time
import os

MUSIC_FILE = os.path.join("assets", "calm_music1.mp3")

def play_music():
    if not os.path.exists(MUSIC_FILE):
        print(f"Music file not found: {MUSIC_FILE}")
        return
    try:
        print(f"Resetting previous mixer")
        pygame.mixer.quit()  # reset any previous mixer state
        pygame.mixer.init()
        pygame.mixer.music.load(MUSIC_FILE)
        pygame.mixer.music.play(-1)
    except pygame.error as e:
        print(f"Audio playback error: {e}")

def stop_music():
    try:
        if pygame.mixer.get_init():  # only stop if mixer is initialized
            pygame.mixer.music.stop()
            pygame.mixer.quit()
    except:
        pass

def breathing_session(cycles=4):
    print("\nStarting breathing session...\n")
    for cycle in range(cycles):
        print(f"\nCycle {cycle + 1} of {cycles}")
        print("Inhale... with 'I'")
        time.sleep(3)
        print("Hold...")
        time.sleep(2)
        print("Exhale... with 'AM'")
        time.sleep(3)
        print("Hold...")
        time.sleep(2)
    print("\nBreathing session complete.")

def start_breathing_with_music(cycles=4):
    play_music()
    try:
        breathing_session(cycles)
    finally:
        stop_music()
        print("\nMusic stopped. Hope you feel relaxed! 🌱")

if __name__ == "__main__":
    input("Press Enter to start the breathing exercise...")
    start_breathing_with_music(cycles=4)
