"""
Check Subtree.
"""


class Node:
    def __init__(self, item, left=None, right=None):
        self.val = item
        self.left = left
        self.right = right


def contains_tree(t1: Node, t2: Node) -> bool:
    if not t2:
        return True  # The empty tree is a subtree of everytree.

    return is_subtree(t1, t2)


def is_subtree(t1: Node, t2: Node) -> bool:
    if not t1:
        return False
    elif t1.val == t2.val and match_tree(t1, t2):
        return True
    return is_subtree(t1.left, t2) or is_subtree(t1.right, t2)


def match_tree(t1: Node, t2: Node) -> bool:
    if not t1 and not t2:
        return True
    elif not t1 or not t2:
        return False
    elif t1.val != t2.val:
        return False
    else:
        return match_tree(t1.left, t2.left) and match_tree(t1.right, t2.right)
