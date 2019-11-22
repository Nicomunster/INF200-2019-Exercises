# -*- coding: utf-8 -*-

__author__ = 'Alf Georg Ovland', 'Nicolai Munsterhjelm'
__email__ = 'alov@nmbu.no', 'nicmunst@nmbu.no'

import random
from collections import Counter

class Board:
    def __init__(self, ladders=None, chutes=None, goal=90):
        """
        Board manages all information about ladders, chutes, and the goal.
        Parameters
        ----------
        ladders: list of tuples
        chutes: list of tuples
        goal: int
        """
        if ladders is None:
            ladders = [(1, 40), (8, 10), (36, 52), (43, 62), (49, 79),
                       (65, 82), (68, 85)]
        if chutes is None:
            chutes = [(24, 5), (33, 3), (42, 30), (56, 37), (64, 27),
                      (74, 12), (87, 70)]

        self.ladders = dict(ladders)
        self.chutes = dict(chutes)
        self.goal = goal

    def goal_reached(self, position):
        """Returns True if position is greater or equal to 90.
        """
        return position >= 90

    def position_adjustment(self, position):
        """
        Checks if the input position is at the start of a chute or a ladder.
        Parameters
        ----------
        position: int

        Returns
        -------
        int: Number of moves to adjust according to chutes and ladders list.
        If it isn't at the start of a chute og ladder it returns zero
        """
        if position in self.ladders.keys():
            return self.ladders[position] - position
        elif position in self.chutes.keys():
            return self.chutes[position] - position
        return 0


class Player:
    def __init__(self, board_instance):
        """
        Creates a player constrained to a board instance.
        Parameters
        ----------
        board_instance: class instance of Board
        """
        self.board_instance = board_instance
        self.position = 0
        self.turns = 0

    def move(self):
        """
        Handles a dice cast and checks if it lands on a chute or a ladder
        and updates position accordingly.
        """
        roll = random.randint(1, 6)
        self.position += roll
        self.position += \
            self.board_instance.position_adjustment(self.position)
        self.turns += 1





class ResilientPlayer(Player):
    def __init__(self, board_instance, extra_steps=None):
        """
        Subclass of Player. takes extra steps next move
         if it goes down a chute.
        Parameters
        ----------
        board_instance: Class instance of Board
        extra_steps: int (number of extra steps)
        """
        if extra_steps is None:
            extra_steps = 1
        self.extra_steps = extra_steps
        self.chute_last = False
        super().__init__(board_instance)

    def move(self):
        """
        Modified version of move from superclass Player.
        Handles the extra steps and updates position accordingly.
        """
        roll = random.randint(1, 6)
        self.position += roll
        if self.chute_last:
            self.position += self.extra_steps
            self.chute_last = False
        pre_adjust = self.position
        self.position += \
            self.board_instance.position_adjustment(self.position)
        if pre_adjust > self.position:
            self.chute_last = True
        self.turns += 1

class LazyPlayer(Player):
    def __init__(self, board_instance, dropped_steps=None):
        """
        Subclass of Player. Drop steps next move
         if it goes up a ladder. It will not go backwards,
         only subtract the dropped steps from the dice roll.
        Parameters
        ----------
        board_instance: Class instance of Board
        dropped_steps: int (number of dropped steps)
        """
        if dropped_steps is None:
            dropped_steps = 1
        self.dropped_steps = abs(dropped_steps)
        self.ladder_last = False
        super().__init__(board_instance)

    def move(self):
        """
        Modified version of move from superclass Player.
        Handles the dropped steps and updates position accordingly.
        Returns
        -------

        """
        roll = random.randint(1, 6)
        start_position = self.position

        if self.ladder_last:
            intermediate_position = start_position + roll - self.dropped_steps
            if intermediate_position < start_position:
                intermediate_position = start_position
        else:
            intermediate_position = start_position + roll

        self.position += \
            self.board_instance.position_adjustment(intermediate_position)

        if self.position > intermediate_position:
            self.ladder_last = True

        self.turns += 1


