

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous: ListNode = None
        current: ListNode = head
        next: ListNode = None
        while current is not None:
            # Reverse node
            next = current.next
            current.next = previous

            # Traverse
            previous = current
            current = next
        return previous