"""
BST Sequences.
"""

from typing import List, Deque
from collections import deque
import itertools


class Node:
    def __init__(self, item, left=None, right=None):
        self.val = item
        self.left = left
        self.right = right


def all_sequences(node: Node) -> List[Deque[int]]:
    result = []

    if not node:
        result.append(deque())
        return result

    prefix = deque()
    prefix.append(node.val)

    # Recurse on left and right subtrees.
    left_seq = all_sequences(node.left)
    right_seq = all_sequences(node.right)

    # Weave together each list from the left and right sides.
    for left, right in itertools.product(left_seq, right_seq):
        weaved = []
        weave_lists(prefix, left, right, weaved)
        result.extend(weaved)

    return result


def weave_lists(prefix: Deque[int], first: Deque[int], second: Deque[int], results: List[Deque[int]]) -> None:
    if not first or not second:
        result = prefix.copy()
        result.extend(first)
        result.extend(second)
        results.append(result)
        return None

    # Recurse with the head of first added to the prefix.
    head_first = first.popleft()
    prefix.append(head_first)
    weave_lists(prefix, first, second, results)
    prefix.pop()
    first.appendleft(head_first)

    # Recurse with the head of second added to the prefix.
    head_second = second.popleft()
    prefix.append(head_second)
    weave_lists(prefix, first, second, results)
    prefix.pop()
    second.appendleft(head_second)
