"""
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth
(e.g., if you have a tree with depth 0, you'll have 0 linked lists).
Hints: #107, #123, #735
"""

from typing import List


class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None


def create_level_linked_list_bfs(root: Node) -> List[List[Node]]:
    result = []

    # Visit the root.
    current = []
    if root:
        current.append(root)

    while current:
        result.append(current)
        parents = current
        current = []
        for parent in parents:
            if parent.left:
                current.append(parent.left)
            if parent.right:
                current.append(parent.right)

    return result


def create_level_linked_list_dfs(root: Node) -> List[List[Node]]:
    lists = []
    r_create_level_linked_list_dfs(root, lists, 0)
    return lists


def r_create_level_linked_list_dfs(root: Node, lists: List, level: int):
    if not root:
        return None
    if len(lists) == level:
        l = []
        lists.append(l)
    else:
        l = lists[level]
    l.append(root)
    r_create_level_linked_list_dfs(root.left, lists, level + 1)
    r_create_level_linked_list_dfs(root.right, lists, level + 1)
