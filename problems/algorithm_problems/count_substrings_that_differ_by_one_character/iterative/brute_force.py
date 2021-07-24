

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        """
        N = len(s)
        M = len(t)
        Time Complexity: O(N*M*min(N, M))
        Space Complexity: O(1)
        """

        def still_within_bounds(s_index: int, t_index: int, position: int) -> bool:
            return s_index + position < len(s) and t_index + position < len(t)

        def count_mismatched_by_one_sub_strings_from(s_index: int, t_index: int) -> int:  # O(min(N, M))
            count, number_of_miss_matches_so_far, position = 0, 0, 0
            while still_within_bounds(s_index, t_index, position) and number_of_miss_matches_so_far < 2:
                not_equal: bool = s[i + position] != t[j + position]
                number_of_miss_matches_so_far += 1 if not_equal else 0
                sub_strings_are_different_by_only_1: bool = number_of_miss_matches_so_far == 1
                count += 1 if sub_strings_are_different_by_only_1 else 0
                position += 1
            return count

        result = 0
        for i in range(len(s)):
            for j in range(len(t)):
                result += count_mismatched_by_one_sub_strings_from(i, j)
        return result
