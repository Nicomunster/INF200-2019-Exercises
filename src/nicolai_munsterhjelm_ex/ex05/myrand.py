# -*- coding: utf-8 -*-

__author__ = 'Nicolai Munsterhjelm'
__email__ = 'nicolai.munsterhjelm@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        """
        Initialise a linear congruence random number generator.

        Arguments
        ---------
        seed : int
            The initial seed for the generator
        """
        self.hidden_state = seed
        self.a = 7**5
        self.m = 2**31 - 1

    def rand(self):
        """Generates a random number using the LCG method,
         based on the seed."""
        self.hidden_state = (self.a * self.hidden_state) % self.m
        return self.hidden_state


class ListRand:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def rand(self):
        if self.index >= len(self.numbers):
            raise RuntimeError("ERROR: No more numbers in list")
        list_number = self.numbers[self.index]
        self.index += 1
        return list_number
