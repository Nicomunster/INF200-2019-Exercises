import random

def single_game(num_players):
    """
    Returns duration of single game.

    Arguments
    ---------
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : int
        Number of moves the winning player needed to reach the goal
    """
    players = create_players(num_players)
    while not game_ends():



def multiple_games(num_games, num_players):
    """
    Returns durations of a number of games.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : list
        List with the numbedr of moves needed in each game.
    """


def multi_game_experiment(num_games, num_players, seed):
    """
    Returns durations of a number of games when playing with given seed.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game
    seed : int
        Seed used to initialise the random number generator

    Returns
    -------
    num_moves : list
        List with the numbedr of moves needed in each game.
    """


def create_players(n):
    """Creates a list of zeroes representing the starting position of players."""
    return [0] * n


def dice_roll():
    """Returns the result of a dice roll."""
    return random.randint(1, 6)


def one_move(starting_position):
    """Plays one move in the game. Returns the position after
     the turn has finished."""
    roll = dice_roll()
    middle_position = starting_position + roll
    end_position = check_if_snake_or_ladder(middle_position)
    if end_position >= 90:
        game ends
    return end_position


def check_if_snake_or_ladder(position):
    """Checks if the player is on a ladder or snake position,
    and returns the new position of that player"""
    snakes_or_ladder = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85,
                        24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}
    if position in snakes_or_ladder.keys():
        return snakes_or_ladder[position]
    else:
        return position

def game_ends():

