class Person:
    def __init__(self, money):
        self.money = money
        self.cards = []
        self.card_value = 0

    def get_hand(self):
        return self.cards

    def add_card(self, card):
       #print(card.get_name())
        self.cards.append(card)
        self.card_value += card.get_value()

    def get_value(self):
        return self.card_value