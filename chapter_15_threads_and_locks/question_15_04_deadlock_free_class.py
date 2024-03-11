from threading import Lock

from ctci.ctci_library.assorted import SingletonType


class LockFactory(metaclass=SingletonType):
    def __init__(self, count: int):
        self.num_of_locks = count
        self.locks = [LockNode(i, count) for i in range(self.num_of_locks)] * self.num_of_locks
        self.lock_order = {}

    # To prevent deadlocks, force processes to declare upfront in what order they will need the locks. Verify that this
    # order does not create a deadlock (a cycle in a directed graph).
    def declare(self, owner_id, resources_in_order):


class LockNode:
    def __init__(self, id, max):  # noqa
        self.lcok_id = id
        self.max_locks = max
        self.children = []
        self.lock = None

    # Join this to node, checking to make sure it does not create a cycle.
    def join_to(self, node):
        self.children.append(node)

    def remove(self, node):
        self.children.remove(node)

    # Check for a cycle by doing a depth-first-search.
    def has_cycle(self):
        ...

    def get_lock(self):
        if not self.lock:
            self.lock = Lock()
        return self.lock


if __name__ == "__main__":
    res1 = [1, 2, 3, 4]
    res2 = [1, 5, 4, 1]
    res3 = [1, 4, 5]

    num_of_locks = 10
