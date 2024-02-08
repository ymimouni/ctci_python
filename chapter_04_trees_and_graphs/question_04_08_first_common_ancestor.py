"""
First Common Ancestor
"""

# from typing import Optional


class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None


# def common_ancestor(root: Node, p: Node, q: Node) -> Optional[Node]:
#     # Error check: One node is not in the tree.
#     if not covers(root, p) or not covers(root, q):
#         return None
#
#     return ancestor_helper(root, p, q)
#
#
# def ancestor_helper(root: Node, p: Node, q: Node) -> Optional[Node]:
#     if root is None or root is p or root is q:
#         return root
#
#     p_is_on_left = covers(root.left, p)
#     q_is_on_left = covers(root.left, q)
#     if p_is_on_left != q_is_on_left:
#         return root
#
#     child_side = root.left if p_is_on_left else root.right
#     return ancestor_helper(child_side, p, q)
#
#
# def covers(root: Node, n: Node) -> bool:
#     if not root:
#         return False
#     if root is n:
#         return True
#
#     return covers(root.left, n) or covers(root.right, n)


# Optimized.
class Result:
    def __init__(self, node, is_anc: bool):
        self.node = node
        self.is_ancestor = is_anc


def common_ancestor(root: Node, p: Node, q: Node) -> Result:
    if not root:
        return Result(None, False)

    if root is p and root is q:
        return Result(root, True)

    rx = common_ancestor(root.left, p, q)
    if rx.is_ancestor:
        # Found common ancestor.
        return rx

    ry = common_ancestor(root.right, p, q)
    if ry.is_ancestor:
        # Found commong ancestor.
        return ry

    if rx.node and ry.node:
        return Result(root, True)  # This is the common ancestor.
    elif root is p or root is q:
        # If we are currently at p or q, and we also found one of those nodes in a subtree, then this is truly an
        # ancestor and the flag should be True.
        is_ancestor = rx.node or ry.node
        return Result(root, is_ancestor)
    else:
        return Result(rx.node if rx.node else ry.node, False)
