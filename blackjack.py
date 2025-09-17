import pygame
import person
import card
class Blackjack:
    # Game functions
    def __init__(self, deck, player, dealer):
        self.perm_deck = deck
        self.deck = deck
        self.player = player
        self.dealer = dealer

    def draw(self):
        if len(self.deck) > 0:
            return self.deck.pop()

        else:
            self.reset()
            self.shuffle(2)
            return self.deck.pop()

    def reset(self):
        self.deck = self.perm_deck

    def shuffle(self, n):
        for i in range(n):
            lstack = self.deck[0:len(self.deck //2)]
            rstack = self.deck[len(self.deck // 2) + 1:]
            temp =[]
            for j in range(len(lstack)):
                temp.append(lstack[i])
                temp.append(rstack[i])
            self.deck = temp

    # PLaying the game

    def player_action(self, action):
        if action == 'hit':
            self.player.add_card(self.deck.draw())
            self.player.get_value()
        elif action == 'stand':
            dealer_turn = True
            self.dealer_controls()


    def dealer_controls(self):
        self.dealer.add_card(self.deck.draw())

# STARTING GAME - DEALING CARDS TO PLAYER AND DEALER AND GIVING PLAYER TURN
    def starting_game(self):
       self.player.add_card(self.deck.draw())
       self.dealer.add_card(self.deck.draw())
       self.player.add_card(self.deck.draw())
       self.dealer.add_card(self.deck.draw())
       print(self.player.get_value())
       print(self.dealer.get_value())
    def run(self):
        running = True
        allow_press_0 = True
        allow_press_1 = False
        allow_press_2 = False

        while running:
            global player_action
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_SPACE and allow_press_0:
                        allow_press_1 = True
                        allow_press_2 = True
                        allow_press_0 = False
                    elif event.key == pygame.K_1 and allow_press_1:
                        player_action('hit')
                    elif event.key == pygame.K_2 and allow_press_2:
                        player_action('stand')
                        allow_press_1 = False
                        allow_press_2 = False

#player.add_card(self.deck.draw())

            # Update the screen with the active surface
            pygame.display.flip()
            # Game FPS
        self.player.add_cards(self.draw())
