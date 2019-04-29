# Team Spring Blossoms
# Asma Berri & Abir Taheer
# IntroCS pd1
# HW43 -- But What Will We Do When Not Sleeping?
# 2019-04-24


# --------------------- Problem 8 ----------------------
def product(L: list) -> int:
    """
    A function that return the product of the items in a list
    :param L: A numerical list
    :return: The product of all of the items

    >>> product([1,2,3])
    6

    >>> product([3,7,2,2])
    84

    >>> product([])
    0

    >>> product([0])
    0
    """

    # Create a variable to store the complete product
    # If we receive an empty set the starting value of the variable to 0
    # Otherwise, set it to 1 because of the multiplication property of 1
    multiple = 1 if len(L) > 0 else 0

    # For each item in the list, set the value of multiple to itself multiplied by the current item in the list
    for x in L:
        multiple *= x

    # Return the value of multiple
    return multiple


# Create a variable to store the number that was given in the problem
num_given = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420


def find_largest_product(num: int, len_series: int) -> int:
    """
    Function that finds the largest product in number of len_series consecutive integers
    :param num: The number to search
    :param len_series: The number of consecutive integers to check at a time
    :return: The largest product of len_series consecutive integers in the number

    This example case was given in the problem itself
    >>> find_largest_product(num_given, 4)
    5832
    """

    # Break the number up into a list of each of its integers
    separated_nums = [int(x) for x in str(num)]

    # Create a variable to store the largest product
    largest_product = 0

    # Check len_series numbers at a time
    for x in range(len(separated_nums) - len_series):

        # Find the product of the current len_series numbers that we're checking
        prod = product(separated_nums[x: x + len_series])

        # If the product is greater than the previously largest recorded product, set it as the largest_product
        if prod > largest_product:
            largest_product = prod

    # Return the value of largest_product
    return largest_product


# We contacted another thinker, Amelia, who also did this problem
# And we verified that she got the same answer as us
print(find_largest_product(num_given, 13))


# --------------------- Problem 22 ---------------------

# Get the file with the names
names = open("p022_names.txt", "r").read()

# Split all of the names by commas
names = names.split(",")

# Remove the two quotes at the beginning and end of the names
names = [x[1:-1] for x in names]


def calc_name_points(name: str) -> int:
    """
    Calculates the number of points a name has based on the sum of the differences of the letters' ascii value and 64
    :param name: A single name as a string
    :return: The points value of a name

    >>> calc_name_points("COLIN")
    53
    """
    # Make a variable to count the points
    points = 0

    # Iterate through each letter of the name
    for x in name.upper():

        # Add the points value of that letter to the points variable
        points += (ord(x) - 64)

    # Return the total number of points
    return points


def get_total_points(list_names: list) -> int:
    # The challenge requires that the names are in alphabetical order
    list_names.sort()

    # Initialize a variable to store all of the points from the entire list
    sum_points = 0

    # Iterate through each of the names
    for x in range(len(list_names)):
        # Increment sum points by the points for each name multiplied by its position
        sum_points += (x + 1) * calc_name_points(list_names[x])

    # Return the total points
    return sum_points


print(get_total_points(names))


# --------------------- Problem 4 ----------------------
def check_Pal(product):
    """
    A function that checks if a value is a palindrome.
    >>> check_Pal(505)
    True

    >>> check_Pal(70700)
    False

    >>> check_Pal(700000000071)
    False

    >>> check_Pal(4343434)
    True
    """
    return str(product) == (str(product)[::-1])
    # check if the forward reading of the product is the same as the backward reading


def palindrome3():
    """
    A function that finds the largest palindrome made from the product of two
    3-digit numbers..

    >>> palindrome3()
    906609 = 913 x 993
    """
    # current maximum palindrome
    max_pal = 0

    # the factors that result in the above product
    factor1 = 0
    factor2 = 0

    # for every value from 999 through 100 (inclusive) and...
    for x in range(999, 99, -1):

        # for every value from 999 through x+1 (inclusive)
        for y in range(999, x, -1):

            # store the product as x times y
            product = x * y

            # check if the product is a palindrome and
            # check if the product is greater than the prev largest palindrome
            if check_Pal(product) and product > max_pal:
                # store the current maximum palindrome as this product
                max_pal = product

                # store the factors as x and y
                factor1 = x
                factor2 = y

    # print the maximum palindrome found in the following format
    print(max_pal, '=', factor1, 'x', factor2)
