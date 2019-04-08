# Team pyDriven
# Abir Taheer & Alif Rahman
# IntroCS pd1
# HW36 -- Back in the [Co]Driver’s Seat, Looping_FTW
# 2019-04-07


def list_sum(L):
    """
    Takes a list (L), containing only numbers, and returns the least value
    :param L: A numerical list
    :return: The sum of L's elements

    >>> list_sum( [0,1,2,3] )
    6
    """
    sum = 0
    for i in L:
        sum += i
    return sum


def min_val(L):
    """
    Takes a list and returns the least value. Returns question mark if list contains strings
    :param L: The list to search, can contain both numbers and strings
    :return: The least value or question mark (if items in list L are strings)
    >>> min_val( [3] )
    3
    >>> min_val( [5,4,3,2,1] )
    1
    >>> min_val( ["free", "fee","phi","pho","phum","Free", "Fee","Phi","Pho","Phum",] )
    '?'
    """
    minimum = L[0]
    for number in L:
        if number < minimum:
            minimum = number
        if number * 2 == str(number) + str(number):
            return "?"
    return minimum


def list_find(L: list, q: object) -> int:
    """
    Return the index of the first matching item in a list
    :param L: The list to search
    :param q: The item to find
    :return: Index of first occurrence or -1 if not found

    >>> list_find( [5,4,3,2,1], 2 )
    3

    >>> list_find( [5,4,3,2,1], 6 )
    -1

    >>> list_find( [5,4,'cat','dog', 'cat'], 'cat' )
    2
    """

    # Check every item in the given list
    for x in range(len(L)):

        # If the item is a match, return its index
        if L[x] == q:
            return x

    # After we've checked all items without matches, return -1
    return -1


def min_pos(L: list) -> int:
    """
    Return the index of the lowest number in a list
    :param L: A numerical list
    :return: Index of the lowest number
    """

    # Assume that the lowest number is at index 0
    min_index = 0

    # Check all numbers in list
    for x in range(len(L)):

        # If current number being checked is less than the number previously assumed to be lowest, update min_index
        if L[min_index] > L[x]:
            min_index = x

    # Return the index that the lowest number was found at
    return min_index


def max_pos(L: list) -> int:
    """
    Return the index of the largest number in a list
    :param L: A numerical list
    :return: Index of largest number

    >>> max_pos([2, 3, 1, 0])
    1

    >>> max_pos([0, 2, 1, 2, 6, 9])
    5

    >>> max_pos([0, 3, 5, 2, 5, 3])
    2
    """

    # Assume the largest number is at index 0
    max_index = 0

    # Check all numbers in the list
    for x in range(len(L)):

        # If current number being checked is less than the number previously assumed to be the largest, update max_index
        if L[max_index] < L[x]:
            max_index = x

    # Return the index of the largest number
    return max_index


def list_mode(nums: list) -> int:
    """
    Return the most occurring item in a list
    :param nums: A numerical list
    :return: The item that appears the most in the list

    >>> list_mode([1, 2, 3, 1])
    1

    >>> list_mode([-1, -4, 9, 2, -4, 9, -4])
    -4

    >>> list_mode(["hello", 0, 2, 3, 2, "hello", "hello"])
    'hello'
    """

    # Initialize two variables
    # Numbers will hold all unique items that appear in the provided list
    numbers = []

    # Frequency will store how many times each item at the same index of numbers appears in the provided list
    frequency = []

    # Check all items in the provided list
    for x in nums:

        # Check if it appears in numbers
        if list_find(numbers, x) == -1:
            # If it does not appear in numbers, add it to numbers and to the frequency lists
            # They are both added at the same time and their indexes in each list will correspond to each other
            numbers.append(x)
            frequency.append(0)

        # Find the item in the numbers list and increment its counter at the same index of the frequency list
        frequency[list_find(numbers, x)] += 1

    # Return the item from the numbers list that has the same index as the index of the
    # highest number in the frequency list
    return numbers[max_pos(frequency)]
