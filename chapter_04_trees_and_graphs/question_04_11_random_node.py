"""
Random Node.
"""

from typing import Optional
import random


class Node:
    def __init__(self, item, left=None, right=None):
        self.val = item
        self.left = left
        self.right = right
        self.size = 1
    
    def insert_in_order(self, v: int):
        if self.val >= v:
            if not self.left:
                self.left = Node(v)
            else:
                self.left.insert_in_order(v)
        else:
            if not self.right:
                self.right = Node(v)
            else:
                self.right.insert_in_order(v)
        self.size += 1

    def find(self, d: int) -> Optional['Node']:
        if d == self.val:
            return self
        elif d <= self.val:
            return self.left.find(d) if self.left else None
        elif d > self.val:
            return self.right.find(d) if self.right else None
        return None

    def get_random_node(self) -> 'Node':
        r = random.randint(0, self.size)
        print(r)
        # r = 7
        return self.get_ith_node(r)

    def get_ith_node(self, i: int) -> 'Node':
        left_size = self.left.size if self.left else 0
        if i == self.size:
            return self
        elif i <= left_size:
            return self.left.get_ith_node(i)
        else:
            return self.right.get_ith_node(i - left_size)


class Tree:
    def __init__(self, root=None):
        self.root = root

    def insert_in_order(self, val: int):
        if not self.root:
            self.root = Node(val)
        else:
            self.root.insert_in_order(val)

    def get_random_node(self) -> Optional[Node]:
        if not self.root:
            return None
        return self.root.get_random_node()


if __name__ == "__main__":
    t = Tree()
    t.insert_in_order(13)
    t.insert_in_order(7)
    t.insert_in_order(15)
    t.insert_in_order(9)
    t.insert_in_order(4)
    t.insert_in_order(3)
    t.insert_in_order(17)
    t.insert_in_order(1)

    print(t.get_random_node().val)
    print(t.root.find(0))