# Abir Taheer
# IntroCS pd1
# HW17 -- Letters & Numbers
# 2019-03-06


def gradeConv(g: int) -> str:
    """
    Convert a numerical grade into a letter grade
    :param g: A number between 0 and 100
    :type g: int
    :return: The letter value associated with the given grade
    :rtype: str

    >>> gradeConv(-12)
    'Z'

    >>> gradeConv(90)
    'A'

    >>> gradeConv(85)
    'B'

    >>> gradeConv(75)
    'C'

    >>> gradeConv(69)
    'D'

    >>> gradeConv(55)
    'F'

    >>> gradeConv(103)
    'Z'
    """

    # If statements testing to see if grade is inside of range and returning the appropriate letter
    if 100 >= g >= 90:
        return "A"
    elif 90 > g >= 80:
        return "B"
    elif 80 > g >= 70:
        return "C"
    elif 70 > g >= 65:
        return "D"
    elif 65 > g >= 0:
        return "F"

    # Exception case: Return 'Z'
    return "Z"

def passJudgement(letterGrade: str) -> str:
    """
    Return a quirky phrase based on the letter grade
    :param letterGrade: Any single letter grade
    :type letterGrade: str
    :return: A query phrase based on the letter grade
    :rtype: str

    >>> passJudgement("A")
    'Alrightyy'

    >>> passJudgement("B")
    'Could be better'

    >>> passJudgement("C")
    'sad reacc'

    >>> passJudgement('Z')
    'mega sad reacc'
    """
    if letterGrade == "A":
        return "Alrightyy"
    elif letterGrade == "B":
        return "Could be better"
    elif letterGrade == "C":
        return "sad reacc"
    return "mega sad reacc"

