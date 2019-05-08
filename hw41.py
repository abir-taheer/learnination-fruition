#Clyde "Thluffy" Sinclair
#StuyCS -- Spring 2019 IntroCS

import random

def rand_list(n, limit):
        """	return a list of n random integers on range [0,limit) """
        g = []
        while (n > 0):
                g.append(random.randrange(limit))
                n-= 1
        return g


#==================================================
# Problem 0

# data is a sorted list of 1000 random integers.
data = sorted(rand_list(1000, 1000))
print(data)
# i) Where in the list would you find the value 673 (it may or may not be in the list)?
#==============
# < < < Your brilliant answer here... > > >
#==============

# ii) Where in the list would you find the value 429 (it may or may not be in the list)?
#==============
# < < < Your brilliant answer here... > > >
#==============

# End Problem 0
#==================================================


#==================================================
# Problem 1

# i) Find the middle index of data (the index that splits a into 2 half sections).
#    use len(data) and any arithmetic operators
#==============
# < < < Your brilliant answer here... > > >
#==============

# ii) Find the index of data that splits it into two sections, the first with 1/4th of the values
#     the other with 3/4th of the values
#==============
# < < < Your brilliant answer here... > > >
#==============

# iii) Find the index of data that splits it into two sections, the first with 3/4th of the values
#       the other with 3/4th of the values
#==============
# < < < Your brilliant answer here... > > >
#==============

# iii) Find the index of data that splits it into two sections, the first with 7/8th of the values
#       the other with 1/8th of the values
#==============
# < < < Your brilliant answer here... > > >
#==============


# End Problem 1
#==================================================


#==================================================
# Problem 2

# Slow search: Write a function that searches for a value in a list.
# It should return the index of the value, or -1.
# This function should just look through each element to find the key,
# don't do anything clever.
# It should also print out the total number of loops it took to complete
def slow_search(g, key):
        i = 0
        count = 0 #loop counts
    #==============
    # <<<YOUR BRILLIANT CODE HERE>>>
    #==============
        return -1

#print(slow_search(a, 673))

# End Problem 2
#==================================================


#==================================================
# Problem 3

# What do you know about your data? Are there aspects of the data that will allow you to implement a significantly faster search algorithm? If so, what are they?

#==============
# < < < Your brilliant answer here... > > >
#==============

# Usually, you want a search function to only need 2 parameters:
# the list and the element you seek (key). 
# Hence the wrapper function, fast_search, taking only 2 parameters.
# Our fast search needs more information,
# so its helper function will incorporate this extra info:
def fast_search(g, key):
        return fast_search_help(g, key, 0, len(g))


# Here is our fast search. We are looking for key in g.
# low represents that bottom index of the list we are searching through
# high represents the top index (exclusize) we a searching through.

# Keep in mind what you did in problems 0 and 1
'''
def fast_search_help(g, key, low, high):

    # Based on the parameters, when can you tell that you cannot find the key?
    if ( <<<YOUR BRILLIANT CODE HERE>>> ):
        return -1

    # If we're here, then there's still hope of finding the key
    # which index shall you check?
    guess = (<<<YOUR BRILLIANT CODE HERE>>>)
    if ( guess == key ):
       return guess

    # But what if you didn't find key and it's less than your guess?
    elif ( guess > key ):
        return fast_search_help( <<<YOUR BRILLIANT CODE HERE>>> )

    # ok, but what if you didn't find key and it's more than your guess?
    elif ( guess < key ):
        return fast_search_help( <<<YOUR BRILLIANT CODE HERE>>> )

'''

# Challenge!
# Modify fast_search so that it prints out the number of times fast_search_help was run!
