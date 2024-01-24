"""
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
"""

import unittest
from ctci.ctci_library.assorted import ListNode


def partition(node: ListNode, x: int) -> ListNode:
    before_start, before_end = None, None
    after_start, after_end = None, None

    while node is not None:
        next = node.next
        node.next = None
        if node.val < x:
            if before_start is None:
                before_start = node
                before_end = node
            else:
                before_end.next = node
                before_end = before_end.next
        else:
            if after_start is None:
                after_start = node
                after_end = node
            else:
                after_end.next = node
                after_end = after_end.next
        node = next

    if before_start is None:
        return after_start

    before_end.next = after_start

    return before_start


# Relative order not respected.
def partition(node: ListNode, x: int) -> ListNode:
    head, tail = node, node

    while node is not None:
        next = node.next
        if node.val < x:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = next
    tail.next = None

    return head


class Test(unittest.TestCase):
    """Test cases."""
    data = [(ListNode(3, ListNode(5, ListNode(8, ListNode(5, ListNode(10, ListNode(2, ListNode(1))))))),
             ListNode(1, ListNode(2, ListNode(3, ListNode(5, ListNode(8, ListNode(5, ListNode(10))))))), 5)]

    def test_partition(self):
        for node, expected, x in self.data:
            self.assertEqual(expected.print_forward(), partition(node, x).print_forward())


if __name__ == "__main__":
    unittest.main()
