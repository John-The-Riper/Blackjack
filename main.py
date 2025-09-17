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

    print(len(cards))
    ##############################################
    # Game Setup
    ##############################################
    player = Person(100)
    dealer = Person(100)
    game = Blackjack(cards, player, dealer)


    ##############################################
    # Game loop
    ##############################################
    game.run()




if __name__ == '__main__':
    main()