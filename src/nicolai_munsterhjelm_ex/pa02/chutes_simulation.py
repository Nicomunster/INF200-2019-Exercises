# -*- coding: utf-8 -*-

__author__ = 'Alf Georg Ovland', 'Nicolai Munsterhjelm'
__email__ = 'alov@nmbu.no', 'nicmunst@nmbu.no'

import random

class Board:
    def __init__(self, ladders=None, chutes=None, goal=90):
        if ladders is None:
            ladders = [(1, 40), (8, 10), (36, 52), (43, 62), (49, 79),
                       (65, 82), (68, 85)]
        if chutes is None:
            chutes = [(24, 5), (33, 3), (42, 30), (56, 37), (64, 27),
                      (74, 12), (87, 70)]

        self.ladders = dict(ladders)
        self.chutes = dict(chutes)
        self.goal = goal
        #self.chute_last = False
        #self.ladder_last = False

    def goal_reached(self, position):
        return position >= 90

    def position_adjustment(self, position):
        #self.chute_last = False
        #self.ladder_last = False
        if position in self.ladders.keys():
            #self.ladder_last = True
            return self.ladders[position] - position
        elif position in self.chutes.keys():
            #self.chute_last = True
            return self.chutes[position] - position
        return 0

"""
`Board`` class
---------------

The ``Board`` class shall manage all information about ladders, snakes,
and the goal.

1. If no parameters are given to the ``Board`` constructor, it shall
   create a standard board, with the snakes, ladders, and goal as in
   PA01.
2. Method ``goal_reached()`` shall return true if it is passed a
   position at or beyond the goal.
3. Method ``position_adjustment()`` shall handle changes in position due
   to snakes and ladders. It accepts a position as argument and returns
   the number of positions the player must move forward (in case of a
   ladder) or backward (chute), to get to the correct position. If the
   player is not at the start of a chute or ladder, the method returns
   0.
"""
class Player:
    def __init__(self, board_instance):
        self.board_instance = board_instance
        self.position = 0
    def move(self):
        roll = random.randint(1, 6)
        self.position += roll
        self.position = \
            self.board_instance.position_adjustment(self.position)



"""
``Player`` class
----------------

The ``Player`` class and its subclasses manage information about player
position, including information on which board a player “lives”. 1. The
player constructor must receive the board as argument:

.. code:: python

           board = Board()
           player = Player(board)

1. The ``move()`` method moves the player by implementing a die cast,
   the following move and, if necessary, a move up a ladder or down a
   chute. It does not return anything.
"""

class ResilientPlayer(Player):
    def __init__(self, board_instance, extra_steps=None):
        if extra_steps is None:
            extra_steps = 1
        self.extra_steps = extra_steps
        self.chute_last = False
        self.board_instance = board_instance
        super().__init__(self.board_instance)

    def move(self):

        roll = random.randint(1, 6)
        self.position += roll
        if self.chute_last:
            self.position += self.extra_steps
            self.chute_last = False
        pre_adjust = self.position
        self.position = \
            self.board_instance.position_adjustment(self.position)
        if pre_adjust > self.position:
            self.chute_last = True
        # self.step += 1



"""
``ResilientPlayer`` class
~~~~~~~~~~~~~~~~~~~~~~~~~

This is a subclass of ``Player`` with slightly different moving
behavior: When a resilient player slips down a chute, he will take extra
steps in the next move, in addition to the roll of the die. The number
of extra steps is provided as an argument to the constructor, default is
1. Extra steps are taken immediately after the steps prescribed by the
die and before snakes and ladders are checked.

"""
class LazyPlayer:
    def __init__(self, board_instance, back_steps=None):
        if back_steps is None:
            back_steps = 1
        self.back_steps = abs(back_steps)
        self.board_instance = board_instance
        super().__init__(self.board_instance)

    def move(self):
        roll = random.randint(1, 6)
        if self.board_instance.ladder_last:
            lazy_move = roll - self.back_steps
            if lazy_move < 0:
                return
            else:
                self.position += (roll - self.back_steps)

        self.position = \
            self.board_instance.position_adjustment(self.position)
"""

``LazyPlayer`` class
~~~~~~~~~~~~~~~~~~~~

This is a subclass of ``Player`` as well. After climbing a ladder, a
lazy player drops a given number of steps. The number of dropped steps
is an optional argument to the constructor, default is 1. The player
never moves backward: if, e.g., the die cast results in 1 step and the
player is to drop 3 steps, the player does not move -2 steps but just
stays in place.

"""
class Simulation:
    def __init__(self):
        pass
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