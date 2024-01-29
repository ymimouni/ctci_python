"""
Stack of plates.
"""


class Node:
    def __init__(self, value: int):
        self.above = None
        self.below = None
        self.value = value


class Stack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.top = None
        self.bottom = None

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    @staticmethod
    def join(above: Node, below: Node):
        if above is not None:
            above.below = below
        if below is not None:
            below.above = above

    def push(self, value: int) -> bool:
        if self.size >= self.capacity:
            return False
        self.size += 1
        n = Node(value)
        if self.size == 1:
            self.bottom = n
        self.join(n, self.top)
        self.top = n
        return True

    def pop(self) -> bool:
        if self.top is None:
            return False
        t = self.top
        self.top = self.top.below
        self.size -= 1
        return t.value

    def remove_bottom(self):
        b = self.bottom
        self.bottom = self.bottom.above
        if self.bottom is not None:
            self.bottom.below = None
        self.size -= 1
        return b.value


class SetOfStacks:
    def __init__(self, stack_size: int):
        self.stack_capacity = stack_size
        self.set_of_stacks = []

    def get_last_stack(self):
        if not self.set_of_stacks:
            return None
        return self.set_of_stacks[-1]

    def is_empty(self):
        last = self.get_last_stack()
        return last is None or last.is_empty()

    def push(self, value: int):
        last_stack = self.get_last_stack()
        if last_stack and not last_stack.is_full():
            last_stack.push(value)
        else:
            new_stack = Stack(self.stack_capacity)
            new_stack.push(value)
            self.set_of_stacks.append(new_stack)

    def pop(self):
        last_stack = self.get_last_stack()
        if not last_stack:
            raise Exception("The stack is empty.")
        v = last_stack.pop()
        if last_stack.is_empty():
            self.set_of_stacks.pop()
        return v

    def pop_at(self, index: int) -> int:
        return self.left_shift(index, True)

    def left_shift(self, index: int, remove_top: bool) -> int:
        stack = self.set_of_stacks[index]
        if remove_top:
            removed_item = stack.pop()
        else:
            removed_item = stack.remove_bottom()
        if stack.is_empty():
            self.set_of_stacks.remove(index)
        elif len(self.set_of_stacks) > index + 1:
            v = self.left_shift(index + 1, False)
            stack.push(v)
        return removed_item
