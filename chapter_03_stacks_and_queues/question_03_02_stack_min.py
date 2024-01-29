"""
Stack Min: How would you design a stack which, in addition to push and pop, has a function min which returns the
minimum element? Push, pop and min should all operate in 0(1) time.
"""


# class MinStack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, x: int) -> None:
#         # If the stack is empty, then the min value is the first value we add.
#         if not self.stack:
#             self.stack.append((x, x))
#         else:
#             current_min = self.stack[-1][1]
#             self.stack.append((x, min(x, current_min)))
#
#     def pop(self) -> int:
#         return self.stack.pop()[0]
#
#     def peek(self) -> int:
#         return self.stack[-1][0]
#
#     def get_min(self):
#         return self.stack[-1][1]


# Using a second stack to keep track of the min.
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        # Always put the number on the main stack.
        self.stack.append(x)

        # If the min stack is empty, or this number is smaller than the top of the min stack, put it on with a count of
        # 1
        if not self.min_stack or x < self.min_stack[-1][0]:
            self.min_stack.append([x, 1])

        # Else if this number is equal to what's currently at the top of the min stack, then increment the count at the
        # top by 1.
        elif x == self.min_stack[-1][0]:
            self.min_stack[-1][1] += 1

    def pop(self) -> int:
        # If the top of min stack is the same as the top of stack, then we need to decrement the count at the top by 1.
        if self.stack[-1] == self.min_stack[-1][0]:
            self.min_stack[-1][1] -= 1

        # If the count at the top of min stack is now 0, then remove that value.
        if self.min_stack[-1][0]:
            self.min_stack.pop()

        # Pop the main stack.
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min_stack[-1][0]