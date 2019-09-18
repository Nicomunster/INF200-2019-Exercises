
def letter_freq(txt):
    """
    This function counts the letters/characters in a string, and stores the frequencies in a dictionary.

    Parameters
    ----------
    txt
        String from which letters will be counted.

    Returns
    -------
    counts
        Dictionary with letter counts.

    """
    counts = {}
    for char in txt.lower():
        if char in counts.keys():
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in sorted(frequencies.items()):
        print('{:3}{:10}'.format(letter, count))
