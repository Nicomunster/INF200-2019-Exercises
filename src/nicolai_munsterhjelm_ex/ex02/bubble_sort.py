def bubble_sort(data):
    """This function sorts a tuple or list of numbers using the bubble sort algorithm.

    Parameters
    ----------
    data (tuple or list)
        The tuple/list to be sorted.

    Returns
    -------
    new_list
        Sorted list.
    """

    new_list = list(data)

    for i in range(len(new_list) - 1):
        for j in list(range(len(new_list) - 1 - i)):
            if new_list[j] > new_list[j + 1]:
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]

    return new_list


if __name__ == "__main__":

    print(bubble_sort(['a', 'hello', '1234', ':)']))

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))

