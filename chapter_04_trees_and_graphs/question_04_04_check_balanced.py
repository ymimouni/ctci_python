"""
Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of this question, a
balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than
one.
Hints: #27, #33, #49, #705, #724
"""


class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None


def get_heigth(root: Node) -> int:
    if root is None:
        return -1
    return max(get_heigth(root.left), get_heigth(root.right)) + 1


def is_balanced(root: Node) -> bool:
    if not root:
        return True
    height_diff = abs(get_heigth(root.left) - get_heigth(root.right))
    if height_diff > 1:
        return False
    else:
        return is_balanced(root.left) and is_balanced(root.right)


def check_heigth(root: Node) -> int:
    if not root:
        return -1

    left_heigth = check_heigth(root.left)
    if left_heigth == -2:
        return -2  # Pass error up

    right_heigth = check_heigth(root.right)
    if left_heigth == -2:
        return -2  # Pass error up

    heigth_diff = abs(left_heigth - right_heigth)
    if heigth_diff > 1:
        return -2
    else:
        return max(left_heigth, right_heigth) + 1


def check_balanced(root: Node) -> bool:
    # -2 is the error code.
    return check_heigth(root) != -2
