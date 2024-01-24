"""
Implement a function to check if a linked list is a palindrome.
3->5->8->5->8->5->3
"""

import unittest
from ctci.ctci_library.assorted import ListNode
from collections import deque


# def is_palindrome(i_list: ListNode) -> bool:
#     reversed_list = reverse_and_clone(i_list)
#     return is_equal(i_list, reversed_list)
#
#
# def reverse_and_clone(node: ListNode) -> ListNode:
#     head = None
#     while node is not None:
#         n = ListNode(node.val)
#         n.next = head
#         head = n
#         node = node.next
#     return head
#
#
# def is_equal(one: ListNode, two: ListNode) -> bool:
#     while one is not None and two is not None:
#         if one.val != two.val:
#             return False
#         one, two = one.next, two.next
#     return one is None and two is None


# Using a stack.
# def is_palindrome(head: ListNode) -> bool:
#     slow = fast = head
#     d = deque()
#
#     while fast is not None and fast.next is not None:
#         d.append(slow.val)
#         slow, fast = slow.next, fast.next.next
#
#     # Has odd number of elements, so skip the middle.
#     if fast is not None:
#         slow = slow.next
#
#     while slow is not None:
#         if slow.val != d.pop():
#             return False
#         slow = slow.next
#
#     return True


# Using recursivity.
class Result:
    def __init__(self, node: ListNode or None, result: bool):
        self.node = node
        self.result = result


def is_palindrome(head: ListNode) -> bool:
    length = length_of_list(head)
    p = is_palindrome_recurse(head, length)
    return p.result


def is_palindrome_recurse(head: ListNode or None, length: int) -> Result or None:
    if head is None or length <= 0:
        return Result(head, True)
    elif length == 1:
        return Result(head.next, True)

    # Recurse on sublist.
    res = is_palindrome_recurse(head.next, length - 2)

    if res is None or not res.result:
        return res

    res.result = (head.val == res.node.val)
    res.node = res.node.next

    return res


def length_of_list(i_list: ListNode) -> int:
    if i_list is None:
        return 0

    return 1 + length_of_list(i_list.next)


class Test(unittest.TestCase):
    """Test cases."""
    data = [(ListNode(3, ListNode(5, ListNode(8, ListNode(5, ListNode(8, ListNode(5, ListNode(3))))))), True),
            (ListNode(3, ListNode(5, ListNode(8, ListNode(5, ListNode(8, ListNode(2, ListNode(3))))))), False),
            (ListNode(3, ListNode(5, ListNode(8, ListNode(8, ListNode(5, ListNode(3)))))), True)]

    def test_is_palindrome(self):
        for i_list, expected in self.data:
            self.assertEqual(expected, is_palindrome(i_list))


if __name__ == "__main__":
    unittest.main()
