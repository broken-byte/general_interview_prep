from typing import Optional

from test_utilities.leetcode_linked_list_builder import get_head_of_built_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time Complexity: O(N) ~(N + 1/2N)
    Space Complexity: O(1)
    """
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size_of_linked_list: int = get_size(head)
        middle_index: int = size_of_linked_list // 2
        counter: int = 0
        while counter != middle_index:
            head = head.next
            counter += 1
        return head


def get_size(head: Optional[ListNode]) -> int:
    size_counter: int = 0
    while head is not None:
        size_counter += 1
        head = head.next
    return size_counter


if __name__ == '__main__':
    solution = Solution()
    head_1 = get_head_of_built_linked_list([1, 2, 3, 4, 5, 6])
    head_2 = get_head_of_built_linked_list([1, 2, 3, 4, 5])
    print(solution.middleNode(head_1).val)
    print(solution.middleNode(head_2).val)
