import pygame
import json
from card import Card
from person import Person
from blackjack import Blackjack


SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

def main():
    ##############################################
    # Pygame initialization
    ##############################################
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    running = True
    screen.fill((0, 0, 0))

    ##############################################
    # Card object creation
    ##############################################

    # List that will store our card objects. We will be using it as a "stack" in this example.
    cards = []

    # Open the JSON file and load the contents into a list
    json_path = "./card_setup.json"
    with open(json_path, 'r') as c:
        json_card_list = json.load(c)

    # For each item in the list, create a card object and append it to our list of cards.
    for entry in json_card_list:
        cards.append(Card(entry["name"], entry["path"], entry["value"], entry["suit"]))

    ##############################################
    # Game Setup
    ##############################################
    player = Person(100)
    game = Blackjack(cards, player)


    ##############################################
    # Game loop
    ##############################################
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_1 and allow_press_1:
                    player_action('hit')
                elif event.key == pygame.K_2 and allow_press_2:
                    player_action('stand')
                    allow_press_1 = False
                    allow_press_2 = False

        # Update the screen with the active surface
        pygame.display.flip()
        # Game FPS
        clock.tick(30)



if __name__ == '__main__':
    main()