from collections import defaultdict


class Solution:
    def minDays(self, n: int) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)

        Algorithm
        ----------
        Essentially, we don't have to
        calculate the step of eating
        one orange a day, we can just
        mathematically calculate those
        numbers and go directly to
        the oranges divisible by 2 and 3.
        At that point, we compare the
        minimum number of days for those
        and choose the smallest.

        We use a dictionary to cache values
        instead of an array since our values
        are large and we don't need to store
        values between n // 2 and n // 3.
        """
        dp_table = defaultdict(int)
        dp_table[0] = 0
        dp_table[1] = 1

        def minimum_days_to_eat_oranges(oranges: int) -> int:
            if oranges in dp_table:
                return dp_table[oranges]
            min_days = 1 + min(
                oranges % 2 + minimum_days_to_eat_oranges(oranges // 2),
                oranges % 3 + minimum_days_to_eat_oranges(oranges // 3)
            )
            dp_table[oranges] = min_days
            return dp_table[oranges]
        return minimum_days_to_eat_oranges(n)


if __name__ == '__main__':
    solution = Solution()
    print(solution.minDays(10))
    print(solution.minDays(6))
    print(solution.minDays(1))
    print(solution.minDays(56))
    print(solution.minDays(820592))
