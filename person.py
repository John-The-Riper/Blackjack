class Person:
    def __init__(self, money):
        self.money = money
        self.cards = []

    def get_hand(self):
        return self.cards

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        total = 0
        aces = 0

        for card in self.cards:
            value = card.get_value()
            total += value
            if value == 11:  # count Ace
                aces += 1

        while total > 21 and aces > 0:
            total -= 10 
            aces -= 1

        return total
