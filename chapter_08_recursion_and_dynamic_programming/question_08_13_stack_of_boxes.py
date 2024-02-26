from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass()
class Box:
    width: int
    height: int
    depth: int

    def can_be_above(self, box: Box):
        return self.width >= box.width and self.height >= box.height and self.depth >= box.depth


# def create_stack(boxes: List[Box]) -> int:  # noqa
#     sorted(boxes, key=lambda box: box.height)
#     stack_map = [None] * len(boxes)
#     max_height = 0
#     for i in range(0, len(boxes)):
#         height = r_create_stack(boxes, i, stack_map)
#         max_height = max(max_height, height)
#     return max_height
#
#
# def r_create_stack(boxes: List[Box], bottom_index: int, stack_map: List[int]) -> int:  # noqa
#     if stack_map[bottom_index]:
#         return stack_map[bottom_index]
#     bottom = boxes[bottom_index]
#     max_height = 0
#     for i in range(bottom_index + 1, len(boxes)):
#         if boxes[i].can_be_above(bottom):
#             height = r_create_stack(boxes, i, stack_map)
#             max_height = max(max_height, height)
#     max_height += bottom.height
#     stack_map[bottom_index] = max_height
#     return max_height


def create_stack(boxes: List[Box]) -> int:  # noqa
    sorted(boxes, key=lambda box: box.height)
    stack_map = [None] * len(boxes)
    return r_create_stack(boxes, None, 0, stack_map)


def r_create_stack(boxes: List[Box], bottom: Optional[Box], offset: int, stack_map: List[Optional[int]]) -> int:  # noqa
    if offset >= len(boxes):
        return 0

    # Height with the bottom
    new_bottom = boxes[offset]
    height_with_bottom = 0
    if not bottom or new_bottom.can_be_above(bottom):
        if not stack_map[offset]:
            stack_map[offset] = r_create_stack(boxes, new_bottom, offset + 1, stack_map)
            stack_map[offset] += new_bottom.height
        height_with_bottom = stack_map[offset]

    # Height without bottom
    height_without_bottom = r_create_stack(boxes, bottom, offset + 1, stack_map)

    return max(height_with_bottom, height_without_bottom)


if __name__ == "__main__":
    boxes = [Box(6, 4, 4), Box(8, 6, 2), Box(5, 3, 3), Box(7, 8, 3), Box(4, 2, 2), Box(9, 7, 3)]
    print(create_stack(boxes))
