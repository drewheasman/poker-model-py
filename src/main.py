from player import Player
from dealer import Dealer
from hands import best_hand


def main():
    while (True):
        print("\n===================== START ROUND =====================\n")

        players = [
            Player("Bob"),
            Player("James"),
            Player("Steve"),
            Player("Dave"),
            Player("Mick"),
        ]

        dealer = Dealer()
        dealer.deal_to_players(players)

        dealer.deal_flop()
        print(f"Community cards: {dealer.community_cards}\n")

        dealer.deal_turn()
        print(f"Community cards: {dealer.community_cards}\n")

        dealer.deal_river()
        print(f"Community cards: {dealer.community_cards}\n")

        print("Players show cards...\n")
        player_outcomes = []
        for p in players:
            hand = best_hand(dealer.community_cards + p.cards)
            player_outcomes.append((p, hand))
            print(
                f"{p.name} has {p.cards}. {hand[1]} plays for {hand[0].value}")
        print()

        print("Ranking:")
        player_outcomes.sort(key=lambda o: o[1][0].value)
        for op in player_outcomes:
            print(
                f"{op[0].name} has {op[0].cards}." +
                f" {op[1][1]} plays for {op[1][0].name}"
            )

        print(
            f"\n{player_outcomes[0][0].name} wins" +
            f" with a {player_outcomes[0][1][0].name}!\n"
        )

        dealer.retrieve_player_cards(players)

        print("\n====================== END ROUND ======================\n")

        input("Press Enter for another round or <ctrl-c> to end")


main()
