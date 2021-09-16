

from typing import Optional

from test_utilities.leetcode_linked_list_builder import get_head_of_built_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)

    Algorithm: slow pointer goes 1x speed, fast pointer foes 2x speed, return slow!
    """
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    solution = Solution()
    head_1 = get_head_of_built_linked_list([1, 2, 3, 4, 5, 6])
    head_2 = get_head_of_built_linked_list([1, 2, 3, 4, 5])
    head_3 = get_head_of_built_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    print(solution.middleNode(head_1).val)
    print(solution.middleNode(head_2).val)
    print(solution.middleNode(head_3).val)
