from random import randint

__author__ = 'Nicolai Munsterhjelm'
__email__ = 'nicmunst@nmbu.no'


def make_guess():
    """
    This function makes the player guess a number.

    Returns
    -------
    int
        Number that the player guessed.
    """

    return int(input('Your guess: '))


def sum_of_two_dice():
    """
    This function returns the sum of two dice.

    Returns
    -------
    int
        The sum of two dice

    """

    return randint(1, 6) + randint(1, 6)


def play_game():
    """
    Plays one game of guessing the sum of two dice. The player gets three guesses.
    The player gets three points for guessing correctly on the first guess, two points
    on the second guess, and one point if he/she guesses correctly on the last guess.
    If the player is not able to guess correctly on any oof the three guesses, he/she
    loses the game.
    """

    answer = sum_of_two_dice()
    for guess_number in range(1, 4):
        guess = make_guess()
        if answer == guess:
            print('You won {} points.'.format(4 - guess_number))
            break
        elif guess_number == 3:
            print('You lost. Correct answer: {}.'.format(answer))
        else:
            print('Wrong, try again!')


if __name__ == '__main__':
    play_game()
