"""
Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a
binary search tree with minimal height.
Hints: #19, #73, #176
"""

from typing import List, Optional


class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None


def create_minimal_bst(arr: List[int]) -> Node:
    return r_create_minimal_bst(arr, 0, len(arr) - 1)


def r_create_minimal_bst(arr: List[int], start: int, end: int) -> Optional[Node, None]:
    if end < start:
        return None
    mid = (start + end) // 2
    n = Node(arr[mid])
    n.left = r_create_minimal_bst(arr, start, mid - 1)
    n.right = r_create_minimal_bst(arr, mid + 1, end)
    return n
