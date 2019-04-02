# Abir Taheer
# IntroCS pd1
# HW25 -- I Am Still Searching...
# 2019-03-18


def index_of(target_char, search_space):
    """
    Search a string for a character and return the index of the first match
    :param target_char: the character to match
    :param search_space: the string to search
    :type target_char: str
    :type search_space: str
    :return: the index of the first occurence of the search character in the search string
    :rtype: int

    >>> index_of('t',"Gotta get up to get down.")
    2

    >>> index_of('q',"Gotta get up to get down.")
    -1

    >>> index_of('b', 'banana')
    0

    >>> index_of('r', 'abir')
    3

    >>> index_of('z', 'awesome')
    -1
    """

    # Initialize a counter
    x = 0

    # Look at each character in the search string
    while x < len(search_space):
        # If the current character being compared is a match, return the current value of the counter
        if search_space[x] == target_char:
            return x
        x += 1
    # If we made it to this point, we don't have any matches. Return -1
    return -1
