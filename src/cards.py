from enum import Enum
import random


class Suit(Enum):
    CLUB = "Club"
    DIAMOND = "Diamond"
    HEART = "Heart"
    SPADE = "Spade"


class Rank(Enum):
    ACE = "Ace"
    KING = "King"
    QUEEN = "Queen"
    JACK = "Jack"
    TEN = "Ten"
    NINE = "Nine"
    EIGHT = "Eight"
    SEVEN = "Seven"
    SIX = "Six"
    FIVE = "Five"
    FOUR = "Four"
    THREE = "Three"
    TWO = "Two"


class Card():
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    def __eq__(self, o):
        return self.suit == o.suit and self.rank == o.rank

    def __repr__(self):
        print(f"{self.rank.value} of {self.suit.value}s")


class Deck():
    def __init__(self):
        self.cards = []
        self.burned = []
        for s in Suit:
            for r in Rank:
                self.cards.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def burn(self):
        self.burned.append(self.cards.pop())
