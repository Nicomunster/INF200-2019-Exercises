
SUITS = ('C', 'S', 'H', 'D')
VALUES = range(1, 14)


def deck_loop():
    """
    This function creates a standard deck of 52 cards using for loops.

    Returns
    -------
    deck
        List representing a deck of cards.
    """
    deck = []
    for suit in SUITS:
        for val in VALUES:
            deck.append((suit, val))
    return deck


def deck_comp():
    """
    This function creates a standard deck of 52 cards using a list comprehension.

    Returns
    -------
    list
        List representing a deck of cards.

    """
    return [(suit, val) for suit in SUITS for val in VALUES]


if __name__ == '__main__':
    if deck_loop() != deck_comp():
        print('ERROR!')
