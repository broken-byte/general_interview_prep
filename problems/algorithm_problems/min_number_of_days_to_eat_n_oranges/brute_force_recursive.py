from functools import lru_cache


class Solution:
    @lru_cache(None)
    def minDays(self, n: int) -> int:
        """
        Time Complexity: O(3^N)
        Space Complexity: O(N)

        Unfortunately, not many sub problems
        are repeated here, so caching in this
        way is not efficient enough
        """
        if n <= 0:
            return 0
        days_to_consume_oranges: list[int] = []
        eat_one_orange: int = self.minDays(n - 1)
        days_to_consume_oranges.append(eat_one_orange)
        if n % 2 == 0:
            eat_half_n_oranges: int = self.minDays(n - n // 2)
            days_to_consume_oranges.append(eat_half_n_oranges)
        if n % 3 == 0:
            eat_third_n_oranges_times_two: int = self.minDays(n - 2 * (n // 3))
            days_to_consume_oranges.append(eat_third_n_oranges_times_two)
        return 1 + min(days_to_consume_oranges)


if __name__ == '__main__':
    solution = Solution()
    print(solution.minDays(10))
    print(solution.minDays(6))
    print(solution.minDays(1))
    print(solution.minDays(56))
    print(solution.minDays(820592))
