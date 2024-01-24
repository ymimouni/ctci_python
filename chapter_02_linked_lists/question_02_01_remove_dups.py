"""
Remove Dups: Write code to remove duplicates from an unsorted linked list.
Hints: #9, #40
"""

import unittest
from ctci.ctci_library.assorted import ListNode


def delete_dups(n: ListNode) -> None:
    s = set()

    while n is not None:
        if n.val in s:
            prev.next = n.next
        else:
            s.add(n.val)
            prev = n
        n = n.next


# Without extra space.
def delete_dups(head: ListNode) -> None:
    current = head
    while current is not None:
        runner = current
        while runner.next is not None:
            if current.val == runner.next.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next


class Test(unittest.TestCase):
    """Test cases."""
    data = [
        (ListNode(1, ListNode(4, ListNode(3, ListNode(5, ListNode(2, ListNode(3)))))),
         ListNode(1, ListNode(4, ListNode(3, ListNode(5, ListNode(2))))))
    ]

    def test_delete_dups(self):
        for node, expected in self.data:
            delete_dups(node)
            self.assertEqual(expected.print_forward(), node.print_forward())
        return True


if __name__ == "__main__":
    unittest.main()
