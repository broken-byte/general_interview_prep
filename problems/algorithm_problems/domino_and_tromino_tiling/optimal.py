class Solution:
    def numTilings(self, n: int) -> int:
        """
        The explanation of the below solution can be found at:
         https://www.youtube.com/watch?v=BlT6VCE6lGc

        Time Complexity: O(n)
        Space Complexity: O(1) Since the dp array is capped at 1001 elements
        """
        mod = 10**9 + 7
        dp: list[int] = [0 for _ in range(1001)]
        dp[0], dp[1], dp[2], dp[3] = 0, 1, 2, 5
        for index in range(4, n + 1):
            dp[index] = 2 * dp[index - 1] + dp[index - 3]
            dp[index] %= mod
        return dp[n]
