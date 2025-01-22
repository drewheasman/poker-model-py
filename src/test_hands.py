import unittest

import hands
from hands import HandType
from cards import Card, Suit, Rank


class TestHands(unittest.TestCase):

    def test_best_hand(self):
        cards = []
        self.assertEqual(
            (None, []),
            hands.best_hand(cards)
        )

        cards.append(Card(Suit.HEART, Rank.TWO))
        self.assertEqual(
            (
                HandType.HIGH_CARD,
                [
                    Card(Suit.HEART, Rank.TWO),
                ]
            ),
            hands.best_hand(cards))

        cards.append(Card(Suit.HEART, Rank.FOUR))
        self.assertEqual(
            (
                HandType.HIGH_CARD,
                [
                    Card(Suit.HEART, Rank.FOUR),
                    Card(Suit.HEART, Rank.TWO),
                ]
            ),
            hands.best_hand(cards))

        cards.append(Card(Suit.CLUB, Rank.THREE))
        self.assertEqual(
            (
                HandType.HIGH_CARD,
                [
                    Card(Suit.HEART, Rank.FOUR),
                    Card(Suit.CLUB, Rank.THREE),
                    Card(Suit.HEART, Rank.TWO)
                ]
            ),
            hands.best_hand(cards))

        cards.append(Card(Suit.DIAMOND, Rank.THREE))
        self.assertEqual(
            (
                HandType.PAIR,
                [
                    Card(Suit.DIAMOND, Rank.THREE),
                    Card(Suit.CLUB, Rank.THREE),
                    Card(Suit.HEART, Rank.FOUR),
                    Card(Suit.HEART, Rank.TWO)
                ]
            ),
            hands.best_hand(cards))

        cards.append(Card(Suit.DIAMOND, Rank.FOUR))
        self.assertEqual(
            (
                HandType.TWO_PAIR,
                [
                    Card(Suit.DIAMOND, Rank.FOUR),
                    Card(Suit.HEART, Rank.FOUR),
                    Card(Suit.DIAMOND, Rank.THREE),
                    Card(Suit.CLUB, Rank.THREE),
                    Card(Suit.HEART, Rank.TWO)
                ]
            ),
            hands.best_hand(cards))

        cards.append(Card(Suit.SPADE, Rank.FIVE))
        cards.append(Card(Suit.SPADE, Rank.ACE))
        self.assertEqual(
            (
                HandType.STRAIGHT,
                [
                    Card(Suit.SPADE, Rank.FIVE),
                    Card(Suit.DIAMOND, Rank.FOUR),
                    Card(Suit.DIAMOND, Rank.THREE),
                    Card(Suit.HEART, Rank.TWO),
                    Card(Suit.SPADE, Rank.ACE_LOW),
                ]
            ),
            hands.best_hand(cards))

        cards.remove(Card(Suit.DIAMOND, Rank.FOUR))
        cards.remove(Card(Suit.HEART, Rank.FOUR))
        cards.append(Card(Suit.SPADE, Rank.THREE))
        self.assertEqual(
            (
                HandType.THREE_OF_A_KIND,
                [
                    Card(Suit.SPADE, Rank.THREE),
                    Card(Suit.DIAMOND, Rank.THREE),
                    Card(Suit.CLUB, Rank.THREE),
                    Card(Suit.SPADE, Rank.ACE),
                    Card(Suit.SPADE, Rank.FIVE),
                ]
            ),
            hands.best_hand(cards))

        cards.append(Card(Suit.DIAMOND, Rank.FOUR))
        cards.append(Card(Suit.HEART, Rank.FOUR))
        self.assertEqual(
            (
                HandType.FULL_HOUSE,
                [
                    Card(Suit.SPADE, Rank.THREE),
                    Card(Suit.DIAMOND, Rank.THREE),
                    Card(Suit.CLUB, Rank.THREE),
                    Card(Suit.HEART, Rank.FOUR),
                    Card(Suit.DIAMOND, Rank.FOUR),
                ]
            ),
            hands.best_hand(cards))

        cards.append(Card(Suit.HEART, Rank.ACE))
        cards.append(Card(Suit.CLUB, Rank.ACE))
        cards.append(Card(Suit.DIAMOND, Rank.ACE))
        self.assertEqual(
            (
                HandType.FOUR_OF_A_KIND,
                [
                    Card(Suit.DIAMOND, Rank.ACE),
                    Card(Suit.CLUB, Rank.ACE),
                    Card(Suit.HEART, Rank.ACE),
                    Card(Suit.SPADE, Rank.ACE),
                    Card(Suit.SPADE, Rank.FIVE),
                ]
            ),
            hands.best_hand(cards))

        cards.append(Card(Suit.HEART, Rank.FIVE))
        cards.append(Card(Suit.HEART, Rank.THREE))
        self.assertEqual(
            (
                HandType.STRAIGHT_FLUSH,
                [
                    Card(Suit.HEART, Rank.FIVE),
                    Card(Suit.HEART, Rank.FOUR),
                    Card(Suit.HEART, Rank.THREE),
                    Card(Suit.HEART, Rank.TWO),
                    Card(Suit.HEART, Rank.ACE_LOW),
                ]
            ),
            hands.best_hand(cards))

        cards.append(Card(Suit.HEART, Rank.KING))
        cards.append(Card(Suit.HEART, Rank.QUEEN))
        cards.append(Card(Suit.HEART, Rank.JACK))
        cards.append(Card(Suit.HEART, Rank.TEN))

    def test_check_royal_flush(self):
        cards = []
        cards.append(Card(Suit.HEART, Rank.TWO))
        cards.append(Card(Suit.HEART, Rank.FOUR))
        cards.append(Card(Suit.HEART, Rank.FIVE))
        cards.append(Card(Suit.HEART, Rank.QUEEN))
        cards.append(Card(Suit.DIAMOND, Rank.TWO))
        cards.append(Card(Suit.HEART, Rank.ACE))
        cards.append(Card(Suit.HEART, Rank.KING))
        cards.append(Card(Suit.HEART, Rank.THREE))
        cards.append(Card(Suit.HEART, Rank.SIX))

        royal_flush_cards = hands.check_royal_flush(cards)
        self.assertEqual([], royal_flush_cards)

        cards.append(Card(Suit.HEART, Rank.TEN))
        royal_flush_cards = hands.check_royal_flush(cards)
        self.assertEqual([], royal_flush_cards)

        cards.append(Card(Suit.HEART, Rank.JACK))
        royal_flush_cards = hands.check_royal_flush(cards)
        self.assertEqual(
            [
                Card(Suit.HEART, Rank.ACE),
                Card(Suit.HEART, Rank.KING),
                Card(Suit.HEART, Rank.QUEEN),
                Card(Suit.HEART, Rank.JACK),
                Card(Suit.HEART, Rank.TEN),

            ],
            royal_flush_cards)

    def test_check_straight_flush(self):
        cards = []
        cards.append(Card(Suit.HEART, Rank.TWO))
        cards.append(Card(Suit.HEART, Rank.FOUR))
        cards.append(Card(Suit.HEART, Rank.FIVE))
        cards.append(Card(Suit.HEART, Rank.QUEEN))
        cards.append(Card(Suit.DIAMOND, Rank.TWO))
        cards.append(Card(Suit.HEART, Rank.ACE))
        cards.append(Card(Suit.HEART, Rank.KING))
        cards.append(Card(Suit.HEART, Rank.THREE))
        straight_cards = hands.check_straight_flush(cards)

        self.assertEqual([
            Card(Suit.HEART, Rank.FIVE),
            Card(Suit.HEART, Rank.FOUR),
            Card(Suit.HEART, Rank.THREE),
            Card(Suit.HEART, Rank.TWO),
            Card(Suit.HEART, Rank.ACE_LOW),

        ], straight_cards)

        cards.append(Card(Suit.HEART, Rank.SIX))
        straight_cards = hands.check_straight_flush(cards)
        self.assertEqual(
            [
                Card(Suit.HEART, Rank.SIX),
                Card(Suit.HEART, Rank.FIVE),
                Card(Suit.HEART, Rank.FOUR),
                Card(Suit.HEART, Rank.THREE),
                Card(Suit.HEART, Rank.TWO),

            ],
            straight_cards)

        cards.append(Card(Suit.HEART, Rank.TEN))
        cards.append(Card(Suit.HEART, Rank.JACK))
        straight_cards = hands.check_straight_flush(cards)
        self.assertEqual(
            [
                Card(Suit.HEART, Rank.ACE),
                Card(Suit.HEART, Rank.KING),
                Card(Suit.HEART, Rank.QUEEN),
                Card(Suit.HEART, Rank.JACK),
                Card(Suit.HEART, Rank.TEN),

            ],
            straight_cards)

    def test_check_four_of_a_kind(self):
        cards = []
        four_cards = hands.check_four_of_a_kind(cards)
        self.assertEqual([], four_cards)

        cards.append(Card(Suit.HEART, Rank.TWO))
        cards.append(Card(Suit.CLUB, Rank.TEN))
        cards.append(Card(Suit.HEART, Rank.FIVE))
        cards.append(Card(Suit.SPADE, Rank.TWO))
        cards.append(Card(Suit.CLUB, Rank.TWO))
        four_cards = hands.check_four_of_a_kind(cards)
        self.assertEqual([], four_cards)

        cards.append(Card(Suit.DIAMOND, Rank.TWO))
        four_cards = hands.check_four_of_a_kind(cards)
        self.assertEqual(
            [
                Card(Suit.DIAMOND, Rank.TWO),
                Card(Suit.CLUB, Rank.TWO),
                Card(Suit.SPADE, Rank.TWO),
                Card(Suit.HEART, Rank.TWO),
            ],
            four_cards)

        cards.append(Card(Suit.DIAMOND, Rank.TEN))
        cards.append(Card(Suit.SPADE, Rank.TEN))
        four_cards = hands.check_four_of_a_kind(cards)
        self.assertEqual(
            [
                Card(Suit.DIAMOND, Rank.TWO),
                Card(Suit.CLUB, Rank.TWO),
                Card(Suit.SPADE, Rank.TWO),
                Card(Suit.HEART, Rank.TWO),
            ],
            four_cards)

        cards.append(Card(Suit.HEART, Rank.TEN))
        four_cards = hands.check_four_of_a_kind(cards)
        self.assertEqual(
            set([
                Card(Suit.DIAMOND, Rank.TEN),
                Card(Suit.CLUB, Rank.TEN),
                Card(Suit.SPADE, Rank.TEN),
                Card(Suit.HEART, Rank.TEN),
            ]),
            set(four_cards))

    def test_check_full_house(self):
        cards = []
        full_cards = hands.check_full_house(cards)
        self.assertEqual([], full_cards)

        cards.append(Card(Suit.HEART, Rank.TWO))
        cards.append(Card(Suit.CLUB, Rank.TEN))
        cards.append(Card(Suit.HEART, Rank.FIVE))
        cards.append(Card(Suit.SPADE, Rank.TEN))
        cards.append(Card(Suit.DIAMOND, Rank.TWO))
        cards.append(Card(Suit.HEART, Rank.ACE))
        cards.append(Card(Suit.HEART, Rank.KING))
        full_cards = hands.check_full_house(cards)
        self.assertEqual([], full_cards)

        cards.append(Card(Suit.SPADE, Rank.TWO))
        full_cards = hands.check_full_house(cards)
        self.assertEqual(
            set([
                Card(Suit.SPADE, Rank.TEN),
                Card(Suit.CLUB, Rank.TEN),
                Card(Suit.SPADE, Rank.TWO),
                Card(Suit.DIAMOND, Rank.TWO),
                Card(Suit.HEART, Rank.TWO),
            ]),
            set(full_cards))

        cards.append(Card(Suit.DIAMOND, Rank.TEN))
        full_cards = hands.check_full_house(cards)
        self.assertEqual(
            set([
                Card(Suit.SPADE, Rank.TEN),
                Card(Suit.CLUB, Rank.TEN),
                Card(Suit.DIAMOND, Rank.TEN),
                Card(Suit.DIAMOND, Rank.TWO),
                Card(Suit.SPADE, Rank.TWO),
            ]),
            set(full_cards))

    def test_check_flush(self):
        cards = []
        flush_cards = hands.check_flush(cards)
        self.assertEqual([], flush_cards)

        cards.append(Card(Suit.HEART, Rank.TWO))
        cards.append(Card(Suit.CLUB, Rank.TEN))
        cards.append(Card(Suit.HEART, Rank.FIVE))
        cards.append(Card(Suit.SPADE, Rank.QUEEN))
        cards.append(Card(Suit.DIAMOND, Rank.TWO))
        cards.append(Card(Suit.HEART, Rank.ACE))
        cards.append(Card(Suit.HEART, Rank.KING))
        flush_cards = hands.check_flush(cards)
        self.assertEqual([], flush_cards)

        cards.append(Card(Suit.HEART, Rank.THREE))
        flush_cards = hands.check_flush(cards)
        self.assertEqual(
            [
                Card(Suit.HEART, Rank.ACE),
                Card(Suit.HEART, Rank.KING),
                Card(Suit.HEART, Rank.FIVE),
                Card(Suit.HEART, Rank.THREE),
                Card(Suit.HEART, Rank.TWO),
            ],
            flush_cards)

        cards.append(Card(Suit.HEART, Rank.TEN))
        flush_cards = hands.check_flush(cards)
        self.assertEqual(
            [
                Card(Suit.HEART, Rank.ACE),
                Card(Suit.HEART, Rank.KING),
                Card(Suit.HEART, Rank.TEN),
                Card(Suit.HEART, Rank.FIVE),
                Card(Suit.HEART, Rank.THREE),
            ],
            flush_cards)

        cards.append(Card(Suit.CLUB, Rank.EIGHT))
        flush_cards = hands.check_flush(cards)
        self.assertEqual(
            [
                Card(Suit.HEART, Rank.ACE),
                Card(Suit.HEART, Rank.KING),
                Card(Suit.HEART, Rank.TEN),
                Card(Suit.HEART, Rank.FIVE),
                Card(Suit.HEART, Rank.THREE),
            ],
            flush_cards)

    def test_check_straight(self):
        cards = []
        straight_cards = hands.check_straight(cards)
        self.assertEqual([], straight_cards)

        cards.append(Card(Suit.HEART, Rank.TWO))
        cards.append(Card(Suit.CLUB, Rank.FOUR))
        cards.append(Card(Suit.HEART, Rank.FIVE))
        cards.append(Card(Suit.SPADE, Rank.QUEEN))
        cards.append(Card(Suit.DIAMOND, Rank.TWO))
        cards.append(Card(Suit.HEART, Rank.ACE))
        cards.append(Card(Suit.HEART, Rank.KING))
        straight_cards = hands.check_straight(cards)
        self.assertEqual([], straight_cards)

        cards.append(Card(Suit.HEART, Rank.THREE))
        straight_cards = hands.check_straight(cards)
        self.assertEqual(
            [
                Card(Suit.HEART, Rank.FIVE),
                Card(Suit.CLUB, Rank.FOUR),
                Card(Suit.HEART, Rank.THREE),
                Card(Suit.DIAMOND, Rank.TWO),
                Card(Suit.HEART, Rank.ACE_LOW),

            ],
            straight_cards)

        cards.append(Card(Suit.HEART, Rank.TEN))
        straight_cards = hands.check_straight(cards)
        self.assertEqual(
            [
                Card(Suit.HEART, Rank.FIVE),
                Card(Suit.CLUB, Rank.FOUR),
                Card(Suit.HEART, Rank.THREE),
                Card(Suit.DIAMOND, Rank.TWO),
                Card(Suit.HEART, Rank.ACE_LOW),

            ],
            straight_cards)

        cards.append(Card(Suit.CLUB, Rank.SIX))
        straight_cards = hands.check_straight(cards)
        self.assertEqual(
            [
                Card(Suit.CLUB, Rank.SIX),
                Card(Suit.HEART, Rank.FIVE),
                Card(Suit.CLUB, Rank.FOUR),
                Card(Suit.HEART, Rank.THREE),
                Card(Suit.HEART, Rank.TWO),

            ],
            straight_cards)

        cards.append(Card(Suit.SPADE, Rank.TEN))
        straight_cards = hands.check_straight(cards)
        self.assertEqual(
            [
                Card(Suit.CLUB, Rank.SIX),
                Card(Suit.HEART, Rank.FIVE),
                Card(Suit.CLUB, Rank.FOUR),
                Card(Suit.HEART, Rank.THREE),
                Card(Suit.HEART, Rank.TWO),

            ],
            straight_cards)

        cards.append(Card(Suit.SPADE, Rank.JACK))
        straight_cards = hands.check_straight(cards)
        self.assertEqual(
            [
                Card(Suit.HEART, Rank.ACE),
                Card(Suit.HEART, Rank.KING),
                Card(Suit.SPADE, Rank.QUEEN),
                Card(Suit.SPADE, Rank.JACK),
                Card(Suit.HEART, Rank.TEN),

            ],
            straight_cards)

    def test_check_three_of_a_kind(self):
        cards = []
        three_cards = hands.check_three_of_a_kind(cards)
        self.assertEqual([], three_cards)

        cards.append(Card(Suit.HEART, Rank.TWO))
        cards.append(Card(Suit.CLUB, Rank.TEN))
        cards.append(Card(Suit.HEART, Rank.FIVE))
        cards.append(Card(Suit.SPADE, Rank.TWO))
        three_cards = hands.check_three_of_a_kind(cards)
        self.assertEqual([], three_cards)

        cards.append(Card(Suit.DIAMOND, Rank.TWO))
        three_cards = hands.check_three_of_a_kind(cards)
        self.assertEqual(
            [
                Card(Suit.DIAMOND, Rank.TWO),
                Card(Suit.SPADE, Rank.TWO),
                Card(Suit.HEART, Rank.TWO),
            ],
            three_cards)

        cards.append(Card(Suit.DIAMOND, Rank.TEN))
        three_cards = hands.check_three_of_a_kind(cards)
        self.assertEqual(
            [
                Card(Suit.DIAMOND, Rank.TWO),
                Card(Suit.SPADE, Rank.TWO),
                Card(Suit.HEART, Rank.TWO),
            ],
            three_cards)

        cards.append(Card(Suit.HEART, Rank.TEN))
        three_cards = hands.check_three_of_a_kind(cards)
        self.assertEqual(
            set([
                Card(Suit.DIAMOND, Rank.TEN),
                Card(Suit.CLUB, Rank.TEN),
                Card(Suit.HEART, Rank.TEN),
            ]),
            set(three_cards))

    def test_check_two_pair(self):
        cards = []
        two_pair = hands.check_two_pair(cards)
        self.assertEqual([], two_pair)

        cards.append(Card(Suit.HEART, Rank.TWO))
        cards.append(Card(Suit.CLUB, Rank.TEN))
        cards.append(Card(Suit.HEART, Rank.FIVE))
        two_pair = hands.check_two_pair(cards)
        self.assertEqual([], two_pair)

        cards.append(Card(Suit.DIAMOND, Rank.TWO))
        cards.append(Card(Suit.DIAMOND, Rank.TEN))
        two_pair = hands.check_two_pair(cards)
        self.assertEqual(
            set([
                Card(Suit.CLUB, Rank.TEN),
                Card(Suit.DIAMOND, Rank.TEN),
                Card(Suit.HEART, Rank.TWO),
                Card(Suit.DIAMOND, Rank.TWO),
            ]),
            set(two_pair))

        cards.append(Card(Suit.DIAMOND, Rank.FIVE))
        two_pair = hands.check_two_pair(cards)
        self.assertEqual(
            set([
                Card(Suit.CLUB, Rank.TEN),
                Card(Suit.DIAMOND, Rank.TEN),
                Card(Suit.HEART, Rank.FIVE),
                Card(Suit.DIAMOND, Rank.FIVE),
            ]),
            set(two_pair))

    def test_check_pair(self):
        cards = []
        two_cards = hands.check_pair(cards)
        self.assertEqual([], two_cards)

        cards.append(Card(Suit.HEART, Rank.TWO))
        cards.append(Card(Suit.CLUB, Rank.TEN))
        cards.append(Card(Suit.HEART, Rank.FIVE))
        two_cards = hands.check_pair(cards)
        self.assertEqual([], two_cards)

        cards.append(Card(Suit.DIAMOND, Rank.TWO))
        two_cards = hands.check_pair(cards)
        self.assertEqual(
            [
                Card(Suit.DIAMOND, Rank.TWO),
                Card(Suit.HEART, Rank.TWO),
            ],
            two_cards)

        cards.append(Card(Suit.DIAMOND, Rank.TEN))
        two_cards = hands.check_pair(cards)
        self.assertEqual(
            set([
                Card(Suit.CLUB, Rank.TEN),
                Card(Suit.DIAMOND, Rank.TEN),
            ]),
            set(two_cards))

    def test_highest_cards(self):
        cards = []
        highest_cards = hands.highest_cards(cards)
        self.assertEqual([], highest_cards)

        cards.append(Card(Suit.HEART, Rank.TWO))
        highest_cards = hands.highest_cards(cards)
        self.assertEqual(
            [
                Card(Suit.HEART, Rank.TWO),
            ],
            highest_cards)

        cards.append(Card(Suit.CLUB, Rank.TEN))
        highest_cards = hands.highest_cards(cards)
        self.assertEqual(
            [
                Card(Suit.CLUB, Rank.TEN),
                Card(Suit.HEART, Rank.TWO),
            ],
            highest_cards)

        cards.append(Card(Suit.HEART, Rank.FIVE))
        highest_cards = hands.highest_cards(cards)
        self.assertEqual(
            [
                Card(Suit.CLUB, Rank.TEN),
                Card(Suit.HEART, Rank.FIVE),
                Card(Suit.HEART, Rank.TWO),
            ],
            highest_cards)

        cards.append(Card(Suit.SPADE, Rank.QUEEN))
        highest_cards = hands.highest_cards(cards)
        self.assertEqual(
            [
                Card(Suit.SPADE, Rank.QUEEN),
                Card(Suit.CLUB, Rank.TEN),
                Card(Suit.HEART, Rank.FIVE),
                Card(Suit.HEART, Rank.TWO),
            ],
            highest_cards)

        cards.append(Card(Suit.DIAMOND, Rank.TWO))
        highest_cards = hands.highest_cards(cards)
        self.assertEqual(
            [
                Card(Suit.SPADE, Rank.QUEEN),
                Card(Suit.CLUB, Rank.TEN),
                Card(Suit.HEART, Rank.FIVE),
                Card(Suit.HEART, Rank.TWO),
                Card(Suit.DIAMOND, Rank.TWO),
            ],
            highest_cards)

        cards.append(Card(Suit.HEART, Rank.ACE))
        highest_cards = hands.highest_cards(cards)
        self.assertEqual(
            [
                Card(Suit.HEART, Rank.ACE),
                Card(Suit.SPADE, Rank.QUEEN),
                Card(Suit.CLUB, Rank.TEN),
                Card(Suit.HEART, Rank.FIVE),
                Card(Suit.HEART, Rank.TWO),
            ],
            highest_cards)

        cards.append(Card(Suit.DIAMOND, Rank.KING))
        highest_cards = hands.highest_cards(cards)
        self.assertEqual(
            [
                Card(Suit.HEART, Rank.ACE),
                Card(Suit.DIAMOND, Rank.KING),
                Card(Suit.SPADE, Rank.QUEEN),
                Card(Suit.CLUB, Rank.TEN),
                Card(Suit.HEART, Rank.FIVE),
            ],
            highest_cards)


if __name__ == "__main__":
    unittest.main()
