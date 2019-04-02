# Abir Taheer
# IntroCS pd1
# HW30 -- 000 000 111, v11
# 2019-03-25


def tablefyASCII():
    """
    :return: HTML code that generates a table containing all uppercase and lowercase letters alongside their ASCII code
    """
    letters = "abcdefghijklmnopqrstuvwxyz"
    html = "<table>\n\t<tr>\n\t\t<th>Letter</th>\n\t\t<th>ASCII Code</th>\n\t</tr>"
    upper = 65
    lower = 97
    for x in letters.upper():
        html += "\n\t<tr>\n\t\t<td>"+ x +"</td>\n\t\t<td>"+ pad(toBin(upper), 8) +"</td>\n\t</tr>"
        upper += 1
    for x in letters:
        html += "\n\t<tr>\n\t\t<td>" + x + "</td>\n\t\t<td>" + pad(toBin(lower), 8) + "</td>\n\t</tr>"
        lower += 1
    html += "\n</table>"
    return html


def pad(n: object, l: int) -> str:
    """
    :param n: integer or string to padd
    :param l: required min length of string
    :return: string padded with 0's at the beginning that meets a given minimum length

    >>> pad(4, 3)
    '004'

    >>> pad('23', 5)
    '00023'

    >>> pad(723, 2)
    '723'
    """
    n = str(n)
    while len(n) < l:
        n = "0" + n
    return n


def fortify(name: str) -> str:
    """
    :param name: name to fortify
    :return: fortified version of name

    >>> fortify("Abir Taheer")
    'Taheer, Abir Taheer'

    >>> fortify("James Bond")
    'Bond, James Bond'
    """
    found = False
    last = ""
    for x in name:
        if x == " ":
            found = True
        if found:
            last += x
    return last + ", " + name


# Convert To Base-2 (Binary) For Fun :)
def toBin(num: int) -> int:
    """
    :param num: number in base-10
    :return: base-2 encoded form of number

    >>> toBin(7)
    111

    >>> toBin(65)
    1000001

    >>> toBin(2)
    10
    """
    bin_txt = ""
    while num > 0:
        bin_txt = str(num % 2) + bin_txt
        num = (num - (num % 2)) // 2
    return int(bin_txt)

