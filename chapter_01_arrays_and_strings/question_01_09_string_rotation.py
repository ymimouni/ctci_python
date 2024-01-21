"""
String Rotation: Assume you have a method isSubst ring which checks if one word is a substring
of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat").
Hints: #34, #88, #104
xyxy yxyx
"""

import unittest


def is_rotation(s1, s2):
    if len(s1) == len(s2):
        return s1 in s2 + s2

    return False


class Test(unittest.TestCase):
    """Test cases."""
    data = [
        ("waterbottle", "erbottlewat", True),
        ("paper", "apple", False),
        ("", "", True),
    ]

    def test_is_rotation(self):
        for s1, s2, expected in self.data:
            self.assertEqual(expected, is_rotation(s1, s2))


if __name__ == "__main__":
    unittest.main()
