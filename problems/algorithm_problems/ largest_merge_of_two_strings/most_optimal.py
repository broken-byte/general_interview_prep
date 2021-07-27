

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        """
        N, M = len(word1), len(word2)
        Time Complexity: O(N^2 + M^2), roughly
        Space Complexity: max(N, M)

        Algorithm: Greedy Algorithm
        ---------------------------
        At each level of the recursive call stack,
        we find the locally optimal choice FIRST. This
        carves a path directly to the right choice
        versus my previous approaches that tried
        all possible states THEN chose the locally optimal
        on the way back up the call stack.
        """
        if len(word1) == 0 or len(word2) == 0:
            return word1 + word2
        elif word1 >= word2:
            return word1[0] + self.largestMerge(word1[1:], word2)
        else:
            return word2[0] + self.largestMerge(word1, word2[1:])


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestMerge(word1="cabaa", word2="bcaaa"))
    print(solution.largestMerge(word1="abcabc", word2="abdcaba"))
