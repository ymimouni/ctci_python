"""
Intersection.
"""

import unittest
from ctci.ctci_library.assorted import ListNode


# Using a set.
# def intersection(list1: ListNode, list2: ListNode) -> ListNode:
#     s = set()
#     while list1 is not None:
#         s.add(list1)
#         list1 = list1.next
#
#     while list2 is not None:
#         if list2 in s:
#             return list2
#         list2 = list2.next


# Using a recursive approach.
class Result:
    def __init__(self, tail: ListNode, size: int):
        self.tail = tail
        self.size = size


def get_tail_and_size(head: ListNode) -> Result or None:
    if head is None:
        return None

    size, current = 1, head
    while current.next is not None:
        size += 1
        current = current.next

    return Result(current, size)


def get_kth_node(head: ListNode, k: int) -> ListNode:
    current = head
    while k > 0 and current is not None:
        current = current.next
        k -= 1

    return current


def find_intersection(list1: ListNode, list2: ListNode) -> ListNode or None:
    if list1 is None or list2 is None:
        return None

    # Get tails and sizes.
    result1 = get_tail_and_size(list1)
    result2 = get_tail_and_size(list2)

    if result1.tail is not result2.tail:
        return None

    shorter = list1 if result1.size < result2.size else list2
    longer = list2 if result1.size < result2.size else list1

    # Advance the pointer for the longer list by the difference in lengths.
    longer = get_kth_node(longer, abs(result1.size - result2.size))

    # Move both pointer until collision.
    while shorter is not longer:
        shorter, longer = shorter.next, longer.next

    # Return either one.
    return shorter


class Test(unittest.TestCase):
    """Test cases."""
    intersection = ListNode(5, ListNode(8, ListNode(5, ListNode(3))))
    data = [(ListNode(3, ListNode(5, ListNode(8, intersection))),
             ListNode(5, ListNode(7, intersection)), intersection)]

    def test_is_palindrome(self):
        for list1, list2, expected in self.data:
            self.assertEqual(expected.print_forward(), find_intersection(list1, list2).print_forward())


if __name__ == "__main__":
    unittest.main()
