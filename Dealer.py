class Dealer:
    def __init__(self, money):
        self.money = money
        self.cards = []
        self.card_value = 0

    def add_card(self, card):
        self.cards.append(card)
        self.card_value += card.get_value()

    def get_value(self):
        return self.card_value