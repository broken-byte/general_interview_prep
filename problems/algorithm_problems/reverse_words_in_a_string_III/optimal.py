
class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Time Complexity: O(N) or ~3N
        Space Complexity: O(N) for final output
        """
        s: list[str] = s.split(' ')
        for index, word in enumerate(s):
            s[index] = word[::-1]
        return ' '.join(s)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords(s="Let's take LeetCode contest"))
