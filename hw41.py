# Team Carrots
# Asma Berri & Abir Taheer
# StuyCS -- Spring 2019 IntroCS pd1
# HW41 -- How to Properly Use a Phonebook
# 2019-16-04


import random


def rand_list(n, limit):
    """	return a list of n random integers on range [0,limit) """
    g = []
    while n > 0:
        g.append(random.randrange(limit))
        n -= 1
    return g


# ==================================================
# Problem 0

# data is a sorted list of 1000 random integers.
data = sorted(rand_list(1000, 1000))
print(data)

# i) Where in the list would you find the value 673 (it may or may not be in the list)?
# ==============

# It is possible that 673 is not in the list because the list contains randomly generated values so 673 may not have been generated.
# If 673 is in the list, it would be found in the upper middle of the list; 3rd quarter.

# ==============

# ii) Where in the list would you find the value 429 (it may or may not be in the list)?
# ==============
# It is possible that 673 is not in the list because the list contains randomly generated values so 429 may not have been one of them.
# If 429 is in the list, it would be found in the lower middle of the list; 2nd quarter.
# ==============

# End Problem 0
# ==================================================


# ==================================================
# Problem 1

# i) Find the middle index of data (the index that splits a into 2 half sections).
#    use len(data) and any arithmetic operators
# ==============

middle_index_data = (len(data) // 2) + 1

# ==============

# ii) Find the index of data that splits it into two sections, the first with 1/4th of the values
#     the other with 3/4th of the values
# ==============

quarter_index_data = (middle_index_data // 2) + 1

# ==============

# iii) Find the index of data that splits it into two sections, the first with 3/4th of the values
#       the other with 3/4th of the values
# ==============
three_fourths_index = len(data) - quarter_index_data
# ==============

# iii) Find the index of data that splits it into two sections, the first with 7/8th of the values
#       the other with 1/8th of the values
# ==============
seven_eights_index = len(data) - (quarter_index_data // 2) + 1


# ==============


# End Problem 1
# ==================================================


# ==================================================
# Problem 2

# Slow search: Write a function that searches for a value in a list.
# It should return the index of the value, or -1.
# This function should just look through each element to find the key,
# don't do anything clever.
# It should also print out the total number of loops it took to complete
def slow_search(g, key):
    i = 0
    count = 0  # loop counts
    # ==============
    for x in g:
        count += 1  # add 1 to count
        if g[i] == key:  # check if the element at index i is the key
            print(count, 'loops')
            return i  # if it is, return the index and loop count
        else:
            i += 1  # if it isn't, add 1 to the index
    # ==============
    print(count, 'loops')
    return -1


a = [1, 2, 3, 4, 5, 673, 10]
print(slow_search(a, 673))
# 6 loops
# 5

g = [1, 2, 3, 4, 5, 6, 20, 25, 30000, 67, 58]
print(slow_search(g, 673))


# 11 loops
# -1

# End Problem 2
# ==================================================


# ==================================================
# Problem 3

# What do you know about your data? Are there aspects of the data that will allow you to implement a significantly
# faster search algorithm? If so, what are they?

# ============== Our data is sorted! That means that the min and the max items are always at the first and last index
# respectively. This allows us to keep splitting the lists in half, using those as indicators to see
# which of the sublists we would find the key in
# ==============

# Usually, you want a search function to only need 2 parameters:
# the list and the element you seek (key).
# Hence the wrapper function, fast_search, taking only 2 parameters.
# Our fast search needs more information,
# so its helper function will incorporate this extra info:

def fast_search(g, key):
    # Start it up by asking the fast search to check the entire list
    return fast_search_help(g, key, 0, len(g) - 1, 0)


# Here is our fast search. We are looking for key in g.
# low represents that bottom index of the list we are searching through
# high represents the top index (exclusize) we a searching through.

# Keep in mind what you did in problems 0 and 1
def fast_search_help(g, key, low, high, times_run):
    times_run += 1
    # Based on the parameters, when can you tell that you cannot find the key?

    # In the case that the key no longer fits into our list portion

    if g[low] > key or g[high] < key:
        return -1

    # If we're here, then there's still hope of finding the key
    # which index shall you check?

    # Guess that the key is at the middle of our current list portion
    guess = (len(g[low:high]) // 2)  # Guess at the half point

    # If the key is the middle, congrats! return the key of that guess in relation to the entire list
    if g[guess] == key:
        print(times_run, 'loops')
        return guess

    # But what if you didn't find key and it's less than your guess?
    # Then call the function again focusing on the lower part of portion of our half list this time
    elif guess > key:
        return fast_search_help(g, key, low, guess, times_run)

    # ok, but what if you didn't find key and it's more than your guess?
    # Focus on the upper portion of our half list this time
    elif guess < key:
        return fast_search_help(g, key, guess, high, times_run)


print(fast_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 3), "expt: 2")
print(fast_search(data, 12), "expt: unkwn")
