# Abir Taheer
# IntroCS pd1
# HW33 -- Anslatingtray Englishway intoway Igpay Atinlay
# 2019-03-28


"""
PIG LATIN RULES:

1. Take the first part of a word that isn't followed by a vowel and place it after the remaining part followed by "ay"
2. If the part preceeding the "ay" is a vowel, replace the "a" with the vowel
3. Punctuation goes at the end


OUTLINE:

First we need to figure out all of the quirks of the pig latin language as well as certain exception cases.
Then we make a rudimentary version of our pig latin function based only on the root principles and test it out.
Any time we run into an exception case, document it and find a solution.
End development once the function handles all tests without error

DEVELOPMENT PLAN:

* Will just split up a phrase into it's words
* Find the first vowel in the word
* Move all parts before and including the vowel after the rest of the word
* Add the "ay" ending to the new word part


DEVELOPMENT LOG:

2019-04-01 7:32
Abir: Figured out how Pig Latin works

2019-04-01 7:39
Abir: Finished rudimentary version of pig latin translator

2019-04-01 7:46
Abir: Diagnosed issue with pope example not passing doctest because of misplaced h

2019-04-01 7:55
Abir: Found issue with punctuation, brought in replace function to fix issues with punctuation

"""


vowels = "aeiou";


def isVowel(l):
    return vowels.find(l.lower()) != -1


def findVowel(word):
    for x, y in enumerate(word):
        if isVowel(y):
            return x
    return -1


def replace(s: str, q: str, r: str) -> str:
    """
    :param s: The original string
    :param q: The string  to match in the original string
    :param r: The string to replace the match with
    :return: The new string with the replacement in place

    >>> replace("hello from the other side", "other", "banana")
    'hello from the banana side'

    >>> replace("Winter is coming", "Winter", "Spring")
    'Spring is coming'

    >>> replace("Dolphins run this planet", "dolphins", "mice")
    'Dolphins run this planet'
    """
    loc = s.find(q)
    if loc == -1:
        return s
    beginning = s[:loc]
    end = s[loc + len(q):]
    return beginning + r + end


def movePuntToEnd(phr):
    punctuation = ["?", ".", "!"]
    for x in punctuation:
        if phr.find(x) != -1:
            return replace(phr, x, "") + x
    return phr


def useWay(word):
    if isVowel(word[-1]) or word[-1] == "f":
        return True
    return False


def translate(phrase: str) -> str:
    """
    Returns the pig latin equivalent of a phrase
    :param phrase: Phrase in english, words separated by phrases
    :return: Pig Latin equivalent of phrase

    >>> translate('What are the rules of Pig Latin?')
    'Atwhay areway ethay ulesray ofway Igpay Atinlay?'

    >>> translate('the pope rocks red kicks')
    'ethay opepay ocksray edray ickskay'

    """

    # Init a variable to store the translated phrase
    translated = []

    for x in phrase.split(" "):
        y = x.lower()
        beginning = findVowel(y) if findVowel(y) != -1 else 0
        beg = y[beginning:] if y[0] == x[0] else y[beginning:].capitalize()
        end = "way" if useWay(beg + y[:beginning]) else "ay"
        translated.append(beg + y[:beginning] + end)
    return movePuntToEnd(" ".join(translated))
