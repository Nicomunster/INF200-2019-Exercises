
def char_counts(textfilename):
    """Counts number of each utf-8-character in the given file.
    Returns a list 'result', where result[i] gives the number
    of occurrences of character code i.

    Parameters
    ----------
    textfilename (string)
        The file that is to be counted

    Returns
    -------
    result (list)
        List with numbers corresponding to the number of occurrences of character with character code i.

    """

    result = [0] * 256

    with open(textfilename, mode='r', encoding='UTF--8') as file:
        for char in file.read():
            result[ord(char)] += 1

    return result


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
