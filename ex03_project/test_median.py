
# -*- coding: utf-8 -*-

__author__ = 'Nicolai Munsterhjelm'
__email__ = 'nicmunst@nmbu.no'

# The source of the code for the median() function is the
# INF200 Exercise 3 text by Yngve Mardal Moe.

def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sdata = sorted(data)
    n = len(sdata)
    return (sdata[n//2] if n % 2 == 1
            else 0.5 * (sdata[n//2 - 1] + sdata[n//2]))


def test_single_element():
    """Tests that the median function returns the correct value for
    a single element list"""
    assert median([5]) == 5


def test_odd_number():
    """Tests that the median function returns the correct value for lists
    with odd numbers of elements"""
    assert median([5, 4, 3, 2, 1]) == 3
    assert median([1, 43, 21]) == 21


def test_even_number():
    """Tests that the median function returns the correct value for lists
     with even number of elements"""
    assert median([4, 3, 2, 1]) == 2.5
    assert median([1, 43]) == 22


def test_ordered():
    """Tests that the median function returns the correct value for lists
    with ordered elements"""


def test_reverse_ordered():
    """Tests that the median function returns the correct value for
     reverse-ordered lists"""


def test_unordered():
    """Tests that the median function returns the correct value for
    unordered lists"""


def test_empty_list():
    """Tests that the median of an empty list raises a ValuError exception"""


def test_original_unchanged():
    """Tests that the median function leaves the original data unchanged"""


def test_tuples_and_lists():
    """Tests that the median function works for tuples as well as lists"""
