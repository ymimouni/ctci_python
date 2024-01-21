"""
URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string has sufficient space
at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If
implementing in Java, please use a character array so that you can perform this operation in place.)
EXAMPLE
Input: "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"
Hints: #53, #118
"""

import unittest
import itertools


def reverse_enumerate(sequence):
    """Generates a reverse indexed sequence."""
    i = len(sequence)
    while i >= 0:
        yield i - 1, sequence[i - 1]
        i -= 1


def find_last_character(char_list):
    i = len(char_list) - 1
    while i > 0:
        if char_list[i] != " ":
            return i + 1
        i -= 1
    return -1


def find_last_character(char_list):
    """Using reverse_enumerate."""
    for index, char in reverse_enumerate(char_list):
        if char != " ":
            return index + 1
    return -1


def replace_spaces(char_list, true_length):
    space_count = 0

    for char in itertools.islice(char_list, true_length):
        if char == " ":
            space_count += 1

    index = true_length + space_count * 2 - 1
    i = true_length - 1
    while i > 0:
        if char_list[i] != " ":
            char_list[index] = char_list[i]
            index -= 1
        else:
            char_list[index - 2: index + 1] = "%20"
            index -= 3
        i -= 1

    return char_list


class Test(unittest.TestCase):
    string = "Mr John Smith    "
    char_list = list(string)
    true_length = find_last_character(char_list)

    def test_replace_spaces(self):
        self.assertEqual(''.join(replace_spaces(self.char_list, self.true_length)), "Mr%20John%20Smith")


if __name__ == "__main__":
    unittest.main()
