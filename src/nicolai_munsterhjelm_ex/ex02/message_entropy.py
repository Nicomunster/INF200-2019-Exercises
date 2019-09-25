from math import log2


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


def entropy(message):
    """This function computes the message entropy of a string.
    The entropy is defined as sum(p_i log_2(p_i)), where p_i
    is the frequency of letter i in the message.

    Parameters
    ----------
    message (string)
        The string for which the entropy is the be computed.

    Returns
    -------
    h (float)
        The entropy of the message.
    """

    frequencies = letter_freq(message)
    n = sum(frequencies.values())

    h = 0

    for n_i in frequencies.values():
        p_i = n_i/n
        h += - p_i * log2(p_i)

    return h


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
