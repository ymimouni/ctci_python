"""
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node,
not necessarily the exact middle) of a singly linked list, given only access to that node.
"""

import unittest
from ctci.ctci_library.assorted import ListNode


def delete_node(node: ListNode) -> bool:
    if node is None or node.next is None:
        return False

    node.val = node.next.val
    node.next = node.next.next
    return True


class Test(unittest.TestCase):
    """Test cases."""
    data = [(ListNode(1, ListNode(4, ListNode(3, ListNode(5, ListNode(2, ListNode(3)))))),
             ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(3))))))]

    def test_delete_node(self):
        for node, expected in self.data:
            delete_node(node.next.next.next)
            self.assertEqual(expected.print_forward(), node.print_forward())


if __name__ == "__main__":
    unittest.main()