class Simulation:
    def __init__(
            self, player_field, board=None,
            seed=None, randomize_players=False
    ):
        """
        Handles the simulation part of the task.
        Parameters
        ----------
        player_field: List (types of players)
        board: Class instance of Board
        seed: int (sets the seed of random functions)
        randomize_players: bool (choose if players should be shuffled)
        """
        if board is None:
            board = Board()
        self.player_field = player_field
        self.board = board
        self.seed = seed
        if randomize_players:
            random.shuffle(self.player_field)
        self.winning_list = []

    def single_game(self):
        """
        Plays a single game
        Returns
        -------
        Tuple : (turns , winning player type)
        """

        players = [cl(self.board) for cl in self.player_field]

        while True:
            for player in players:
                player.move()
                if self.board.goal_reached(player.position):
                    return player.turns, player.__class__.__name__

    def run_simulation(self, num_games):
        """
        Runs simulation for given number of games
        stores result in the simulation-object as a
        list: [(turns , winning player type)]
        Parameters
        ----------
        num_games : Number of games to be simulated
        """

        for game in range(num_games):
            self.winning_list.append(self.single_game())

    def get_results(self):
        """
        Collects and returns all results from
         run_simulation as a list of tuples
        Returns
        -------
        list: [(turns, winning player type), .....]
        """
        return self.winning_list

    def winners_per_type(self):
        """
        Returns a dictionary mapping player types to
        the number of wins
        Returns
        -------
        dict:{'Player type' : number of wins, ......}
        """
        
        return dict(Counter(elem[1] for elem in self.winning_list))

    def durations_per_type(self):
        """
        Returns a dictionary mapping player types to
        lists of game durations for that type
        Returns
        -------
        dict: {'Player type': [num turns of games won, .....]}
        """
        player_turn_count = {}

        for winning_tuple in self.winning_list:
            num_turns = winning_tuple[0]
            player = winning_tuple[1]

            if player not in player_turn_count:
                player_turn_count[player] = [num_turns]
            else:
                player_turn_count[player].append(num_turns)

        return player_turn_count

    def players_per_type(self):
        """
        Returns a dictionary showing how many players of
        each type participate
        Returns
        -------
        dict: {'Player type': number of that type participating}
        """
        return dict(Counter(player.__name__
                    for player in self.player_field))
"""

``Simulation`` class
--------------------

The ``Simulation`` class manages an entire simulation.

In addition to the board, the ``Simulation`` constructor receives - a
random seed to seed the random number generator; - a boolean flag
indicating whether the order or players should be randomized before the
start of each game played; - a list of player *classes*: for each game,
a list of player objects will be created, one player for each entry in
the list.

The example below shows a constructor call for simulations on the
default board in which two players, three resilient players and one lazy
player compete with each other, using a different starting order in each
game:

.. code:: python

   sim = Simulation([Player, Player, ResilientPlayer, ResilientPlayer,
                     ResilientPlayer, LazyPlayer],
                     randomize_players=True)


The class has the following methods:

1. ``single_game()`` runs a single game returning a tuple consisting of
   the number of moves made and the type of the winner, e.g.
   ``(25, 'LazyPlayer')``.
2. ``run_simulation()`` runs a given number of games and stores the
   results in the ``Simulation`` object. It returns nothing.
3. ``get_results()`` returns all results generated by
   ``run_simulation()`` calls so far as a list of result tuples, e.g.,
   ``[(10, 'Player'), (6, 'ResilientPlayer')]``.
4. ``winners_per_type()`` returns a dictionary mapping player types to
   the number of wins, e.g.,
   ``{'Player': 4, 'LazyPlayer': 2, 'ResilientPlayer': 5}``
5. ``durations_per_type()`` returns a dictionary mapping player types to
   lists of game durations for that type, e.g.,
   ``{'Player': [11, 25, 13], 'LazyPlayer': [39], 'ResilientPlayer': [8, 7, 6, 11]}``
6. ``players_per_type`` returns a dictionary showing how many players of
   each type participate, e.g.,
   ``{'Player': 3, 'LazyPlayer': 1, 'ResilientPlayer': 0}``
"""

s = Simulation([Player, LazyPlayer, ResilientPlayer])
p = s.players_per_type()
print(p)