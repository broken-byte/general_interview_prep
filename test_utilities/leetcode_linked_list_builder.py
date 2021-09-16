from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_head_of_built_linked_list(leet_code_input: list[int]) -> Optional[ListNode]:
    if len(leet_code_input) == 0:
        return None
    n: int = len(leet_code_input)
    head = ListNode(leet_code_input[0])
    current = head
    for val in leet_code_input[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
