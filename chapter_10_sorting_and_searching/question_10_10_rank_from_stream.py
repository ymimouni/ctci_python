from random import choices


class RankNode:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None
        self.left_size = 0

    def insert(self, x: int):  # noqa
        if x <= self.data:
            if not self.left:
                self.left = RankNode(x)
            else:
                self.left.insert(x)
            self.left_size += 1
        else:
            if not self.right:
                self.right = RankNode(x)
            else:
                self.right.insert(x)

    def get_rank(self, x: int):  # noqa
        if self.data == x:
            return self.left_size + 1
        elif x < self.data:
            if not self.left:
                return None
            else:
                return self.left.get_rank(x)
        else:
            right_rank = None if not self.right else self.right.get_rank(x)
            if not right_rank:
                return None
            else:
                return self.left_size + 1 + right_rank


if __name__ == "__main__":
    arr = choices(range(-10, 10), k=10)
    print(arr)

    root = RankNode(arr[0])
    for x in arr[1:]:
        root.insert(x)

    for x in range(-11, 11):
        print(f'{x}: ', root.get_rank(x))
