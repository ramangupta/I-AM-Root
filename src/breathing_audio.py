# src/breathing_audio.py
import pygame
import time
import os

pygame.mixer.init()

# Use WAV files
INHALE_SOUND = os.path.join("assets", "inhale.wav")
HOLD_SOUND   = os.path.join("assets", "hold.wav")
EXHALE_SOUND = os.path.join("assets", "exhale.wav")

inhale_time = 3
hold_time   = 2
exhale_time = 3
cycles      = 4

def play_sound(file):
    if os.path.exists(file):
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
    else:
        print(f"Audio file not found: {file}")

def start_breathing_audio(cycles=cycles):
    print("\nStarting audio-only breathing session...\n")
    for i in range(cycles):
        print(f"Cycle {i+1} of {cycles}")

        print("Inhale...")
        play_sound(INHALE_SOUND)
        time.sleep(inhale_time)

        print("Hold...")
        play_sound(HOLD_SOUND)
        time.sleep(hold_time)

        print("Exhale...")
        play_sound(EXHALE_SOUND)
        time.sleep(exhale_time)

        print("Hold...")
        time.sleep(hold_time)

    print("\nBreathing session complete. 🌱")

if __name__ == "__main__":
    input("Press Enter to start the audio-only breathing session...")
    start_breathing_audio()
