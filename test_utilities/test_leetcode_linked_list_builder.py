import unittest
from typing import Optional

from leetcode_linked_list_builder import ListNode, get_head_of_built_linked_list


class TestLinkedListBuilder(unittest.TestCase):

    def test_that_linked_list_builder_can_build_a_linked_list(self):
        expected_value_traversal = [1, 2, 3, 4, 5, 6]
        leetcode_test_input = [1, 2, 3, 4, 5, 6]
        head_of_built_linked_list: ListNode = get_head_of_built_linked_list(leetcode_test_input)
        actual_value_traversal: list[int] = self.get_linked_list_value_traversal(head_of_built_linked_list)
        self.assertEqual(expected_value_traversal, actual_value_traversal)

    def get_linked_list_value_traversal(self, head_of_built_linked_list: Optional[ListNode]) -> list[int]:
        values: list[int] = []
        while head_of_built_linked_list is not None:
            value: int = head_of_built_linked_list.val
            values.append(value)
            head_of_built_linked_list = head_of_built_linked_list.next
        return values


