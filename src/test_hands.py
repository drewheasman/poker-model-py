import unittest

import hands
from cards import Card, Suit, Rank


class TestHands(unittest.TestCase):

    def test_best_hand(self):
        pass

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

        straight_cards = hands.check_royal_flush(cards)
        self.assertEqual([], straight_cards)

        cards.append(Card(Suit.HEART, Rank.TEN))
        straight_cards = hands.check_royal_flush(cards)
        self.assertEqual([], straight_cards)

        cards.append(Card(Suit.HEART, Rank.JACK))
        straight_cards = hands.check_royal_flush(cards)
        self.assertEqual(
            [
                Card(Suit.HEART, Rank.ACE),
                Card(Suit.HEART, Rank.KING),
                Card(Suit.HEART, Rank.QUEEN),
                Card(Suit.HEART, Rank.JACK),
                Card(Suit.HEART, Rank.TEN),

            ],
            straight_cards)

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
        pass

    def test_check_full_house(self):
        pass

    def test_check_flush(self):
        cards = []
        flush_cards = hands.check_flush(cards)
        self.assertEqual(0, len(flush_cards))

        cards.append(Card(Suit.HEART, Rank.TWO))
        flush_cards = hands.check_flush(cards)
        self.assertEqual([], flush_cards)

        cards.append(Card(Suit.CLUB, Rank.TEN))
        flush_cards = hands.check_flush(cards)
        self.assertEqual([], flush_cards)

        cards.append(Card(Suit.HEART, Rank.FIVE))
        flush_cards = hands.check_flush(cards)
        self.assertEqual([], flush_cards)

        cards.append(Card(Suit.SPADE, Rank.QUEEN))
        flush_cards = hands.check_flush(cards)
        self.assertEqual([], flush_cards)

        cards.append(Card(Suit.DIAMOND, Rank.TWO))
        flush_cards = hands.check_flush(cards)
        self.assertEqual([], flush_cards)

        cards.append(Card(Suit.HEART, Rank.ACE))
        flush_cards = hands.check_flush(cards)
        self.assertEqual([], flush_cards)

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
        self.assertEqual(0, len(straight_cards))

        cards.append(Card(Suit.HEART, Rank.TWO))
        straight_cards = hands.check_straight(cards)
        self.assertEqual([], straight_cards)

        cards.append(Card(Suit.CLUB, Rank.FOUR))
        straight_cards = hands.check_straight(cards)
        self.assertEqual([], straight_cards)

        cards.append(Card(Suit.HEART, Rank.FIVE))
        straight_cards = hands.check_straight(cards)
        self.assertEqual([], straight_cards)

        cards.append(Card(Suit.SPADE, Rank.QUEEN))
        straight_cards = hands.check_straight(cards)
        self.assertEqual([], straight_cards)

        cards.append(Card(Suit.DIAMOND, Rank.TWO))
        straight_cards = hands.check_straight(cards)
        self.assertEqual([], straight_cards)

        cards.append(Card(Suit.HEART, Rank.ACE))
        straight_cards = hands.check_straight(cards)
        self.assertEqual([], straight_cards)

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
        pass

    def test_check_two_pair(self):
        pass

    def test_check_pair(self):
        pass

    def test_highest_cards(self):
        cards = []
        highest_cards = hands.highest_cards(cards)
        self.assertEqual(0, len(highest_cards))

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
