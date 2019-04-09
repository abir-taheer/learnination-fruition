# Abir Taheer
# IntroCS pd1
# HW37 -- Bucket List
# 2019-04-08


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


def is_int(num: object) -> bool:
    return str(num * 2) != str(num) * 2


def mean_list(nums: list) -> int:
    sum = 0
    count = 0
    for x in nums:
        if is_int(x):
            sum += x
            count += 1
    return sum / count


def mode_list(nums: list) -> list:
    """
    Return the most occurring item in a list
    :param nums: A numerical list
    :return: The item that appears the most in the list

    >>> mode_list([1, 2, 3, 1, 2])
    [1, 2]

    >>> mode_list([-1, -4, 9, 2, -4, 9, -4])
    [-4]

    >>> mode_list(["hello", 0, 2, 3, 2, "hello", "hello"])
    ['hello']
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

    # Find the first instance of the highest frequency that appeared
    highest_frequency = frequency[max_pos(frequency)]

    # Initialize a variable to store the list containing the modes
    modes = []

    # Iterate through the list of frequencies
    for x in range(len(frequency)):

        # If any of the frequencies are the same as the max, add their correlated number to the list of modes
        if highest_frequency == frequency[x]:
            modes.append(numbers[x])

    # Return the list of modes
    return modes


# I don't know why, but I thought I might need this. Guess I didn't
def bubble_sort(nums: list) -> list:
    conflict = True
    while conflict:
        conflict = False
        for x in range(len(nums) - 1):
            if nums[x] > nums[x + 1]:
                conflict = True
                nums[x], nums[x + 1] = nums[x + 1], nums[x]
    return nums


def bar_graphify(nums):
    """

    :param nums:

    >>> bar_graphify([0, 1, 2, 3])
    0:
    1: =
    2: ==
    3: ===

    >>> bar_graphify([1, 0, 3, 2])
    0: =
    1:
    2: ===
    3: ==
    """
    for x in range(len(nums)):
        line = str(x) + ": "
        for y in range(nums[x]):
            line += "="
        print(line)