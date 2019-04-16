# Abir Taheer
# IntroCS pd1
# HW40 -- Oh, Give Me a Home Where the Buffalo Roam
# 2019-04-15
import random


def merge(L1, L2):
    """
    Returns a new list containing the elements of both lists, in sorted (ascending) order.
    Assumes each input list is sorted. Length of output list must equal sum of lengths of input lists.
    :param L1: The first list to combine
    :param L2: The second list to combine
    :return: The combined & sorted list with all of the elements from the original lists

    >>> merge([0, 2, 4, 6, 8],  [1, 3, 5, 7])
    [0, 1, 2, 3, 4, 5, 6, 7, 8]

    >>> merge([-5, -4, -1, 5], [-3, 2, 4])
    [-5, -4, -3, -1, 2, 4, 5]
    """

    # Make a variable to store the two combined lists
    combined = L1 + L2

    # Make a variable to add an offset with the lowest number, solves the case with any negative numbers
    offset = 0 - min(combined)

    # Create a bucket to store the frequencies of items in the lists
    buckets = [0 for x in range(max(combined) + offset + 1)]

    # Make a variable to store the new list
    new_list = []

    # Add to the counters for each of the items in the bucket
    for x in combined:
        buckets[x + offset] += 1

    # Construct a new list based on the frequencies of the original lists
    for x in range(len(buckets)):
        for y in range(buckets[x]):
            new_list.append(x - offset)

    # Return the new list
    return new_list


def rand_list(n):
    """
    Returns a list with n elements where each element is a randomly generated number from range 0 to 99999
    :param n: The number of random items wanted
    :return: A list containing n random integers

    >>> test_rand_list()
    True
    """

    # Make a list to contain the numbers
    nums = []

    # Add new random items to the list for as many times as was asked
    nums += [random.randrange(100000) for x in range(n)]

    # Return the list of the negative numbers
    return nums


def rand_ip():
    """
    Return a random IPv4 address
    :return: A string resembling an IP address
    """
    return ".".join([str(random.randrange(256)) for x in range(4)])


def test_rand_ip():
    """
    Tests the rand_ip function based on the rules of an IP address:
    * There are 4 Octets
    * Each octet is smaller than 256
    * Each octet is equal to or greater than 0
    :return: Whether or not the rand_ip function passed all test cases

    >>> test_rand_ip()
    True
    """

    # Test the function 1000 times for safety
    for x in range(1000):

        # Make a variable to store the different octets received from the function
        ip_parts = [int(x) for x in rand_ip().split(".")]

        # Check to make sure there are 4 octets
        if len(ip_parts) != 4:
            return False

        # Make sure each of the octets is in the proper range
        for y in ip_parts:
            if y > 255 or y < 0:
                return False

    # If the function gets to this stage, it has passed all of the tests
    return True


def test_rand_list():
    """
    Tests to make sure that the rand_list function works properly
    :return: Whether or not the rand_list function passed all test cases

    >>> test_rand_list()
    True
    """

    # Test out the function 1000 times
    for x in range(1000):

        # Generate a random number to test the function with
        test_amount = random.randrange(1000)

        # If the function did not return the correct number of items, return False
        if test_amount != len(rand_list(test_amount)):
            return False

    # If it makes it to this point, return True
    return True

