import pygame
import person
class Blackjack:
    def _init_(self, deck, player):
        self.perm_deck = deck
        self.deck = deck
        self.player = player

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

    def player_action(self, action):
        global player_hand_value, player_hand, dealer_turn
        if action == 'hit':
            self.player.add_card(self.deck.draw())

        elif action == 'stand':
            dealer_turn = True
            self.dealer_controls()


    def dealer_controls(self):
        print("Hello world")


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
            clock.tick(30)
        self.player.add_cards(self.draw())
