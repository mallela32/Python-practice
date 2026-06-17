"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int: The value of a given card.  See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.
    """
    face_cards = ['J','Q','K']
    if card in face_cards:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)



def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.

    Returns:
        str or tuple: The resulting tuple contains both cards if they are of equal value.
    """

    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    if card_one_value == card_two_value:
        return (card_one,card_two)
    if card_one_value > card_two_value:
        return card_one
    else:
        return card_two
    


def value_of_ace(card_one, card_two):

    total = 0

    for card in [card_one, card_two]:

        if card in ["J", "Q", "K"]:

            total += 10

        elif card == "A":

            total += 11

        else:

            total += int(card)

    return 11 if total + 11 <= 21 else 1

def is_blackjack(card_one, card_two):

    return (

        (card_one == "A" and card_two in ["10", "J", "Q", "K"])

        or

        (card_two == "A" and card_one in ["10", "J", "Q", "K"])

    )

def can_split_pairs(card_one, card_two):

    return value_of_card(card_one) == value_of_card(card_two)

def can_double_down(card_one, card_two):

    total = value_of_card(card_one) + value_of_card(card_two)

    return total in [9, 10, 11]