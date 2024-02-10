"""
Paths with Sum.
"""


class Node:
    def __init__(self, item, left=None, right=None):
        self.val = item
        self.left = left
        self.right = right


def count_paths_with_sum(root: Node, target_sum: int) -> int:
    return r_count_paths_with_sum(root, target_sum, 0, {})


def r_count_paths_with_sum(node: Node, target_sum: int, running_sum: int, path_count: dict) -> int:
    if not node:
        return 0

    # Count paths with sum ending at the current node.
    running_sum += node.val
    total_paths = path_count.get(running_sum - target_sum, 0)

    # If running_sum equals target_sum, then one additional path starts at root.
    if running_sum == target_sum:
        total_paths += 1

    # Increment path_count, recurse, then decrement path_count.
    increment_hash_table(path_count, running_sum, 1)
    total_paths += r_count_paths_with_sum(node.left, target_sum, running_sum, path_count)
    total_paths += r_count_paths_with_sum(node.right, target_sum, running_sum, path_count)
    increment_hash_table(path_count, running_sum, -1)

    return total_paths


def increment_hash_table(path_count: dict, running_sum: int, delta: int) -> None:
    new_count = path_count.get(running_sum, 0) + delta
    if not new_count:
        path_count.pop(running_sum)
    else:
        path_count[running_sum] = new_count


# if __name__ == "__main__":
#     root = Node(0)
#     root.left = Node(0)
#     root.right = Node(0)
#     root.right.left = Node(0)
#     root.right.left.right = Node(0)
#     root.right.right = Node(0)
#     print(count_paths_with_sum(root, 4))
