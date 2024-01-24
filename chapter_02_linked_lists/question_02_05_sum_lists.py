"""
Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
"""

import unittest
from ctci.ctci_library.assorted import ListNode


# Iterative.
# def add_lists(l1: ListNode, l2: ListNode) -> ListNode:
#
#     carry = 0
#     result = None
#
#     while l1 is not None or l2 is not None or carry > 0:
#         value = carry
#         if l1 is not None:
#             value += l1.val
#             l1 = l1.next
#         if l2 is not None:
#             value += l2.val
#             l2 = l2.next
#         node = ListNode(value % 10)
#         if result is None:
#             result = node
#             tail = result
#         else:
#             tail.next = node
#             tail = node
#         carry = 1 if value >= 10 else 0
#
#     return result


# # Recursive.
# def add_lists(l1: ListNode, l2: ListNode) -> ListNode:
#     return r_add_lists(l1, l2, 0)
#
#
# def r_add_lists(l1: ListNode or None, l2: ListNode or None, carry: int) -> ListNode or None:
#     if l1 is None and l2 is None and carry == 0:
#         return None
#
#     value = carry
#     if l1 is not None:
#         value += l1.val
#     if l2 is not None:
#         value += l2.val
#     result = ListNode(value % 10)
#     if l1 is not None or l2 is not None:
#         more = r_add_lists(None if l1 is None else l1.next,
#                            None if l1 is None else l2.next,
#                            1 if value >= 10 else 0)
#         result.next = more
#
#     return result


# Follow up.
class PartialSum:

    def __init__(self, sum_node=None, carry=0):
        self.sum_node = sum_node
        self.carry = carry


def add_lists(l1: ListNode, l2: ListNode) -> ListNode:
    # Get length of l1 and l2.
    len1 = length(l1)
    len2 = length(l2)

    if len1 < len2:
        l1 = pad_list(l1, len2 - len1)
    else:
        l2 = pad_list(l2, len1 - len2)

    ps = r_add_lists(l1, l2)

    # Check if there was a carry value left over.
    if ps.carry == 0:
        return ps.sum_node
    else:
        return insert_before(ps.sum_node, ps.carry)


def r_add_lists(l1: ListNode or None, l2: ListNode or None) -> PartialSum:
    if l1 is None and l2 is None:
        return PartialSum()

    ps = r_add_lists(l1.next, l2.next)

    value = ps.carry + l1.val + l2.val

    # Insert new node.
    full_result = insert_before(ps.sum_node, value % 10)

    ps.sum_node = full_result
    ps.carry = 1 if value >= 10 else 0

    return ps


def insert_before(node: ListNode, value: int) -> ListNode:
    new_node = ListNode(value)
    new_node.next = node
    return new_node


def length(i_list: ListNode) -> int:
    if i_list is None:
        return 0

    return 1 + length(i_list.next)


def pad_list(io_list: ListNode, x: int) -> ListNode:
    while x > 0:
        node = ListNode(0)
        node.next = io_list
        io_list = node
        x -= 1

    return io_list


class Test(unittest.TestCase):
    """Test cases."""
    # data = [(ListNode(7, ListNode(1, ListNode(6))),
    #          ListNode(5, ListNode(9, ListNode(2))),
    #          ListNode(2, ListNode(1, ListNode(9)))),
    #         (ListNode(7, ListNode(1, ListNode(9))),
    #          ListNode(5, ListNode(9, ListNode(2))),
    #          ListNode(2, ListNode(1, ListNode(2, ListNode(1))))),
    #         (ListNode(7, ListNode(1, ListNode(6))),
    #          ListNode(5, ListNode(9, ListNode(2, ListNode(5)))),
    #          ListNode(2, ListNode(1, ListNode(9, ListNode(5)))))
    #         ]

    # Follow up.
    data = [(ListNode(6, ListNode(1, ListNode(7))),
             ListNode(2, ListNode(9, ListNode(5))),
             ListNode(9, ListNode(1, ListNode(2)))),
            (ListNode(9, ListNode(1, ListNode(7))),
             ListNode(2, ListNode(9, ListNode(5))),
             ListNode(1, ListNode(2, ListNode(1, ListNode(2))))),
            (ListNode(6, ListNode(1, ListNode(7))),
             ListNode(5, ListNode(2, ListNode(9, ListNode(5)))),
             ListNode(5, ListNode(9, ListNode(1, ListNode(2)))))
            ]

    def test_add_lists(self):
        for l1, l2, expected in self.data:
            self.assertEqual(expected.print_forward(), add_lists(l1, l2).print_forward())


if __name__ == "__main__":
    unittest.main()
