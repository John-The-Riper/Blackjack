import pygame
import random
import person
import card
class Blackjack:
    # Game functions
    def __init__(self, deck, player, dealer, screen):
        self.perm_deck = deck
        self.deck = deck
        self.player = player
        self.dealer = dealer
        self.screen = screen

        # Load and scale card back image to 20%
        original_back = pygame.image.load('card_back.png').convert_alpha()
        width = int(original_back.get_width() * 0.2)
        height = int(original_back.get_height() * 0.2)
        self.card_back_img = pygame.transform.smoothscale(original_back, (width, height))

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
            lstack = self.deck[0:len(self.deck) // 2]
            rstack = self.deck[(len(self.deck) // 2):]
            temp =[]
            for j in range(len(rstack)):
                temp.append(lstack[j])
                temp.append(rstack[j])
            self.deck = temp

    def random_shuffle(self):
        random.shuffle(self.deck)

    # PLaying the game

    def player_action(self, action):
        if action == 'hit':
            self.player.add_card(self.draw())
            print(self.player.get_value())
        elif action == 'stand':
           self.dealer_turn()

    # Dealer functions

    def dealer_stand(self):
        print("dealer stood")
        print(self.dealer.get_value())

    def dealer_turn(self):
        self.dealer_hidden = False
        while self.dealer.get_value() < 17:
            self.dealer.add_card(self.draw())
            print(self.dealer.get_value())
        self.dealer_stand()
 # Screen functions
    def draw_hand(self, person, start_x, start_y, hide_second_card=False):
        card_spacing = 100
        for i, card in enumerate(person.get_hand()):
            card.move(start_x + i * card_spacing, start_y)
            if person == self.dealer and hide_second_card and i == 1:
                rect = self.card_back_img.get_rect(center=(start_x + i * card_spacing, start_y))
                self.screen.blit(self.card_back_img, rect)
            else:
                card.update(self.screen)

# Starting game
    def starting_game(self):
       self.random_shuffle()
       self.dealer_hidden = True
       self.player.add_card(self.draw())
       self.dealer.add_card(self.draw())
       self.player.add_card(self.draw())
       self.dealer.add_card(self.draw())
       print(self.player.get_value())

    def run(self):
        running = True
        allow_press_0 = True
        allow_press_1 = False
        allow_press_2 = False
        self.starting_game()
        while running:
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
                        self.player_action('hit')
                    elif event.key == pygame.K_2 and allow_press_2:
                        self.player_action('stand')
                        allow_press_1 = False
                        allow_press_2 = False
            self.draw_hand(self.dealer, start_x=400, start_y=150, hide_second_card=self.dealer_hidden)
            self.draw_hand(self.player, start_x=400, start_y=500)

            # Update the screen with the active surface
            pygame.display.flip()
            # Game FPS
