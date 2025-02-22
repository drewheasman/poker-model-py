from typing import List
from cards import Card


class Player():
    def __init__(self, name):
        self.name = name
        self.cards: List[Card] = []

    def give_card(self, card: Card):
        assert len(self.cards) < 2
        self.cards.append(card)

    def retrieve_cards(self):
        to_return = self.cards.copy()
        self.cards = []
        return to_return
