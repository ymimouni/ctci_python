"""
Loop detection.
"""

from ctci.ctci_library.assorted import ListNode


def find_beginning(head: ListNode) -> ListNode or None:
    slow, fast = head

    # Find meeting point.
    while fast is not None and fast.next is not None:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            break

    # Check no meeting point: no loop.
    if fast is None or fast.next is None:
        return None

    # Move slow to head. Keep fast at meeting point. Each are k steps from loop start.
    slow = head
    while slow is not fast:
        slow, fast = slow.next, fast.next

    # Return either
    return slow
