"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
"""

import unittest
from collections import Counter


def check_permutation(s, t):
    if len(s) != len(t):
        return False

    d = {}

    for char in s:
        d[char] = d.get(char, 0) + 1

    for char in t:
        d[char] = d.get(char, 0) - 1
        if d[char] < 0:
            return False

    return True


def check_permutation(s, t):
    """Using Counter"""
    if len(s) != len(t):
        return False

    counter = Counter(s)

    for char in t:
        if counter[char] == 0:
            return False
        counter[char] -= 1

    return True


class Test(unittest.TestCase):
    pairsT = (
        ("apple", "papel"),
        ("carrot", "tarroc")
    )
    pairsF = (
        ("hello", "llloh"),
    )

    def test_is_unique(self):
        # true check
        for pair in self.pairsT:
            self.assertTrue(check_permutation(*pair))
        # false check
        for pair in self.pairsF:
            self.assertFalse(check_permutation(*pair))


if __name__ == "__main__":
    unittest.main()