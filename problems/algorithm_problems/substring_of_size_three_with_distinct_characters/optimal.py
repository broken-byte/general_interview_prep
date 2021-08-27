

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        """
        Time Complexity: O(3*N) -> O(N)
        Space Complexity: O(3) -> O(1)

        Algorithm: Sliding Window
        """
        n = len(s)
        if n < 3:
            return 0
        count_of_good_strings = 0
        left_cursor = 0
        for right_cursor in range(2, len(s)):
            substring: str = s[left_cursor: right_cursor + 1]
            if has_no_repeated_characters(substring):
                count_of_good_strings += 1
            left_cursor += 1
        return count_of_good_strings


def has_no_repeated_characters(substring: str) -> bool:
    distinct_chars = set(substring)
    return len(substring) == len(distinct_chars)


if __name__ == '__main__':
    solution = Solution()
    print(solution.countGoodSubstrings(s="xyzzaz"))
    print(solution.countGoodSubstrings(s="aababcabc"))
