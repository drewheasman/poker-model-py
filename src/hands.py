from typing import List
from enum import Enum

from cards import Card, Suit, Rank


class HandTypes(Enum):
    ROYAL_FLUSH = "Royal flush"
    STRAIGHT_FLUSH = "straight flush"
    FOUR_OF_A_KIND = "four of a kind"
    FULL_HOUSE = "full house"
    FLUSH = "flush"
    STRAIGHT = "straight"
    THREE_OF_A_KIND = "three of a kind"
    TWO_PAIR = "two pair"
    PAIR = "pair"
    HIGH_CARD = "high card"


def best_hand(cards: List[Card]):
    matching_hand = check_royal_flush(cards)
    if len(matching_hand) > 0:
        return matching_hand

    matching_hand = check_straight_flush(cards)
    if len(matching_hand) > 0:
        return matching_hand

    matching_hand = check_four_of_a_kind(cards)
    if len(matching_hand) > 0:
        return matching_hand

    matching_hand = check_full_house(cards)
    if len(matching_hand) > 0:
        return matching_hand

    matching_hand = check_flush(cards)
    if len(matching_hand) > 0:
        return matching_hand

    matching_hand = check_straight(cards)
    if len(matching_hand) > 0:
        return matching_hand

    matching_hand = check_three_of_a_kind(cards)
    if len(matching_hand) > 0:
        return matching_hand

    matching_hand = check_two_pair(cards)
    if len(matching_hand) > 0:
        return matching_hand

    matching_hand = check_pair(cards)
    if len(matching_hand) > 0:
        return matching_hand

    matching_hand = highest_cards(cards)
    if len(matching_hand) > 0:
        return matching_hand


def check_royal_flush(cards: List[Card]):
    royal_cards = cards.copy()
    royal_cards = check_straight_flush(royal_cards)
    if len(royal_cards) == 5 and royal_cards[0].rank == Rank.ACE:
        return royal_cards

    return []

    tested_cards = check_royal_flush(cards)


def check_straight_flush(cards: List[Card]):
    straight_flush_cards = cards.copy()
    for s in Suit:
        suit_cards = [c for c in straight_flush_cards if c.suit == s]
        straight_cards = check_straight(suit_cards)
        if len(straight_cards) == 5:
            return straight_cards

    return []


def check_four_of_a_kind(cards: List[Card]):
    pass


def check_full_house(cards: List[Card]):
    pass


def check_flush(cards: List[Card]):
    flush_cards = cards.copy()
    for s in Suit:
        matched_cards = [c for c in flush_cards if c.suit == s]
        if len(matched_cards) >= 5:
            matched_cards.sort(key=lambda c: c.rank.value, reverse=True)
            return matched_cards[:5]
    return []


def check_straight(cards: List[Card]):
    straight_cards = cards.copy()
    straight_cards.sort(key=lambda c: c.rank.value, reverse=True)

    # Append matching low aces
    for c in straight_cards:
        if c.rank == Rank.ACE:
            straight_cards.append(Card(c.suit, Rank.ACE_LOW))

    run_cards = []
    for i in range(len(straight_cards)-1):
        if straight_cards[i].rank == straight_cards[i+1].rank:
            continue
        if straight_cards[i].rank.value == straight_cards[i+1].rank.value + 1:
            run_cards.append(straight_cards[i])
            if len(run_cards) == 4:
                run_cards.append(straight_cards[i+1])
                return run_cards
        else:
            run_cards = []

    return []


def check_three_of_a_kind(cards: List[Card]):
    pass


def check_two_pair(cards: List[Card]):
    pass


def check_pair(cards: List[Card]):
    pass


def highest_cards(cards: List[Card]):
    ranked_cards = cards.copy()
    ranked_cards.sort(key=lambda c: c.rank.value, reverse=True)
    if len(ranked_cards) > 5:
        return ranked_cards[:5]
    return ranked_cards
