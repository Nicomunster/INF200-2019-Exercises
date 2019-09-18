
def squares_by_comp(n):
    """
    This function returns the squares of numbers with a remainder of 1 when when divided by 3.
    The function does this by using a list comprehension.

    Parameters
    ----------
    n
        Numbers up to this value will be squared.

    Returns
    -------
    list
        list of squares of numbers up to n which have a remainder of 1 when divided by 3.
    """
    return [k**2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    """
    This function returns the squares of numbers with a remainder of 1 when when divided by 3.
    The function does this by using a for-loop.

    Parameters
    ----------
    n
        Numbers up to this value will be squared.

    Returns
    -------
    list
        list of squares of numbers up to n which have a remainder of 1 when divided by 3.
    """
    squares = []
    for k in range(n):
        if k % 3 == 1:
            squares.append(k**2)
    return squares


if __name__ == '__main__':
    m = 100
    print(squares_by_loop(m))
    if squares_by_comp(m) != squares_by_loop(m):
        print('ERROR!')
