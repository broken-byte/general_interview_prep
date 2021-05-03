from itertools import tee
from collections import deque


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        """
        What are we optimizing for?
        ----------------------------

        1. Make the smallest number of groups such that all of the groups
            except the first group have exactly k elements.

        Constraints
        ------------

        1. Maintain the original order
        2. All groups except the first have to be size k
        3. All lowercase letters should be upper cased
        4. First group must be 1 <= size <= k


        Algorithm
        Example: s = "5F3Z-2e-9-w", k = 4
        -------------
        1. Split string up by dashes
        [5F3Z, 2e, 9, w]
        2. Aggregate groups 1-> n - 1 (skip first) from left to right, as if they are being
            "squished" together from the right.
            2a. Iterate pairwise, asking if p1 has k elements, and if so, moving elements from p2
                to p1 until it DOES have k elements.

        TC: O(2n)
        TODO: Fix this case: "2-4A0r7-4k", 4
        """
        initial_groups: list = self.split_license_into_groups_and_convert_to_deques(s)
        aggregated_groups: list = self.aggregate_into_size_k_groups(initial_groups, k)
        formatted_result: str = self.convert_groups_into_upper_case_string(aggregated_groups)
        return formatted_result[:-1]

    def split_license_into_groups_and_convert_to_deques(self, s: str) -> list:
        initial_groups: list = s.split("-")
        return [deque(group) for group in initial_groups]

    def aggregate_into_size_k_groups(self, initial_groups: list, k: int) -> list:
        i, j = 1, 2
        while j < len(initial_groups):
            current_group: deque = initial_groups[i]
            next_group: deque = initial_groups[j]
            self.transfer_elements_until_current_is_full(current_group, next_group, k)
            if len(next_group) == 0:
                j += 1
            else:
                i += 1
                j += 1
        return initial_groups

    def transfer_elements_until_current_is_full(self, current_group: deque, next_group: deque, k: int):
        while len(current_group) != k and len(next_group) != 0:
            current_group.append(next_group.popleft())

    def convert_groups_into_upper_case_string(self, groups: list) -> str:
        final_output: str = ""
        for group in groups:
            if len(group) == 0:
                break
            upper_cased_group: list = self.upper_case(group)
            final_output += "".join(upper_cased_group) + "-"
        return final_output

    def upper_case(self, group: list) -> list:
        for index in range(len(group)):
            group[index] = group[index].upper()
        return group


if __name__ == '__main__':
    solution = Solution()
    print(solution.licenseKeyFormatting(s = "5F3Z-2e-9-w", k = 4))