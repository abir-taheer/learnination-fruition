# Abir Taheer
# IntroCS pd1
# HW24 -- 000 000 111
# 2019-03-14


def bondify(n):
    """
    Return a name in the James Bond format
    :param n: The name to 'bondify'
    :type n: str
    :return: The bondified name
    :rtype: str

    >>> bondify('Abir Taheer')
    'Taheer, Abir Taheer'

    >>> bondify("Thluffy Sinclair")
    'Sinclair, Thluffy Sinclair'

    >>> bondify("William Harris")
    'Harris, William Harris'
    """
    nani = n.split(" ")
    return nani[1] + ", " + n
