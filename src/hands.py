from typing import List
from enum import Enum

from cards import Card, Suit, Rank


class HandType(Enum):
    ROYAL_FLUSH = 0
    STRAIGHT_FLUSH = 1
    FOUR_OF_A_KIND = 2
    FULL_HOUSE = 3
    FLUSH = 4
    STRAIGHT = 5
    THREE_OF_A_KIND = 6
    TWO_PAIR = 7
    PAIR = 8
    HIGH_CARD = 9


def best_hand(cards: List[Card]) -> (HandType, List[Card]):
    matching_hand = check_royal_flush(cards)
    if len(matching_hand) > 0:
        return (
            HandType.ROYAL_FLUSH,
            matching_hand
        )

    matching_hand = check_straight_flush(cards)
    if len(matching_hand) > 0:
        return (
            HandType.STRAIGHT_FLUSH, matching_hand
        )

    matching_hand = check_four_of_a_kind(cards)
    if len(matching_hand) > 0:
        remaining = [c for c in cards if c not in matching_hand]
        return (
            HandType.FOUR_OF_A_KIND,
            matching_hand + highest_cards(remaining, 1)
        )

    matching_hand = check_full_house(cards)
    if len(matching_hand) > 0:
        return (
            HandType.FULL_HOUSE,
            matching_hand
        )

    matching_hand = check_flush(cards)
    if len(matching_hand) > 0:
        return (
            HandType.FLUSH,
            matching_hand
        )

    matching_hand = check_straight(cards)
    if len(matching_hand) > 0:
        return (
            HandType.STRAIGHT,
            matching_hand
        )

    matching_hand = check_three_of_a_kind(cards)
    if len(matching_hand) > 0:
        remaining = [c for c in cards if c not in matching_hand]
        return (
            HandType.THREE_OF_A_KIND,
            matching_hand + highest_cards(remaining, 2)
        )

    matching_hand = check_two_pair(cards)
    if len(matching_hand) > 0:
        remaining = [c for c in cards if c not in matching_hand]
        return (
            HandType.TWO_PAIR,
            matching_hand + highest_cards(remaining, 1)
        )

    matching_hand = check_pair(cards)
    if len(matching_hand) > 0:
        remaining = [c for c in cards if c not in matching_hand]
        return (
            HandType.PAIR,
            matching_hand + highest_cards(remaining, 3)
        )

    matching_hand = highest_cards(cards)
    if len(matching_hand) > 0:
        return (HandType.HIGH_CARD, matching_hand)

    return (None, [])


def check_royal_flush(cards: List[Card]):
    royal_cards = cards.copy()
    royal_cards = check_straight_flush(royal_cards)
    if len(royal_cards) == 5 and royal_cards[0].rank == Rank.ACE:
        return royal_cards

    return []


def check_straight_flush(cards: List[Card]):
    straight_flush_cards = cards.copy()
    for s in Suit:
        suit_cards = [c for c in straight_flush_cards if c.suit == s]
        straight_cards = check_straight(suit_cards)
        if len(straight_cards) == 5:
            return straight_cards

    return []


def check_four_of_a_kind(cards: List[Card]):
    return check_of_a_kind(4, cards)


def check_full_house(cards: List[Card]):
    cards_to_check = cards.copy()

    three_of_a_kind = check_of_a_kind(3, cards_to_check)
    if len(three_of_a_kind) != 3:
        return []

    cards_to_check = [c for c in cards_to_check if c not in three_of_a_kind]

    pair = check_of_a_kind(2, cards_to_check)
    if len(pair) != 2:
        return []

    full_house = three_of_a_kind + pair
    return full_house


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
    return check_of_a_kind(3, cards)


def check_two_pair(cards: List[Card]):
    cards_to_check = cards.copy()

    first_pair = check_of_a_kind(2, cards_to_check)
    if len(first_pair) != 2:
        return []

    cards_to_check = [c for c in cards_to_check if c not in first_pair]

    second_pair = check_of_a_kind(2, cards_to_check)
    if len(second_pair) != 2:
        return []

    pairs = first_pair + second_pair
    return pairs


def check_pair(cards: List[Card]):
    return check_of_a_kind(2, cards)


def highest_cards(cards: List[Card], num=5):
    ranked_cards = cards.copy()
    ranked_cards.sort(key=lambda c: c.rank.value, reverse=True)
    if len(ranked_cards) > num:
        return ranked_cards[:num]
    return ranked_cards


def check_of_a_kind(of: int, cards: List[Card]):
    cards_to_check = cards.copy()
    cards_to_check.sort(key=lambda c: c.rank.value)
    counts = {}
    while len(cards_to_check) > 0:
        c: Card = cards_to_check.pop()
        if c.rank not in counts:
            counts[c.rank] = []
        counts[c.rank].append(c)
        if len(counts[c.rank]) == of:
            return counts[c.rank]

    return []
