"""
Validate BST: Implement a function to check if a binary tree is a binary search tree.
Hints: #35, #57, #86, # 773, # 728
"""


class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None


last_printed = None


# def r_check_bst(root: Node, is_left: bool) -> bool:
#     global last_printed
#     if not root:
#         return True
#
#     # Check / recurse left.
#     if not r_check_bst(root.left, True):
#         return False
#
#     # Check current.
#     if last_printed:
#         if is_left:
#             # Left child is allowed to be equal to part.
#             if root.val < last_printed:
#                 return False
#         else:
#             # Right child is not allowed to be equal to parent.
#             if root.val <= last_printed:
#                 return False
#     last_printed = root.val
#
#     # Check / recurse right.
#     if not r_check_bst(root.right, False):
#         return False
#
#     return True
#
#
# def check_bst(root: Node) -> bool:
#     return r_check_bst(root, True)


def check_bst(n: Node) -> bool:
    return r_check_bst(n, None, None)


def r_check_bst(n: Node, min: int or None, max: int or None) -> bool:
    if not n:
        return True
    if (min and n.val <= min) or (max and n.val > max):
        return False
    if not r_check_bst(n.left, min, n.val) or not r_check_bst(n.right, n.val, max):
        return False
    return True
