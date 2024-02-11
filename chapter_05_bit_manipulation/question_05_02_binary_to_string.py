"""
Binary to string.
"""

import unittest


# def binary_to_string(num) -> str:
#     if num <= 0 or num >= 1:
#         return "ERROR"
#
#     binary = ["0", "."]
#     while num > 0:
#         # Set a limit on length: 32 characters.
#         if len(binary) > 32:
#             return "ERROR"
#
#         r = num * 2
#         if r >= 1:
#             binary.append("1")
#             num = r - 1
#         else:
#             binary.append("0")
#             num = r
#
#     return "".join(binary)


def binary_to_string(num) -> str:
    if num <= 0 or num >= 1:
        return "ERROR"

    binary = ["0", "."]
    frac = 0.5
    while num > 0:
        # Set a limit on length: 32 characters.
        if len(binary) > 32:
            return "ERROR"

        if num >= frac:
            binary.append("1")
            num -= frac
        else:
            binary.append("0")
        frac /= 2

    return "".join(binary)


class Test(unittest.TestCase):
    """Test cases."""
    def test_binary_to_string(self):
        self.assertEqual(binary_to_string(0.625), "0.101")
        self.assertEqual(binary_to_string(0.3), "ERROR")


if __name__ == "__main__":
    unittest.main()
