import random
from statistics import median, mean, stdev

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
    num_moves = 0
    players = create_players(num_players)
    while not game_ends(players):
        for player_num, position in enumerate(players):
            players[player_num] = one_move(position)
        num_moves += 1

    return num_moves


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
    num_moves = []
    for i in range(num_games):
        num_moves.append(single_game(num_players))
    return num_moves


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

    random.seed(seed)
    num_moves = multiple_games(num_games, num_players)
    return num_moves


def create_players(n):
    """
    Creates a list of zeroes representing the starting position of players.
    """
    return [0] * n


def dice_roll():
    """
    Returns the result of a dice roll.
    """
    return random.randint(1, 6)


def one_move(starting_position):
    """
    Plays one move in the game. Returns the position after
     the turn has finished.
     """
    roll = dice_roll()
    middle_position = starting_position + roll
    end_position = check_if_snake_or_ladder(middle_position)

    return end_position


def check_if_snake_or_ladder(position):
    """
    Checks if the player is on a ladder or snake position,
    :returns the new position of that player
    """
    snakes_or_ladder = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85,
                        24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}
    if position in snakes_or_ladder.keys():
        return snakes_or_ladder[position]
    else:
        return position


def game_ends(players):
    """
    Terminates the game when a player wins
    :returns True if any player is past the finishing line
    """

    for player_num, position in enumerate(players):
        if position >= 90:
            return True

if __name__ == '__main__':
    num_moves = multi_game_experiment(100, 4, 20)
    minimum = min(num_moves)
    maximum = max(num_moves)
    medianen = median(num_moves)
    gj_snitt = mean(num_moves)
    std = stdev(num_moves)

    print('Minimum :', minimum)
    print('Maximum :', maximum)
    print('Medianen :', medianen)
    print('gj_snitt :', gj_snitt)
    print('std :', std)
