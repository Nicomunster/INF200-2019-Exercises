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

    def random_sequence(self, length):
        return RandIter(self, length)


    def infinite_random_sequence(self):
        """
        Generate an infinite sequence of random numbers.

        Yields
        ------
        int
            A random number.
        """
        while True:
            yield self.rand()


class RandIter:
    def __init__(self, random_number_generator, length):
        """

        Arguments
        ---------
        random_number_generator :
            A random number generator with a ``rand`` method that
            takes no arguments and returns a random number.
        length : int
            The number of random numbers to generate
        """
        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = None

    def __iter__(self):
        """
        Initialise the iterator.

        Returns
        -------
        self : RandIter

        Raises
        ------
        RuntimeError
            If iter is called twice on the same RandIter object.
        """
        if self.num_generated_numbers is not None:
            raise RuntimeError
        self.num_generated_numbers = 0

        return self

    def __next__(self):
        """
        Generate the next random number.

        Returns
        -------
        int
            A random number.

        Raises
        ------
        RuntimeError
            If the ``__next__`` method is called before ``__iter__``.
        StopIteration
            If ``self.length`` random numbers are generated.
        """
        if self.num_generated_numbers is None:
            raise RuntimeError('Cannot call "next" before '
                               'RandIter is initialized as an iterator')
        if self.num_generated_numbers == self.length:
            raise StopIteration

        random_number = self.generator.rand()
        self.num_generated_numbers += 1

        return random_number


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


if __name__ == "__main__":
    generator = LCGRand(1)
    for rand in generator.random_sequence(10):
        print(rand)

    for i, rand in generator.infinite_random_sequence():
        print(f'The {i}-th random number is {rand}')
        if i > 100:
            break
