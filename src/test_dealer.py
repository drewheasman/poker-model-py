import unittest
from dealer import Dealer
from cards import Deck
from player import Player


class TestDealer(unittest.TestCase):
    def test_dealer_init(self):
        dealer = Dealer()
        self.assertEqual(0, len(dealer.community_cards))
        self.assertEqual(52, len(dealer.deck.cards))
        new_deck = Deck()
        self.assertNotEqual(new_deck.cards, dealer.deck.cards)

    def test_dealer_deal_flop(self):
        dealer = Dealer()
        dealer.deal_flop()
        self.assertEqual(3, len(dealer.community_cards))
        self.assertEqual(48, len(dealer.deck.cards))
        self.assertEqual(1, len(dealer.deck.burned))

    def test_dealer_deal_flop_late(self):
        dealer = Dealer()
        dealer.deck.burned.append(dealer.deck.cards.pop())
        with self.assertRaises(AssertionError):
            dealer.deal_flop()
        dealer.community_cards.append(dealer.deck.cards.pop())
        with self.assertRaises(AssertionError):
            dealer.deal_flop()

    def test_dealer_deal_turn(self):
        dealer = Dealer()
        dealer.deal_flop()
        dealer.deal_turn()
        self.assertEqual(4, len(dealer.community_cards))
        self.assertEqual(46, len(dealer.deck.cards))
        self.assertEqual(2, len(dealer.deck.burned))

    def test_dealer_deal_turn_early(self):
        dealer = Dealer()
        with self.assertRaises(AssertionError):
            dealer.deal_turn()

    def test_dealer_deal_river(self):
        dealer = Dealer()
        dealer.deal_flop()
        dealer.deal_turn()
        dealer.deal_river()
        self.assertEqual(5, len(dealer.community_cards))
        self.assertEqual(44, len(dealer.deck.cards))
        self.assertEqual(3, len(dealer.deck.burned))

    def test_dealer_deal_river_early(self):
        dealer = Dealer()
        dealer.deal_flop()
        with self.assertRaises(AssertionError):
            dealer.deal_river()

    def test_retrieve_player_cards(self):
        dealer = Dealer()
        players = [
            Player("Player1"),
            Player("Player2"),
        ]
        dealer.deal_to_players(players)
        dealer.retrieve_player_cards(players)
        self.assertEqual(52, len(dealer.deck.cards))


if __name__ == "__main__":
    unittest.main()
