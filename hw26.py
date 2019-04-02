# Abir Taheer
# IntroCS pd1
# HW26 -- 000 000 111, v10
# 2019-03-18


def bondify(name: str) -> str:
    """
    :param name: The name of the person
    :return: The name, bondified

    >>> bondify("Abir Taheer")
    'Taheer, Abir Taheer'

    >>> bondify("banana man")
    'man, banana man'

    >>> bondify("coolio")
    'coolio, coolio'
    """
    loc = name.find(" ")
    return name[loc + 1:] + ", " + name


def replace(s: str, q: str, r: str) -> str:
    """
    :param s: The original string
    :param q: The string  to match in the original string
    :param r: The string to replace the match with
    :return: The new string with the replacement in place

    >>> replace("hello from the other side", "other", "banana")
    'hello from the banana side'

    >>> replace("Winter is coming", "Winter", "Spring")
    'Spring is coming'

    >>> replace("Dolphins run this planet", "dolphins", "mice")
    'Dolphins run this planet'
    """
    loc = s.find(q)
    if loc == -1:
        return s
    beginning = s[:loc]
    end = s[loc + len(q):]
    return beginning + r + end
