import pygame
pygame.mixer.init()
pygame.mixer.music.load("assets/calm_music1.mp3")
pygame.mixer.music.play()
input("Press Enter to stop...")
pygame.mixer.music.stop()
pygame.mixer.quit()

