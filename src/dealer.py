from typing import List
from cards import Card, Deck


class Dealer():
    def __init__(self):
        self.deck = Deck()
        self.community_cards: List[Card] = []

        self.deck.shuffle()

    def deal_to_players(self):
        pass

    def deal_flop(self):
        assert (len(self.community_cards) == 0)
        assert (len(self.deck.burned) == 0)

        self.deck.burn()
        self.community_cards.append(self.deck.draw())
        self.community_cards.append(self.deck.draw())
        self.community_cards.append(self.deck.draw())

    def deal_turn(self):
        assert (len(self.community_cards) == 3)
        assert (len(self.deck.burned) == 1)

        self.deck.burn()
        self.community_cards.append(self.deck.draw())

    def deal_river(self):
        assert (len(self.community_cards) == 4)
        assert (len(self.deck.burned) == 2)

        self.deck.burn()
        self.community_cards.append(self.deck.draw())
