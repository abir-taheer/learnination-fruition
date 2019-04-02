# Team nice_people
# Shah Wafi, Abir Taheer, Alex Tang
# IntroCS pd1
# HW16 -- Boolean Logic, Conditionals, Oh My!
# 2018-03-01

def cartDist(X1: float, Y1: float, X2: float, Y2: float) -> float:
    """
    takes numeric inputs X1, Y1, X2, Y2 -- representing coordinate pairs (x1,y1) and (x2,y2)
    :rtype: int
    :param X1: The x coordinate of the first point
    :param Y1: The y coordinate of the first point
    :param X2: The x coordinate of the second point
    :param Y2: The y coordinate of the seconds point
    :return: returns the distance between the two points

    >>> cartDist(0,0,0,0)
    0.0

    >>> cartDist(4,4,4,4)
    0.0

    >>> cartDist(0,0,3,4)
    5.0
    """
    # Insert the values in to the distance formula and return the result
    return (((X2 ** 2) - (X1 ** 2)) + ((Y2 ** 2) - (Y1 ** 2))) ** (1 / 2)


def pythTriple(a: int, b: int, c: int) -> bool:
    """
    Takes numeric inputs a, b, c -- representing side lengths of a triangle
    :param a: The first side of the triangle
    :param b: The second side of the triangle
    :param c: The third side of the triangle
    :returns: Whether the the parameters constitute a Pythagorean triple.
    :rtype: bool

    >>> pythTriple(0,0,0)
    False

    >>> pythTriple(3,4,5)
    True

    >>> pythTriple(3,4,6)
    False

    >>> pythTriple(32,255,257)
    True

    """

    # If any parameter is equal to or less than 0, return False
    if a <= 0 or b <= 0 or c <= 0:
        return False

    # Make sure that c is equal to the largest number
    if b > c and b > a:
        temp = c
        c = b
        b = temp
    elif a > c and a > b:
        temp = c
        c = a
        a = temp

    # Return the result of a pythagorean triple comparison
    return (a ** 2) + (b ** 2) == (c ** 2)



