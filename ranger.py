# Specifying a default value in the function definition suppresses an exception
# If the parameter is not given on function call


def ranger( beginning , end = None , step = 1):
    """
    A reconstruction of the range function
    :param beginning: The integer from which to start, inclusive
    :param end: The integer at which to stop, exclusive
    :param step: The amount to increment the beginning value by
    :return: a list containing all of the values in between the beginning and the end value while incremented by the value of step
    """

    # Do the following if only one parameter is provided
    if end is None:

        # Replace the end parameter with the value received for beginning
        end = beginning

        # Set the beginning value equal to 0
        beginning = 0

    # Initialize our response as a list
    numbers = []

    # Perform the following for as long as beginning is less than or equal to the end
    # This means that if the original value of end is less
    # The value of beginning than the r an empty list will be returned
    while beginning < end:

        # Add each number to the list
        numbers.append(beginning)

        # Increment the beginning value by the value of step
        beginning += step

    # Once we've reached the point where the beginning value is equal to or greater than the end
    # Return the list we initialized in the numbers variable
    return numbers


# Example use case
for x in ranger(3):
    """
    Expected:
    0
    1
    2
    """
    print(x)

for x in ranger(-2, -1):
    """
    Expected:
    -2
    """
    print(x)

for x in ranger(-2, 5, 2):
    """
    Expected:
    -2
    0
    2
    4
    """
    print(x)
