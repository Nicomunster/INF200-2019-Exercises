# -*- coding: utf-8 -*-

__author__ = 'Nicolai Munsterhjelm'
__email__ = 'nicmust@nmbu.no'


import random
import walker_sim


class BoundedWalker(walker_sim.Walker):
    def __init__(self, start, home, left_limit, right_limit):
        """
        Initialise the walker

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        self.start = start
        self.home = home
        self.left_limit = left_limit
        self.right_limit = right_limit

        super().__init__(start, home)

    def move(self):
        """Change coordinate by +1 or -1 with equal probability.
        Is bounded by left_limit and right_limit."""
        self.position += random.choice((-1, 1))

        if self.position < self.left_limit:
            self.position += 1
        elif self.position > self.right_limit:
            self.position -= 1
        else:
            self.steps += 1


class BoundedSimulation(walker_sim.Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        self.start = start
        self.home = home
        random.seed(seed)
        self.left_limit = left_limit
        self.right_limit = right_limit

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.
        Walk is bounded by left and right limit.

        Returns
        -------
        int
            The number of steps taken
        """

        walker = BoundedWalker(self.start, self.home, self.left_limit, self.right_limit)

        while not walker.is_at_home():
            walker.move()

        return walker.steps


if __name__ == "__main__":
    left_limits = [0, -10, -100, -1000, -10000]
    for left_limit in left_limits:
        bounded_sim = BoundedSimulation(0, 20, 12345, left_limit, 20)
        print(f"left_limit: {left_limit}, "
              f"number of steps:", bounded_sim.run_simulation(20))
