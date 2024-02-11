"""
Flip bit to win.
"""

import unittest


def logical_right_shift(n: int) -> int:
    # Assumes that n can be written in 64 bits.
    return (n % 0x100000000) >> 1


def flip_bit(n: int) -> int:
    if ~n == 0:
        return 32

    current_length = 0
    previous_length = 0
    max_length = 1  # We can always have a sequennce of at least 1.

    while n:
        if n & 1:
            current_length += 1
        else:
            previous_length = current_length if n & 2 else 0
            current_length = 0
        max_length = max(current_length + previous_length + 1, max_length)
        n = logical_right_shift(n)

    return max_length


class Test(unittest.TestCase):
    """Test cases."""
    def test_flip_bit(self):
        self.assertEqual(flip_bit(-1), 32)
        self.assertEqual(flip_bit(-10), 31)
        self.assertEqual(flip_bit(0), 1)
        self.assertEqual(flip_bit(15), 5)


if __name__ == "__main__":
    unittest.main()
