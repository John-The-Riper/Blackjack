import pygame

class Blackjack:
    def _init_(self, deck):
        self.perm_deck = deck
        self.deck = deck

    def draw(self):
        if len(self.deck) > 0:
            self.deck.pop()

        else:
            self.reset()
            self.shuffle(2)

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
