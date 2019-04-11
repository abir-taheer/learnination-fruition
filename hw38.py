# Abir Taheer
# IntroCS pd1
# HW38 -- Stats on Stats on Stats
# 2019-04-10


# I made this in the previous hw, but looks like it came in handy now
# I am aware that this is pretty inefficient, but it gets the job done for as of right now
def bubble_sort(nums: list) -> list:

    # If we run into any conflicts, that means the list is not fully sorted and we need to check one more time
    conflict = True
    while conflict:

        # Assume no conflicts to begin with
        conflict = False

        # Check to make sure every element is in order and set conflict to true in case of a conflict
        for x in range(len(nums) - 1):
            if nums[x] > nums[x + 1]:
                conflict = True
                nums[x], nums[x + 1] = nums[x + 1], nums[x]

    # The list will have been sorted at this point so return the list
    return nums


# A "who cares about memory" based approach using the bucket stuff
def bucket_sort(nums: list) -> list:
    # Make a bucket that goes up to the largest int
    bucket = [0 for x in range(max(nums) + 1)]
    sorted_list = []

    # Add frequencies for each item in the bucket
    for x in nums: bucket[x] += 1

    # For each item in the bucket, append it to the sorted list for the same number of times as its frequency
    for x in range(len(bucket)): sorted_list.extend([x for y in range(bucket[x])])
    return sorted_list


def med_list(nums: list) -> float:
    """
    returns the median of the numeric elements in list nums.
    :param nums: list of integers
    :return: the median of the list

    >>> med_list([1,2,3])
    2

    >>> med_list([2,3,4,5,6,3])
    3.5

    >>> med_list([9,2,1,4])
    3
    """
    # Sort the list
    nums = bucket_sort(nums)

    # Find the middle
    middle = len(nums) // 2

    # Return the average of the two numbers at the middle if even number of items
    # Else return the middle item
    return nums[middle + 1] if len(nums) % 2 == 1 else (nums[middle] + nums[middle + 1]) / 2


def vertbargraphify(nums):
    """
    takes a list of non-negative integers and prints a set of vertical bars visualizing the magnitude of the value at each index.
    :param nums: list of values to plot for bar graph

    >>> vertbargraphify([0, 1, 2, 3])
           *
         * *
       * * *
     0 1 2 3
    """
    # Check from the highest value in the bar graph to the lowest
    top_to_bottom = [x for x in range(max(nums))]
    top_to_bottom.reverse()

    # Create a list with the labels to be printed later
    labels = [str(x) for x in range(len(nums))]

    # For each frequency from top to bottom, check if the frequency of the current item in the list falls
    # Inside of the current one being tried
    # Add an x if it does, and a space if it doesn't
    for x in top_to_bottom:
        current_line = ""
        for y in nums:
            current_line += " x" if y > x else "  "
        print(current_line)
    print(" " + " ".join(labels))
