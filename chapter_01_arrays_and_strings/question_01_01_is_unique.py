"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional
data structures?
"""

import unittest


# def is_unique(input_string):
#     """"Determine if a string has all unique characters, using a set"""
#     char_set = set()
#     for char in input_string:
#         if char in char_set:
#             return False
#         char_set.add(char)
#     return True


# def is_unique(input_string):
#     """"Determine if a string has all unique characters, using a bit vector"""
#     if len(input_string) > 26:
#         return False
#
#     checker = 0
#     for char in input_string:
#         val = ord(char)
#         if checker & (1 << val) > 0:
#             return False
#         checker |= 1 << val
#     return True


def is_unique(input_string):
    """Assuming character set is ASCII (128 characters), determine if a string has all unique characters, using a
     character array"""
    if len(input_string) > 128:
        return False

    # https://stackoverflow.com/questions/3459098/create-list-of-single-item-repeated-n-times
    char_set = [False] * 128
    for char in input_string:
        index = ord(char)
        if char_set[index]:
            return False
        char_set[index] = True
    return True


# TODO: Determine if a string has all unique characters, you cannot use additional data structures. Careful, though:
# many sorting algorithms take up extra space


class Test(unittest.TestCase):
    wordsT = ["abcde", "kite", "padle"]
    wordsF = ["hello", "apple"]

    def test_is_unique(self):
        # true check
        for test_string in self.wordsT:
            self.assertTrue(is_unique(test_string))
        # false check
        for test_string in self.wordsF:
            self.assertFalse(is_unique(test_string))


if __name__ == "__main__":
    unittest.main()
