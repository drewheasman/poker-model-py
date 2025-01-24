import unittest
from cards import Card, Deck


class TestDeck(unittest.TestCase):
    def test_deck_init(self):
        d = Deck()
        self.assertEqual(52, len(d.cards))

    def test_deck_shuffle(self):
        d = Deck()
        d2 = Deck()
        original_cards = d.cards.copy()
        self.assertEqual(d.cards, d2.cards)
        self.assertEqual(original_cards, d.cards)

        d.shuffle()
        self.assertNotEqual(original_cards, d.cards)

        d2.shuffle()
        self.assertNotEqual(d.cards, d2.cards)

    def test_deck_draw(self):
        d = Deck()
        drawn = d.draw()
        self.assertTrue(isinstance(drawn, Card))
        self.assertEqual(51, len(d.cards))
        self.assertFalse(drawn in d.cards)

    def test_deck_return_cards(self):
        d = Deck()
        drawn = [d.draw()]
        drawn.append(d.draw())
        drawn.append(d.draw())
        self.assertEqual(3, len(drawn))
        self.assertEqual(49,  len(d.cards))

        d.return_cards(drawn)
        self.assertEqual(52,  len(d.cards))


if __name__ == "__main__":
    unittest.main()
