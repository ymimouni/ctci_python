"""
One Away: There are three types of edits that can be performed on strings: insert a character, remove a character,
or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales. pale -> true
pale. bale -> true
pale. bake -> false
Hints: #23, #97, #130
"""

import unittest


# Time complexity: O(n).
# Space complexity: O(1).
def one_edit_away(first, second):
    if len(first) == len(second):
        return one_replace_away(first, second)
    elif len(first) == len(second) + 1:
        return one_insert_away(second, first)
    elif len(first) == len(second) - 1:
        return one_insert_away(first, second)
    else:
        return False


def one_insert_away(s1, s2):
    i = 0
    j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if i != j:
                return False
            j += 1
        else:
            i += 1
            j += 1

    return True


def one_replace_away(s1, s2):
    found_difference = 0

    i = 0
    while i < len(s1):
        if s1[i] != s2[i]:
            if found_difference:
                return False
            found_difference = True
        i += 1

    return True


# In one single pass
def one_edit_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False

    first = s1 if len(s1) > len(s2) else s2
    second = s2 if len(s1) > len(s2) else s1

    found_difference = False
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if s1[i] != s2[j]:
            # Ensure that this is the first difference found.
            if found_difference:
                return False
            found_difference = True
            if len(first) == len(second):
                # On replace, move shorter pointer.
                j += 1
        else:
            # If matching, move shorter pointer.
            j += 1
        # Always move longer pointer.
        i += 1

    return True


class Test(unittest.TestCase):
    """Test cases."""
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('a', 'b', True),
        ('', 'd', True)
    ]

    def test_one_edit_away(self):
        for first, second, expected in self.data:
            self.assertEqual(one_edit_away(first, second), expected)


if __name__ == "__main__":
    unittest.main()
