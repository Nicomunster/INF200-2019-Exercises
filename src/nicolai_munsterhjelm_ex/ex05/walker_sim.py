# -*- coding: utf-8 -*-

__author__ = 'Nicolai Munsterhjelm'
__email__ = 'nicmust@nmbu.no'


import random


class Walker:
    def __init__(self, start, home):
        """
        :param start: initial position of the walker
        :param home: position of the walker's home
        """

        self.position = start
        self.home = home
        self.steps = 0

    def move(self):
        """Change coordinate by +1 or -1 with equal probability."""
        self.position += random.choice((-1, 1))
        self.steps += 1

    def is_at_home(self):
        """Returns True if walker is at home position."""
        if self.position == self.home:
            return True
        else:
            return False

    def get_position(self):
        """Returns current position."""
        return self.position

    def get_steps(self):
        """Returns number of steps taken by walker."""
        return self.steps


class Simulation:
    def __init__(self, start, home, seed):
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
        """

        self.start = start
        self.home = home
        random.seed(seed)

        self.walker = Walker(self.start, self.home)

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """

        while not self.walker.is_at_home():
            self.walker.move()

        return self.walker.steps

    def run_simulation(self, num_walks):
        """
        Run a set of walks, returns list of number of steps taken.

        Arguments
        ---------
        num_walks : int
            The number of walks to simulate

        Returns
        -------
        list[int]
            List with the number of steps per walk
        """

        return [self.single_walk() for _ in range(num_walks)]

if __name__ == "__main__":
    sim = Simulation(10, 0, 125)
    print(sim.run_simulation(10))