"""
Three in One: Describe how you could use a single array to implement three stacks.
"""


# class FixedMultiStack:
#     def __init__(self, stack_size: int):
#         self.number_of_stacks = 3
#         self.stack_capacity = stack_size
#         self.values = [0] * (self.number_of_stacks * self.stack_capacity)
#         self.sizes = [0] * self.number_of_stacks
#
#     # Push value onto stack.
#     def push(self, stack_num: int, value: int):
#         # Check that we have space for the next element.
#         if self.is_full(stack_num):
#             raise Exception("Stack is full.")
#
#         self.sizes[stack_num] += 1
#         self.values[self.index_of_top(stack_num)] = value
#
#     # Pop item from top stack.
#     def pop(self, stack_num: int) -> int:
#         if self.is_empty(stack_num):
#             raise Exception("Stack is empty.")
#
#         top_index = self.index_of_top(stack_num)
#         value = self.values[top_index]  # Get top
#         self.values[top_index] = 0  # Clear
#         self.sizes[stack_num] -= 1  # Shrink
#         return value
#
#     # Return top element.
#     def peek(self, stack_num: int) -> int:
#         if self.is_empty(stack_num):
#             raise Exception("Stack is empty.")
#
#         return self.values[self.index_of_top(stack_num)]
#
#     # Return if stack is empty.
#     def is_empty(self, stack_num: int) -> bool:
#         return self.sizes[stack_num] == 0
#
#     # Return if stack is full.
#     def is_full(self, stack_num: int) -> bool:
#         return self.sizes[stack_num] == self.stack_capacity
#
#     # Return index of the top of the stack.
#     def index_of_top(self, stack_num: int) -> int:
#         offset = stack_num * self.stack_capacity
#         size = self.sizes[stack_num]
#         return offset + size - 1


class MultiStack:
    class StackInfo:
        def __init__(self, outer_instance, start: int, capacity: int):
            self.outer_instance = outer_instance
            self.size = 0
            self.start = start
            self.capacity = capacity

        # Check if an index of the full array is within the stack boundaries.
        def is_within_stack_boundaries(self, index: int) -> bool:
            if index < 0 or index > len(self.outer_instance.values):
                return False

            # If index wraps around, adjust it.
            contiguous_index = index + len(self.outer_instance.values) if index < self.start else index
            end = self.start + self.capacity
            return self.start <= contiguous_index < end

        def last_capacity_index(self):
            return self.outer_instance.adjust_index(self.start + self.capacity - 1)

        def last_element_index(self):
            return self.outer_instance.adjust_index(self.start + self.size - 1)

        def is_full(self) -> bool:
            return self.size == self.capacity

        def is_empty(self) -> bool:
            return self.size == 0

    def __init__(self, number_of_stacks: int, default_size: int):
        # Create metadata for all the stacks.
        self.info = [None] * number_of_stacks
        for i in range(number_of_stacks):
            self.info[i] = self.StackInfo(self, default_size * i, default_size)
        self.values = [0] * (number_of_stacks * default_size)

    def number_of_elements(self) -> int:
        size = 0
        for si in self.info:
            size += si.size
        return size

    # Returns true if all stacks are full.
    def all_stacks_are_full(self):
        return self.number_of_elements() == len(self.values)

    # Adjust index to be in the range of 0 -> length - 1.
    def adjust_index(self, index: int) -> int:
        return index % len(self.values)

    # Get index after this index, adjusted for wrap around.
    def next_index(self, index: int) -> int:
        return self.adjust_index(index + 1)

    # Get index before this index, adjusted for wrap around.
    def previous_index(self, index: int) -> int:
        return self.adjust_index(index - 1)

    def shift(self, stack_num: int):
        stack = self.info[stack_num]

        """If this stack is full, then shift the next stack over by one element. This stack can now claim the freed
        element."""
        if stack.size >= stack.capacity:
            next_stack = (stack_num + 1) % len(self.info)
            self.shift(next_stack)
            stack.capacity += 1

        # Shift all elements in stack over by one.
        index = stack.last_capacity_index()
        while stack.is_within_stack_boundaries(index):
            self.values[index] = self.values[self.previous_index(index)]
            index = self.previous_index(index)

        # Adjust stack data.
        self.values[stack.start] = 0  # Clear item
        stack.start = self.next_index(stack.start)  # Move start
        stack.capacity -= 1  # Shrink capacity

    # Expand stack by shifting over other stacks.
    def expand(self, stack_num: int):
        self.shift((stack_num + 1) % len(self.info))
        self.info[stack_num].capacity += 1

    def push(self, stack_num: int, value):
        if self.all_stacks_are_full():
            raise Exception("Stack is full.")

        # If this stack if full, expand it.
        stack = self.info[stack_num]
        if stack.is_full():
            self.expand(stack_num)

        stack.size += 1
        self.values[stack.last_element_index()] = value

    def pop(self, stack_num: int) -> int:
        stack = self.info[stack_num]
        if stack.is_empty():
            raise Exception("Stack is empty.")

        # Remove last element.
        value = self.values[stack.last_element_index()]
        self.values[stack.last_element_index()] = 0
        stack.size -= 1
        return value

    def peek(self, stack_num: int) -> int:
        stack = self.info[stack_num]
        if stack.is_empty():
            raise Exception("Stack is empty.")

        return self.values[stack.last_element_index()]


# if __name__ == "__main__":
    # ms = MultiStack(3, 4)
    # print(', '.join(str(elm) for elm in ms.values))
    # ms.push(0, 10)
    # print(', '.join(str(elm) for elm in ms.values))
    # ms.push(1, 20)
    # print(', '.join(str(elm) for elm in ms.values))
    # ms.push(2, 30)
    # print(', '.join(str(elm) for elm in ms.values))
    # ms.push(1, 21)
    # ms.push(0, 11)
    # ms.push(0, 12)
    # print(', '.join(str(elm) for elm in ms.values))
    #
    # print(ms.pop(0))
    # print(', '.join(str(elm) for elm in ms.values))
    #
    # ms.push(2, 31)
    # print(', '.join(str(elm) for elm in ms.values))
    #
    # ms.push(0, 13)
    # print(', '.join(str(elm) for elm in ms.values))
    # ms.push(1, 22)
    # print(', '.join(str(elm) for elm in ms.values))
    #
    # ms.push(2, 31)
    # print(', '.join(str(elm) for elm in ms.values))
    #
    # ms.push(0, 13)
    # print(', '.join(str(elm) for elm in ms.values))
    #
    # ms.push(1, 22)
    # print(', '.join(str(elm) for elm in ms.values))
    #
    # ms.push(0, 5)
    # print(', '.join(str(elm) for elm in ms.values))
