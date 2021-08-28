import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> list[Optional[ListNode]]:
        """
        Time Complexity: O(2N) -> O(N)
        Space Complexity: O(N)

        Algorithm:
        -----------
        We calculate whether we will
        have either size 1 groups with
        empty groups, or large groups
        with smaller groups. Then, we create a
        spread of how large each group
        will be. Then, we use that
        spread to create groups of the
        correct sizes, and return the list
        of the head references for each
        group.
        """
        n: int = get_number_of_nodes(head)
        quotient: float = n / k  # 0.6
        k_parts_spread: list[int] = []
        if quotient < 1:
            k_parts_spread = get_single_group_spread(n, k)
        else:
            k_parts_spread = get_dynamic_group_spread(n, k)
        output: list[Optional[ListNode]] = []
        pointer: Optional[ListNode] = head
        for group_size in k_parts_spread:
            part, pointer = create_linked_list_of_size(group_size, pointer)
            output.append(part)
        return output


def get_number_of_nodes(head: ListNode) -> int:
    n = 0
    while head is not None:
        n += 1
        head = head.next
    return n


def get_single_group_spread(n: int, k: int) -> list[int]:
    single_group_spread: list[int] = []
    for _ in range(n):
        single_group_spread.append(1)
    for _ in range(k - n):
        single_group_spread.append(0)
    return single_group_spread


def get_dynamic_group_spread(n: int, k: int) -> list[int]:
    """
    Time Complexity: O(K)
    Space Complexity: O(1)

    Algorithm:
    -----------
    This function gets the proper
    group spread given the problem
    constraints, when the groups
    require the first couple of
    groups to be larger than the
    rest. Since we don't initially
    know what size the large groups
    should be, we do a trial and error
    approach to find that number.
    """
    dynamic_group_spread: list[int] = []
    quotient: float = n / k
    number_of_large_groups = 0  # pre-initial value
    number_of_small_groups = k  # pre-initial value
    while sum(dynamic_group_spread) != n:
        number_of_large_groups += 1
        number_of_small_groups -= 1
        dynamic_group_spread.clear()
        for _ in range(number_of_large_groups):
            dynamic_group_spread.append(math.ceil(quotient))
        for _ in range(number_of_small_groups):
            dynamic_group_spread.append(math.floor(quotient))
    return dynamic_group_spread


def create_linked_list_of_size(group_size: int, node: Optional[ListNode]) -> tuple:
    """
    Time Complexity: O(group_size)
    Space Complexity: O(group_size)
    """
    if group_size == 0:
        return None, node
    head = ListNode(node.val)
    cursor = head
    node = node.next
    group_size -= 1
    while node is not None and group_size != 0:
        cursor.next = ListNode(node.val)
        cursor = cursor.next
        node = node.next
        group_size -= 1
    return head, node


def create_linked_list_from_numbers(numbers: list[int]) -> ListNode:
    """
    Helper function for debugging
    """
    head = ListNode(numbers[0])
    cursor = head
    for val in numbers[1:]:
        cursor.next = ListNode(val)
        cursor = cursor.next
    return head


if __name__ == '__main__':
    solution = Solution()
    result_1 = solution.splitListToParts(
        head=create_linked_list_from_numbers([1, 2, 3]),
        k=5
    )
    result_2 = solution.splitListToParts(
        head=create_linked_list_from_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        k=3
    )



