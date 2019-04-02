# Abir Taheer
# IntroCS pd1
# HW15 -- Visiting Old Friends
# 2018-02-28

from math import pi


def areaCirc(r):
    """takes numeric input r and returns the area of a circle of radius r.
        :param r: The radius of circle
        :type r: int
        :return The area of the circle
        :rtype float
    """
    return pi * (r ** 2)


def areaWasher(radInner, radOuter):
    """takes numeric inputs radOuter, radInner and returns the area of a washer with inner radius radInner and outer radius radOuter.
        :param radOuter: The radius of the entire washer
        :param radInner: The radius of the hole in the middle of the washer
        :type radOuter: int
        :type radInner: int
        :returns: The area of the washer
        :rtype: float

    """
    return areaCirc(radOuter) - areaCirc(radInner)


def sumOfSquares(a, b):
    """takes numeric inputs a, b and returns the sum of their squares.
        :param a: first number to square
        :param b: second number to square
        :type a: int
        :type b: int
        :returns: The sum of the squares
        :rtype: int
    """
    return (a ** 2) + (b ** 2)


print("areaCirc Tests!!!")
print(str(areaCirc(1)) + " Expected: 3.14159265359")
print(str(areaCirc(3)) + " Expected: 28.2743338823")
print(str(areaCirc(5)) + " Expected: 78.5398163397")

print("\nareaWasher Tests!!!")
print(str(areaWasher(0, 2)) + " Expected: 12.5663706144")
print(str(areaWasher(3, 5)) + " Expected: 50.2654824574")
print(str(areaWasher(6, 10)) + " Expected: 201.06192983")

print("\nsumOfSquares Tests!!!")
print(str(sumOfSquares(0, 0)) + " Expected: 0")
print(str(sumOfSquares(1, 2)) + " Expected: 5")
print(str(sumOfSquares(4, 5)) + " Expected: 41")

# Test Results
# areaCirc Tests!!!
# 3.141592653589793 Expected: 3.14159265359
# 28.274333882308138 Expected: 28.2743338823
# 78.53981633974483 Expected: 78.5398163397
#
# areaWasher Tests!!!
# 12.566370614359172 Expected: 12.5663706144
# 50.26548245743669 Expected: 50.2654824574
# 201.06192982974676 Expected: 201.06192983
#
# sumOfSquares Tests!!!
# 0 Expected: 0
# 5 Expected: 5
# 41 Expected: 41
