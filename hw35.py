# Abir Taheer
# IntroCS pd1
# HW35 -- Float Like a Butterfly, Sting Like a Bee_
# 2019-04-04   


def min_pos(L: []) -> int:
    """
    Find the index of the smallest item in a list
    :param L: An integer list to find the minimum of
    :returns: The index of the lowest number in the list

    >>> min_pos( [3] )
    0

    >>> min_pos( [5,4,3,2,1] )
    4

    >>> min_pos( [17, -5, -45, 90, 3] )
    2

    >>> min_pos( [100, 2000, 20000, 0, 9] )
    3
    """
    # Initialize a variable to store the index of the min
    index_of_min = 0

    # Iterate through all of the items in the list
    for x in range(len(L)):

        # Check if the current item is less than the current minimum found
        if L[index_of_min] > L[x]:

            # If it is less, change the value of the min index to the current index being checked
            index_of_min = x

    # Return the index of the item with the min value
    return x
