# Abir Taheer
# IntroCS pd1
# HW39 -- Removal Three Ways
# 2019-04-12


def listFib(n):
    # Set up a list with the first 2 fibonacci numbers
    nums = [0, 1]

    # While we still don't have enough numbers in the list, add as many fibonacci items until we reach enough
    while len(nums) < n:
        # Each new fibonacci number is the sum of the two numbers before it
        nums += [nums[len(nums) - 1] + nums[len(nums) - 2]]

    # Return the first n items in the fibonacci list
    return nums[:n]


def rm_negatives(L):
    # Create a new list to store all of the positive values
    new_list = []

    # Iterate through all of the values in the original list, adding them if they are positive
    for x in L:
        if L[x] >= 0:
            new_list += [x]
        x += 1

    # Return the new list
    return new_list


"""
POP: Removes the item at a given index of a python list
syntax: [1, 3, 2].pop(0) -> [3, 2]
behavior: Affects the original list. Returns the deleted item.

REMOVE: Removes the first instance of a given item in a list
syntax: [1, 3, 2].remove(3) -> [1, 2]
behavior: Affects the original list. Does not return a new list

DEL: Removes an item at a given index or index range.
syntax: del [1, 2, 3][0] -> [2, 3]
behavior: Affects the original list. Does not return the item that was removed

Shweet prefers del for use in rmNegatives() because we do not need the removed item in this given scenario so it doesn't make sense to use pop in favor of delete. 
"""


def rmNegatives(L):
    # Initialize a counter
    x = 0

    # Iterate through the list
    while x < len(L):
        # If the current item is less than 0, remove it and move the counter back one to offset it for the missing item
        if L[x] < 0:
            del L[x]
            x -= 1
        # Increment the counter and move onto the next item
        x += 1

    # Return the new list with negatives removed
    return L
