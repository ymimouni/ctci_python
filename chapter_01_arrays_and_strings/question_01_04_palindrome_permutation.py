"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome
is a word or phrase that is the same forwards and backwards. A permutation is a rea rrangement of letters. The
palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat". "atco cta". etc.)
Hints: #106, #121, #134, #136
"""

import unittest


# Time complexity: O(n)
# Space complexity: O(n)
def is_permutation_of_palindrome(phrase):
    s = set()
    for char in phrase.lower():
        if char != " ":
            if char in s:
                s.remove(char)
            else:
                s.add(char)

    return len(s) <= 1


# Time complexity: O(n)
# Space complexity: O(1)
def is_permutation_of_palindrome(phrase):  # noqa
    """Using a bit vector"""
    checker, count_odd = 0, 0

    for char in phrase.lower():
        if char != " ":
            val = ord(char)
            if checker & 1 << val:
                checker &= ~(1 << val)
                count_odd -= 1
            else:
                checker |= 1 << val
                count_odd += 1

    return count_odd <= 1


# Time complexity: O(n)
# Space complexity: O(1)
def is_permutation_of_palindrome(phrase):  # noqa
    """With better code organization."""

    bit_vector = create_bit_vector(phrase.lower())
    return check_at_most_one_bit_set(bit_vector)


def create_bit_vector(phrase):
    """Create a bit vector for a string. For each char with value i, toggle the ith bit"""
    bit_vector = 0

    for char in phrase:
        x = get_char_number(char)
        bit_vector = toggle(bit_vector, x)

    return bit_vector


def get_char_number(char):
    if char != " ":
        return ord(char) - ord("a")

    return -1


def toggle(bit_vector, index):
    if index < 0:
        return bit_vector

    mask = 1 << index
    if bit_vector & mask:
        bit_vector &= ~mask
    else:
        bit_vector |= mask

    return bit_vector


def check_at_most_one_bit_set(bit_vector):
    bits_set = 0

    for char in bin(bit_vector):
        if char == "1":
            bits_set += 1
            if bits_set > 1:
                return False

    return True


class Test(unittest.TestCase):
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_is_permutation_of_palindrome(self):
        for phrase, expected in self.data:
            self.assertEqual(is_permutation_of_palindrome(phrase), expected)


if __name__ == "__main__":
    unittest.main()
