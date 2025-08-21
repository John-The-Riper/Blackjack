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

# Game variables
player_hand = 0

# Functions
def player_hit():
    global player_hand
    player_hand += 1
    print(player_hand)

def screen_settings():
    screen = pygame.display.set_mode((475, 475))
    pygame.display.set_caption("Blackjack")
    screen.fill(GREEN)
    pygame.display.flip()
    return screen

def start_game():
    running = True
    screen_settings()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_1:
                    player_hit()
    pygame.quit()
    sys.exit()

# Start the game loop
start_game()
