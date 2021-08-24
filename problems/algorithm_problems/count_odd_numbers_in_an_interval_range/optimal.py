

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        total_numbers_in_range: int = (high - low) + 1
        if total_numbers_in_range % 2 == 0:
            return total_numbers_in_range // 2
        if low % 2 != 0 or high % 2 != 0:
            return total_numbers_in_range // 2 + 1
        return total_numbers_in_range // 2


if __name__ == '__main__':
    solution = Solution()
    print(solution.countOdds(3, 7))
    print(solution.countOdds(8, 10))
    print(solution.countOdds(21, 22))
    print(solution.countOdds(13, 18))
