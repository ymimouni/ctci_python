"""
Queue via stacks.
"""

from collections import deque

# class Queue:
#     def __init__(self):
#         self.stack_newest = []
#         self.stack_oldest = []
#
#     def add(self, value: int):
#         self.stack_newest.append(value)
#
#     def peek(self):
#         self.shift_stacks()
#         return self.stack_oldest[-1]
#
#     def remove(self):
#         self.shift_stacks()
#         return self.stack_oldest.pop()
#
#     # Move elements from stack_newest to stack_oldest.
#     def shift_stacks(self):
#         if not self.stack_oldest:
#             while self.stack_newest:
#                 self.stack_oldest.append(self.stack_newest.pop())


# Using Deque.
class Queue:
    def __init__(self):
        self.stack_newest = deque()
        self.stack_oldest = deque()

    def add(self, value: int):
        self.stack_newest.append(value)

    def peek(self):
        self.shift_stacks()
        return self.stack_oldest[-1]

    def remove(self):
        self.shift_stacks()
        return self.stack_oldest.pop()

    # Move elements from stack_newest to stack_oldest.
    def shift_stacks(self):
        if not self.stack_oldest:
            while self.stack_newest:
                self.stack_oldest.append(self.stack_newest.pop())
