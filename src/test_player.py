import unittest
from player import Player
from cards import Deck


class TestPlayer(unittest.TestCase):
    def test_player_init(self):
        player = Player("Jimbob")
        self.assertEqual([], player.cards)

    def test_player_take_cards(self):
        player = Player("Jimbob")
        deck = Deck()

        player.take_card(deck.draw())
        self.assertEqual(1, len(player.cards))

        player.take_card(deck.draw())
        self.assertEqual(2, len(player.cards))

        with self.assertRaises(AssertionError):
            player.take_card(deck.draw())

    def test_player_return_cards(self):
        player = Player("Jimbob")
        deck = Deck()

        self.assertEqual(0, len(player.return_cards()))

        player.take_card(deck.draw())
        self.assertEqual(1, len(player.return_cards()))
        self.assertEqual(0, len(player.cards))

        player.take_card(deck.draw())
        player.take_card(deck.draw())
        self.assertEqual(2, len(player.return_cards()))
        self.assertEqual(0, len(player.cards))


if __name__ == "__main__":
    unittest.main()
