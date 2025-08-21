import pygame
import random
import sys

pygame.init()

# Colors for the game screen
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 100, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)


# Game variables and functions
def screen_settings():
    screen = pygame.display.set_mode((475, 475))
    screen.fill((GREEN))
    pygame.display.flip()
    return screen


def deck_of_cards():
    deck = []


# Start game has the while loop that runs the game
def start_game():
    running = True
    screen_settings()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

    pygame.quit()


start_game()
sys.exit()