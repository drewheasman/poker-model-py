from enum import Enum
import random


class Suit(Enum):
    CLUB = 0
    DIAMOND = 1
    HEART = 2
    SPADE = 3


class Rank(Enum):
    ACE = 14
    KING = 13
    QUEEN = 12
    JACK = 11
    TEN = 10
    NINE = 9
    EIGHT = 8
    SEVEN = 7
    SIX = 6
    FIVE = 5
    FOUR = 4
    THREE = 3
    TWO = 2
    ACE_LOW = 1


class Card():
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    def __eq__(self, o):
        return self.suit == o.suit and self.rank == o.rank

    def __repr__(self):
        return f"{self.rank.value} of {self.suit.name}s"


class Deck():
    def __init__(self):
        self.cards = []
        self.burned = []
        for s in Suit:
            for r in Rank:
                if r == Rank.ACE_LOW:
                    continue
                self.cards.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def burn(self):
        self.burned.append(self.cards.pop())
