

class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        """
        Time Complexity: O(n) ~ 2n
        Space Complexity: O(n)

        Since strings are immutable
        in Python, I don't think we
        can improve the space complexity
        unfortunately :/
        """
        n = len(s)
        restored_string: list[str] = ['' for _ in range(n)]
        for character, destination_index in zip(s, indices):
            restored_string[destination_index] = character
        return "".join(restored_string)


if __name__ == '__main__':
    solution = Solution()
    print(solution.restoreString(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3]))
    print(solution.restoreString(s="abc", indices=[0, 1, 2]))
    print(solution.restoreString(s="aiohn", indices=[3, 1, 4, 2, 0]))
    print(solution.restoreString(s="aaiougrt", indices=[4, 0, 2, 6, 7, 3, 1, 5]))
    print(solution.restoreString(s="art", indices=[1, 0, 2]))