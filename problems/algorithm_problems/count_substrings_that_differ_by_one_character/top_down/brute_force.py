

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        """
        N = len(s)
        M = len(t)
        Time Complexity: O(N*M*min(N, M))
        Space Complexity: O(min(N, M))
        """

        n, m = len(s), len(t)

        def dp(s_index: int, t_index: int, difference: int) -> int:
            # Base Cases
            if s_index < 0 or t_index < 0 or difference < 0:
                return 0
            if difference == 0 and s[s_index] != t[t_index]:
                return 0

            # Recursive Cases for when i, j > 0 and difference is 0 or 1
            answer = 0
            if s[s_index] == t[t_index]:
                dynamic_result = dp(s_index - 1, t_index - 1, difference)
                diff_equals_0: bool = difference == 0
                answer += dynamic_result + 1 if diff_equals_0 else dynamic_result
            else:
                dynamic_result = dp(s_index - 1, t_index - 1, difference)
                answer += dynamic_result + 1
            return answer

        ans = 0
        for i in range(n):
            for j in range(m):
                if (i, j) == (2, 3):
                    print("We got to 2, 3! here: ", dp(i, j, 1))
                ans += dp(i, j, 1)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.countSubstrings(s="aba", t="baba"))
