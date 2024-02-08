"""
Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search
tree. You may assume that each node has a link to its parent.
Hints: #79, #91
"""


class Node:
    def __init__(self, item, left=None, right=None):
        self.val = item
        self.left = left
        self.right = right
        self.parent = None
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self


def r_inorder_succ(n: Node) -> Node or None:
    if not n:
        return None

    # Found right children, return leftmost child of right subtree
    if not n.parent or n.right:
        return left_most_child(n.right)
    else:
        # Go up until we are on left instead of right.
        x = n
        while x and x.parent.left is not x:
            x = x.parent
        return x


def left_most_child(n: Node) -> Node or None:
    if not n:
        return None
    while n.left:
        n = n.left
    return n
