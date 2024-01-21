"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
Hints: #92, # 110
"""

import unittest
from io import StringIO


# Time complexity: O(p + k^2), where p is the string's length and k is the number of sequences.
# Space complexity: O(p)
# def string_compression(string):
#     compressed_string = ""
#     count_consecutive = 0
#     for i in range(len(string)):
#         count_consecutive += 1
#
#         # If next character is different than current, append this char to result.
#         if i + 1 >= len(string) or string[i] != string[i + 1]:
#             compressed_string += string[i] + str(count_consecutive)
#             count_consecutive = 0
#
#     return min(compressed_string, string, key=len)


# Using join.
# Time complexity: O(p), where p is the string's length.
# Space complexity: O(p)
# def string_compression(string):
#     compressed_sequences = []
#     count_consecutive = 0
#     for i in range(len(string)):
#         count_consecutive += 1
#
#         # If next character is different than current, append this char to result.
#         if i + 1 >= len(string) or string[i] != string[i + 1]:
#             compressed_sequences.append(string[i] + str(count_consecutive))
#             count_consecutive = 0
#
#     return min(string, ''.join(compressed_sequences), key=len)


# Using join. Count compression beforehand.
# Time complexity: O(p), where p is the string's length.
# Space complexity: O(p)
# def string_compression(string):
#     final_length = count_compression(string)
#     if final_length >= len(string):
#         return string
#
#     compressed_sequences = []
#     count_consecutive = 0
#     for i in range(len(string)):
#         count_consecutive += 1
#
#         # If next character is different than current, append this char to result.
#         if i + 1 >= len(string) or string[i] != string[i + 1]:
#             compressed_sequences.append(string[i] + str(count_consecutive))
#             count_consecutive = 0
#
#     return ''.join(compressed_sequences)


# def count_compression(string):
#     final_length = 0
#     count_consecutive = 0
#
#     for i in range(len(string)):
#         count_consecutive += 1
#
#         # If next character is different than current, increment final length.
#         if i + 1 >= len(string) or string[i] != string[i + 1]:
#             final_length += 1 + len(str(count_consecutive))
#             count_consecutive = 0
#
#     return final_length


# Using StreamIO.
# https://waymoot.org/home/python_string/
# def string_compression(string):
#     final_length = count_compression(string)
#     if final_length >= len(string):
#         return string
#
#     file_compressed = StringIO()
#
#     count_consecutive = 0
#     for i in range(len(string)):
#         count_consecutive += 1
#
#         # If next character is different than current, append this char to result.
#         if i + 1 >= len(string) or string[i] != string[i + 1]:
#             file_compressed.write(string[i])
#             file_compressed.write(str(count_consecutive))
#             count_consecutive = 0
#
#     return file_compressed.getvalue()


# Using generators.
def string_compression(string):
    final_length = count_compression(string)
    if final_length >= len(string):
        return string

    file_compressed = StringIO()

    count_consecutive = 0
    for current_item, next_item in with_next(string):
        count_consecutive += 1

        # If next character is different than current, append this char to result.
        if current_item != next_item:
            file_compressed.write(current_item)
            file_compressed.write(str(count_consecutive))
            count_consecutive = 0

    # Add remaining item.
    file_compressed.write(next_item)
    file_compressed.write(str(count_consecutive + 1))

    return file_compressed.getvalue()


# Using generators.
def count_compression(string):
    final_length = 0
    count_consecutive = 0

    if string == "":
        return 0

    for current_item, next_item in with_next(string):
        count_consecutive += 1

        # If next character is different than current, increment final length.
        if current_item != next_item:
            final_length += 1 + len(str(count_consecutive))
            count_consecutive = 0

    # Add remaining item.
    final_length += 1 + len(str(count_consecutive))

    return final_length


def with_next(iterable):
    """Yield (current, next_item) tuples for each item in iterable."""
    iterator = iter(iterable)
    try:
        current_item = next(iterator)
    except StopIteration:
        return
    for next_item in iterator:
        yield current_item, next_item
        current_item = next_item


class Test(unittest.TestCase):
    """Test cases."""
    count_compression_data = [
        ("aabcccccaaad", 10),
        ("aabcccccaaa", 8),
        ("aabcc", 6),
        ("aab", 4),
        ("ab", 4),
        ("a", 2),
        ("", 0)
    ]

    data = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("aabcccccaaad", "a2b1c5a3d1"),
        ("aabcc", "aabcc")
    ]

    def test_count_compression(self):
        for string, final_length in self.count_compression_data:
            self.assertEqual(final_length, count_compression(string))

    def test_string_compression(self):
        for string, expected in self.data:
            self.assertEqual(expected, string_compression(string))


if __name__ == "__main__":
    unittest.main()