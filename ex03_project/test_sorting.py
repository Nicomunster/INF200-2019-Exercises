
__author__ = 'Nicolai Munsterhjelm'
__email__ = 'nicmunst@nmbu.no'


def bubble_sort(data):
    """This function sorts a tuple or list of numbers using the bubble sort algorithm.

    Parameters
    ----------
    data (tuple or list)
        The tuple/list to be sorted.

    Returns
    -------
    new_list (list)
        Sorted list.
    """

    new_list = list(data)

    for i in range(len(new_list) - 1):
        for j in list(range(len(new_list) - 1 - i)):
            if new_list[j] > new_list[j + 1]:
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]

    return new_list


def test_empty():
    """Test that the sorting function works for empty list"""
    assert bubble_sort([]) == []


def test_single():
    """Test that the sorting function works for single-element list"""
    assert bubble_sort([1]) == [1]


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert bubble_sort(data) is not sorted_data


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert data == [3, 2, 1]


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert bubble_sort(data) == data


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert bubble_sort(data) == data.reverse()


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    pass


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    pass