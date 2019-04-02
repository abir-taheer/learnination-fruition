# Team Bet, Thanks A Lot
# Abir Taheer, Shah Wafi, Alex Tang
# IntroCS pd1
# HW31 -- Cereal-Grade Encryption
# 2019-03-28

alphabet = "abcdefghijklmnopqrstuvwxyz"


def rot_char(c, shft):
    """
    A helper function that encodes a character by allowing you to set the character rotational offset to any number
    :param c: The character to encode
    :param shft: How much to offset the encoded character
    :return: The encoded version of the original character with the offset specified
    """
    letters = alphabet
    if c.upper() == c:
        letters = alphabet.upper()
    return letters[(letters.find(c) + shft) % 26]


def decodeChar(char, rot):
    """
    Decode a character encoded using a rotary cipher
    :param char: the character to decoded
    :param rot: the rotation offset for the cipher
    :return: the decoded character
    """
    alpha_case = alphabet.upper() if alphabet.find(char[0]) == -1 else alphabet
    return alpha_case[(alpha_case.find(char[0]) - rot + len(alpha_case)) % len(alpha_case)]


def decodeWord(word, rot):
    """
    Decodes a word encoded using a rotary cipher
    :param word: The encoded word to decode
    :param rot: The rotational offset for the cipher
    :return: The decoded word
    """
    decoded = ""
    for x in word:
        decoded += decodeChar(x, rot)
    return decoded


def rot13_char(ch):
    """
    Encodes a character using 13 as a rotational offset
    :param ch: character to encode
    :return: encoded character
    """
    return rot_char(ch, 13)


def print_em_all() -> str:
    """
    Print all characters from A-Z as well as their encoded version
    """
    for x in alphabet.upper() + alphabet:
        print(x + "<->" + rot13_char(x))


def rot13_word(word):
    """
    Encode a word in the rotary 13 cipher
    :param word: The word to be encoded
    :return: The rotary 13 encrypted version of the word
    """
    encoded = ""
    for x in word:
        encoded += rot13_char(x)
    return encoded
