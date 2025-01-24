from typing import List
from cards import Card, Deck
from player import Player


class Dealer():
    def __init__(self):
        self.deck = Deck()
        self.community_cards: List[Card] = []

        print("dealer: shuffling")
        self.deck.shuffle()

    def deal_to_players(self, players: List[Player]):
        # First card
        print("dealer: dealing player first cards")
        for p in players:
            p.give_card(self.deck.draw())
        # Second card
        print("dealer: dealing player second cards")
        for p in players:
            p.give_card(self.deck.draw())

    def deal_flop(self):
        assert len(self.community_cards) == 0
        assert len(self.deck.burned) == 0

        print("dealer: dealing flop")
        self.deck.burn()
        self.community_cards.append(self.deck.draw())
        self.community_cards.append(self.deck.draw())
        self.community_cards.append(self.deck.draw())

    def deal_turn(self):
        assert len(self.community_cards) == 3
        assert len(self.deck.burned) == 1

        print("dealer: dealing turn")
        self.deck.burn()
        self.community_cards.append(self.deck.draw())

    def deal_river(self):
        assert len(self.community_cards) == 4
        assert len(self.deck.burned) == 2

        print("dealer: dealing river")
        self.deck.burn()
        self.community_cards.append(self.deck.draw())

    def retrieve_player_cards(self, players: List[Player]):
        print("dealer: retrieving player cards")
        for p in players:
            self.deck.return_cards(p.retrieve_cards())
        self.deck.return_cards(self.community_cards)
        self.deck.return_burned()

        assert len(self.community_cards) == 0
        assert len(self.deck.burned) == 0
        assert len(self.deck.cards) == 52
