# -*- coding: utf-8 -*-

__author__ = 'Nicolai Munsterhjelm'
__email__ = 'nicolai.munsterhjelm@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.seed = seed
        self.a = 7**5
        self.m = 2**31 - 1

    def rand(self):
        """Generates a random number using the LCG method,
         based on the seed."""
        self.seed = (self.a * self.seed) % self.m
        return self.seed


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
