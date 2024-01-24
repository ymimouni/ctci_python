"""
Implement an algorithm to find the kth to last element of a singly linked list.
"""

import unittest
from ctci.ctci_library.assorted import ListNode


def kth_to_last(head: ListNode, k: int) -> int:
    first = head
    # Move first to kth position.
    while k > 0 and first is not None:
        first = first.next
        k -= 1

    if k > 0:
        return -1

    second = head
    # Move them at the same pace. When first hits the end, second would be at the right element.
    while first is not None:
        first, second = first.next, second.next

    return second.val


# Using recursivity.
class Index:
    value = 0


def kth_to_last(head: ListNode, k: int) -> int:
    idx = Index()
    return r_kth_to_last(head, k, idx)


def r_kth_to_last(head: ListNode, k: int, idx: Index) -> int:
    if head is None:
        return None
    val = r_kth_to_last(head.next, k, idx)
    idx.value += 1
    if idx.value == k:
        return head.val
    return val


class Test(unittest.TestCase):
    """Test cases."""
    data = [(ListNode(1, ListNode(4, ListNode(3, ListNode(5, ListNode(2, ListNode(3)))))), 3, 5),
            (ListNode(1, ListNode(4, ListNode(3, ListNode(5, ListNode(2, ListNode(3)))))), 1, 3),
            (ListNode(1, ListNode(4, ListNode(3, ListNode(5, ListNode(2, ListNode(3)))))), 7, None)]

    def test_kth_to_last(self):
        for node, k, expected in self.data:
            self.assertEqual(expected, kth_to_last(node, k))


if __name__ == "__main__":
    unittest.main()
