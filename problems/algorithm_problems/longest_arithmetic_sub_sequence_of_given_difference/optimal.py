

class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        """
        Explanation
        ------------
            For longest arithmetic sequence with difference d:
            Iterate over array and for each value check the length of num - difference and add 1
            For example, think of array as [1, 2, 4, 5, 7, 8, 10] with d = 3
            For a = 1, length = 1
            For a = 2, length = 1
            For a = 4, length = 2 (because cache[1] = 1)
            For a = 5, length = 2 (because cache[2] = 1)
            For a = 7, length = 3 (because cache[4] = 2)
            For a = 8, length = 3 (because cache[5] = 2)
            For a = 10, length = 4 (because cache[7] = 3)
            So result = cache[10] = 4,
            since the longest arithmetic sub sequence is [1, 4, 7, 10]

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        cache: dict = {}
        for num in arr:
            if num - difference in cache:
                cache[num] = cache[num - difference] + 1
            else:
                cache[num] = 1
        return max(cache.values())


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestSubsequence([1, 4, 2, 5, 3], 1))
    print(solution.longestSubsequence(arr=[1, 2, 3, 4], difference=1))
    print(solution.longestSubsequence(arr=[1, 3, 5, 7], difference=1))
    print(solution.longestSubsequence(arr=[1, 5, 7, 8, 5, 3, 4, 2, 1], difference=-2))