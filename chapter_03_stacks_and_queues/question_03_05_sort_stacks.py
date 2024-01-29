"""
Sort stack.
"""

from collections import deque
from typing import Deque
import random


def merge_sort(s: Deque) -> Deque:
    if len(s) <= 1:
        return s

    left = deque()
    right = deque()
    count = 0
    while s:
        count += 1
        if count % 2 == 0:
            left.append(s.pop())
        else:
            right.append(s.pop())

    left = merge_sort(left)
    right = merge_sort(right)
    while left or right:
        if not left:
            s.append(right.pop())
        elif not right:
            s.append(left.pop())
        elif left[-1] <= right[-1]:
            s.append(left.pop())
        else:
            s.append(right.pop())

    # Reverse the stack.
    s.reverse()

    return s


def sort(s: Deque) -> None:
    r = deque()
    while s:
        # Insert each element in s in sorted order into r.
        temp = s.pop()
        while r and r[-1] > temp:
            s.append(r.pop())
        r.append(temp)

    # Copy the elements from r back into s.
    while r:
        s.append(r.pop())


if __name__ == "__main__":
    a_stack = deque(random.sample(range(50), 10))
    print(a_stack)
    merge_sort(a_stack)
    print(a_stack)
