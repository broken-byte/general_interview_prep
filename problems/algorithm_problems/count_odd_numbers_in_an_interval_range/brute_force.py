

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        odd_number_count = 0
        for number in range(low, high + 1):
            if number % 2 != 0:
                odd_number_count += 1
        return odd_number_count


if __name__ == '__main__':
    solution = Solution()
    print(solution.countOdds(3, 7))
