# Team Try It
# Abir Taheer, Stone Su
# IntroCS pd1
# HW20 -- Repetition, Two Ways
# 2019-03-12


def fact_rec(n: int) -> int:
    """
    Calculates the factorial of a given integer using a recursive method
    :param n: The number to calculate the factorial of
    :type n: int
    :rtype: int
    :return: The factorial of the given number
    >>> fact_rec(0)
    1

    >>> fact_rec(1)
    1

    >>> fact_rec(2)
    2

    >>> fact_rec(3)
    6

    >>> fact_rec(4)
    24
    """
    # specify our known case for the recursive function
    if n <= 0:
        return 1

    # keep calling the function and multiplying by n until we reach our known case
    return n * fact_rec(n - 1)


def fact_iter(n: int) -> int:
    """
    Calculates the factorial of a number using an iterative method
    :param n: The number to calculate the factorial of
    :type n: int
    :return: The factorial of the given number
    :rtype: int

    >>> fact_iter(0)
    1

    >>> fact_iter(1)
    1

    >>> fact_iter(2)
    2

    >>> fact_iter(3)
    6

    >>> fact_iter(4)
    24
    """
    # instantiate variables to store the current number to multiply as well as the product up until that certain point
    product = 1
    counter = 1

    # if a negative input is given, return 0
    if n < 0:
        return 0

    while counter <= n:
        # multiply the product by the counter
        product = product * counter
        # increment the counter
        counter += 1
    return product
