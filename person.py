# import pygame
#
# def calculate_hand_value(hand):
#     value = 0
#     ace_count = 0
#
#     for card in hand:
#         rank = card['rank']
#         if rank.isdigit():
#             value += int(rank)
#         elif rank in ['Jack', 'Queen', 'King']:
#             value += 10
#         elif rank == 'Ace':
#             ace_count += 1
#             value += 11
#
#     while value > 21 and ace_count:
#         value -= 10
#         ace_count -= 1
#
#     return value
#
# player_hand = []

class Person:
    def __init__(self, money):
        self.money = money
        self.cards = []
        self.card_value = 0

    def add_card(self, card):
        self.cards.append(card)
        self.card_value += card.value

    def get_value(self):
        return self.card_value
